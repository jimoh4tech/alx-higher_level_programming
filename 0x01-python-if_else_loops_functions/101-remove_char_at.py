def remove_char_at(str, n):
    s = ""
    i = 0
    for c in str:
        if i != n:
            s += c
        i += 1
    return s