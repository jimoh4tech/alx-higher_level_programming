def uppercase(str):
    s = ""
    for c in str:
        if (97 <= ord(c) <= 122):
            s += chr(ord(c) - 32)
        else:
            s += c
    print(s)