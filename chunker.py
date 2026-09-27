"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
import re
from ingest import Document

@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"

def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks

def _split_section(text: str, max_chunk_size: int, overlap_size : int) -> list[str]:
    text = text.strip()
    if not text: 
        return [] 
    if len(text) <= max_chunk_size: 
        return [text]
    
    pattern = re.compile('\n\n|\n|[.!?]\s')
    search_window = 100
    min_chunk_ratio = 0.5
    
    result = []
    start = 0
    n = len(text)
    
    while start < n:
        remaining = n - start
        if remaining <= max_chunk_size:
            tail = text[start:].strip()
            if tail: 
                result.append(tail)
            break
        
        interim_end = start + max_chunk_size
        window_start = max(start, interim_end - search_window)
        window_end = min(n, interim_end + search_window)
        window = text[window_start:window_end]
        
        options = [
            window_start + m.end()
            for m in pattern.finditer(window)
            if (window_start + m.end() - start) >= max_chunk_size * min_chunk_ratio
        ]
        
        split_position = min(options, key=lambda p: abs(p - interim_end)) if options else interim_end
        
        chunk = text[start:split_position].strip()
        if chunk: 
            result.append(chunk)
            
        next_start = split_position - overlap_size
        start = next_start if next_start > start else split_position
        
    return result
        

def split_documents(documents: list[Document], MAX_CHUNK_SIZE: int = config.CHUNK_SIZE, OVERLAP_SIZE: int = config.CHUNK_OVERLAP) -> list[Chunk]:
    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Right now it just calls the fallback. That is the plain, generic behaviour
    the brief is talking about.

    When you write your own strategy, set `produced_by` to
    "chunker.py::split_documents" so your README's Sample Chunks section names
    the right function. `app.py chunks` prints that string for you.

    Things worth thinking about before you write any code:
        - Are your documents short posts or long guides?
        - Is the useful information in one sentence, or spread over a paragraph?
        - Would splitting on paragraph breaks keep more thoughts intact than
        splitting on a character count?
    """
    chunks: list[Chunk] = []
    header_pattern = r'(?=\n#{1,6}\s+)'
    
    for doc in documents: 
        sections = [s.strip() for s in re.split(header_pattern, doc.text) if s.strip()]
        
        headers: list[tuple[int, str]] = []
        doc_chunks: list[str] = []
        
        for section in sections:
            lines = section.split("\n", 1)
            first_line = lines[0].strip()
            body_content = lines[1].strip() if len(lines) > 1 else ""
            
            if first_line.startswith("#"):
                level = len(first_line.split()[0])
                headers = [h for h in headers if h[0] < level]
                headers.append((level, first_line))
            else:
                body_content = section
                    
            breadcrumb = " > ".join(h[1] for h in headers)
            
                
            raw_section_chunks = (
                _split_section(body_content, MAX_CHUNK_SIZE, OVERLAP_SIZE)
                if body_content 
                else []
            )
            
            for chunk_text in raw_section_chunks:
                new_text = f"{breadcrumb}\n{chunk_text}" if breadcrumb else chunk_text
                doc_chunks.append(new_text)
                
        for idx, text in enumerate(doc_chunks):
            chunks.append(Chunk(
                text, 
                doc.source, 
                idx, 
                "chunker.py::split_documents"
            ))
            
    return chunks




def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
