
def validate_str_to_bool(param=None):
    if not param:
        return
    return param.lower() == 'true' or param == '1'
