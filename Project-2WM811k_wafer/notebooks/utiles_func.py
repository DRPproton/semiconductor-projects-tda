def unwrap_failure_type(failure_type):
    if isinstance(failure_type, np.ndarray):
        failure_type = failure_type.tolist()
    if isinstance(failure_type, list):
        if len(failure_type) == 0:
            return None
        value = failure_type[0]
    if isinstance(value, list):
        if len(value) == 0:
            return None
        value = value[0]
    value = value.strip().strip("'").strip('"')
    return value