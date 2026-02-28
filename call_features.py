def extract_features(call):
    """
    Convert call information into numbers for AI
    """
    return [
        call["duration"],
        call["call_frequency"],
        call["unknown_number"],
        call["international_call"]
    ]