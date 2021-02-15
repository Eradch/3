def m_pow_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return "Error"
    return res


print(m_pow_fun(2, -3))
