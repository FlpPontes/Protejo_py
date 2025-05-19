
def conf(s):
    a = len(s)
    if a<8:
        return 'falt'
    O = 0
    p = 0
    for yey in s:
        if yey in '0123456789':
            p += 1
    for yay in s:
        if yay in "!@#$%&<>.,*-_'":
            O += 1
    if a == p:
        return 'number'
    if O <1:
        return 'specil'
    if p < 2:
        return 'crac'
