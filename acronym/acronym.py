def abbreviate(words):
    w = words.replace("-", " ").replace("_", "").split()
    a = [x[0] for x in w]
    return "".join(a).upper()
