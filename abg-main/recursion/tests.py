def fact(n):
    if n < 2:
        return 1
    else:
        fact(n - 1)
#OUTPUT = fact(4)


def fact(n):
    if n < 2:
        return 1
    else:
        n * fact(n - 1)
#OUTPUT = fact(4)


def fact(n):
    if n < 2:
        return res
    else:
        res = 1
        res = res * fact(n - 1)
#OUTPUT = fact(4)


def fact(n):
    res = 1
    if n < 2:
        return res
    else:
        res = res * fact(n - 1)
#OUTPUT = fact(4)


def fact(n):
    res = 1
    if n < 2:
        return res
    else:
        res = res * fact(n - 1)
    return res
#OUTPUT = fact(4)


def rec_fact(n):
    if n < 2:
        return res
    else:
        res = res * rec_fact(n - 1)

def fact(n):
    res = 1
    rec_fact(n)
#OUTPUT = fact(4)


def rec_fact(n, res):
    if n < 2:
        return res
    else:
        res = res * rec_fact(n - 1, res)

def fact(n):
    res = 1
    rec_fact(n, res)
#OUTPUT = fact(4)


def rec_fact(n, res):
    if n < 2:
        return res
    else:
        res = res * rec_fact(n - 1, res)
        return res

def fact(n):
    res = 1
    return rec_fact(n, res)
#OUTPUT = fact(4)


def rec_fact(n, res):
    if n < 2:
        return res
    else:
        res = res * n
        return rec_fact(n - 1, res)

def fact(n):
    res = 1
    return rec_fact(n, res)
#OUTPUT = fact(4)


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)
#OUTPUT = fact(4)
