import math
from decimal import Decimal as D


# 92653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647
pinr = 3.1
dp = 4

nomi = 1
dnom = 1


def calc(a, b, d):
    res = D(a / b)
    return round(res, d)

def main():
    global nomi, dnom, dp
    if calc(nomi, dnom, dp) < pinr:
        nomi += 1
        main()
    elif calc(nomi, dnom, dp) > pinr:
        dnom += 1
        main()
    else:
        print('{0}/{1}'.format(nomi, dnom))

main()