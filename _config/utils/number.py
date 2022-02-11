def str_to_num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)
