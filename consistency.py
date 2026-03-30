def check_consistency(responses):
    unique_responses = set(responses)

    if len(unique_responses) > 1:
        return "Inconsistency Detected (Possible Hallucination)"
    return "Consistent Responses"