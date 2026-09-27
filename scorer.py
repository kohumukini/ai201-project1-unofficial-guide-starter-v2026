def judge(question, expects, answer, results) -> bool: 
    """
    q: 'give', expect: 'give'
    the expect is in the answer
    """
    answer_lower = answer.lower()
    expected_items = [expects] if isinstance(expects, str) else expects
    
    for item in expected_items: 
        if item.lower().strip() not in answer_lower: 
            return False
    
    return True

"""
LLM as judge
rapidfuzz
"""
def retrieval_hits(expects, results) -> bool:
    """
    Any part of my expect in the results
    """

    return any(expects.strip().lower() for chunk in results)