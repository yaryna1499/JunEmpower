def validate_str_to_bool(param=None):
    if not param:
        return
    return param == "1" or "true" in param.lower()
