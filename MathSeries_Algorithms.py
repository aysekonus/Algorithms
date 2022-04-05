"""
Serilerin python ile kodlanması.
"""
import math


def taylor_series_e(x, n):
    """
    taylor serisi kullanılarak; dışarıdan girilen x ve N değerine göre e^x'i hesaplayan program.
    """
    e_series = 0
    for i in range(n+1):
        e_series += ((x**i) / math.factorial(i))
    return print(e_series)


def consecutive_series(n): # 1-(1/3)+(1/5)-(1/7)+(1/9)-(1/11)+… serisinin n tane terim için toplamını hesaplayan program
    eq = 1
    for i in range(3, n + 1, 2):
        eq += ((-1)**i) * (1 / i)
    return print(eq)


def cos_series(x, n):
    cos = 0
    for i in range(0, n):
        cos += (((-1)**i) * (x**(2*i)) / math.factorial(2*i))
    return print(cos)


def fact_series(n): # 1'den N'e kadar: (1 / i!) + (i / (n-i)!) serisi
    eq = 0
    for i in range(1, n+1):
        eq += ((1 / math.factorial(i)) + (i / (math.factorial(n - i))))
    return print(eq)


if __name__ == '__main__':
    # Examples
    taylor_series_e(2, 4)
    consecutive_series(4)
    cos_series(2, 4)
    fact_series(4)