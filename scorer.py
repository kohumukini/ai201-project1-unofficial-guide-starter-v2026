def judge(question, expects, answer, results) -> bool: 
    """
    q: 'give', expect: 'give'
    the expect is in the answer
    """
    return expects.lower().strip() in answer.lower()

"""
LLM as judge
rapidfuzz
"""
def retrieval_hits(expects, results) -> bool:
    """
    Any part of my expect in the results
    """

    return any(expects.strip().lower() for chunk in results)