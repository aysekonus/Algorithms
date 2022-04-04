"""
TEMEL SAYILAR ALGORITMA PYTHON KODLAMALARI
> Temel Kavramlar ve Sayılar ile ilgili algoritma sorularının python ile çözümleri
"""

from datetime import date

def square_sum(a, b):
    sum = a*a + b*b
    return sum


def pow_three_sum(num): # 1'den n'e kadar olan sayılarının küplerinin toplamını bulan program
    sum = 0
    for i in range(num):
        sum = sum + pow(i+1, 3)
        print(pow(i+1, 3))
    return sum


def age_calculator(year): # Doğum tarihi girilen kişinin yaşını hesaplayan program
    today = date.today().year
    age = today - year
    return age


def factorial_calculator(f): # Girilen sayının faktöriyelini bulan program
    fact = 1
    for i in range(f):
        fact = fact * (i+1)
    return fact


def multiplication_with_sum(num1, num2): # Çarpma işlemini toplama kullanarak bulan program
    sum = 0
    for i in range(num2):
        sum = sum + num1
    return sum


def divide_with_extraction(num1, num2): # Bölme işlemini çıkarma kullanarak yapan program
    sayac = 0
    for i in range(num1):
        num1 = num1 - num2
        sayac = sayac + 1
        if num1 == 0:
            break
    return sayac


def mod_calculator(num1, num2): # Girilen sayının istenilen sayıya göre mod işlemini yaptıran program
    while num1 >= num2:
        num1 = num1 - num2
    return print(num1)


def step_find(num): # girilen sayının kaç basamaklı olduğunu söyleyen program
    digits = 0
    while num > 0:
        digits += 1
        num //= 10

    return print(digits)


def armstrong_check(num): # Girilen 3 basamaklı bir sayının basamaklarının küpleri toplamı sayının kendine eşit olup olmadığını bulan program
    b3 = num % 10
    b2 = int((num % 100 - num % 10) / 10)
    b1 = int((num - num % 100) / 100)
    # print(b1, b2, b3)
    sum = pow(b1, 3) + pow(b2, 3) + pow(b3, 3)
    # print(sum)
    if sum == num:
        print("esit")
    else:
        print("degil")


def even_odd(n): # 1'den n' kadar olan çift sayıların toplamının tek sayıların toplamına oranını bulan program
    even_sum = 0
    odd_sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i

    return even_sum/odd_sum


def tam_square_nums(n): # 1'den n'e kadar sayılar arasındaki tam kare sayıları ekrana yazdıran program
    num = 1
    while num <= n:
        sqrt = pow(num, 2)
        num += 1
        if sqrt <= 1000:
            print(sqrt)


def multiply_table():
    for i in range(1,10):
        for j in range(1,10):
            print(i*j)
        print("\n")


def dost_num(num1, num2):
    """
    X,Y pozitif olmak üzere, eğer x sayısının çarpanları toplamı y sayısına
    ve aynı zamanda y sayısının çarpanları toplamı x sayısına eşit ise bu sayılar dost sayılardır.
    Buna göre girilen iki sayının dost olup olmadığını bulan program
    """
    t1 = 0
    t2 = 0

    for i in range(1, num1):
        if num1 % i == 0:
            t1 += i
    for i in range(1, num2):
        if num2 % i == 0:
            t2 += i

    if (t1 == num2) and (t2 == num1):
        return print(num1, "ve", num2, "dost sayılardır")
    else:
        return print(num1, "ve", num2, "dost sayılar değildir.")


def fibonacci_arr(n): # fibonacci serisinin ilk n terimini yazdıran program
    if n <= 0:
        return [0]
    arr = [0, 1]
    while len(arr) <= n:
        next_value = arr[len(arr) - 1] + arr[len(arr) - 2]
        arr.append(next_value)
    return print(arr)


def perfect_num(num): # Girilen sayinin mukemmel sayi olup olmadıgını bulan program
    """
    Mükemmel sayı, sayılar teorisinde, kendisi hariç pozitif tam bölenlerinin toplamı kendisine eşit olan sayı.
    """
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return print(num, "mükemmel sayıdır")

    else:
        return print(num, "mükemmel sayı degildir")


def us_al(num, us): # us alan program
    out = 1
    for i in range(us):
        out = out * num
    print(out)


def decimal_to_binary(num): # Girilen decimal (onluk) bir sayının binary (ikilik) bir sayıya dönüştüren program
    if num >= 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


def ideal_kilo_calculate(): # Boyu ile kilosu girilen kişinin ideal kiloda mı olduğunu gösteren program
    cins = int(input("Cinsiyetiniz kadın ise 1, Erkek ise 0 giriniz: "))
    boy = (int(input("Boyunuzu cm olarak giriniz: "))) / 100
    kilo = int(input("Kilonuzu kg olarak giriniz: "))

    def vci(boy, kilo):
        vci = kilo / (boy*boy)
        return vci
    if cins == 1:
        if (vci(boy, kilo) >= 19) and (vci(boy, kilo) <= 24):
            print("ideal kilodasiniz")
        else:
            print("ideal kiloda degilsiniz")
    else:
        if (vci(boy, kilo) >= 20) and (vci(boy, kilo) <= 25):
            print("ideal kilodasiniz")
        else:
            print("ideal kiloda degilsiniz")


def orj_num_check(num):
    """
    Girilen dört basamaklı sayılardan ilk iki basamağı ile son iki basamağının toplamının karesi,
    sayının kendine eşit olan sayılara orijinal sayı denir.
    Girilen sayının orijinal olup olmadığını bulan program
    """
    bas1 = int((num - (num % 100)) / 100)
    bas2 = (num - 1000) % 100

    if (bas1 + bas2) ** 2 == num:
        return print(num, "orijinal sayidir")
    else:
        return print(num, "orijinal sayi degildir")


def basamak_check(num): # 4 haneli bir sayının birler, onlar, yüzler ve binler hanesini bulan program
    bas1 = int((num - (num % 1000)) / 1000)
    bas2 = int(((num - (num % 100)) / 100) % 10)
    bas3 = int((((num - (num % 10)) - 1000) / 10) % 10)
    bas4 = (num % 10)

    print("binler, yüzler, onlar, birler: ", bas1, bas2, bas3, bas4)


def display_asal_nums(alt, ust): # n-m arasında kaç asal sayı vardır gösteren program
    for num in range(alt, ust + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


def avr_num_list(n):
    """
    Arka arkaya girilen rastgele 10 tam sayının ortalaması ile bu sayılardan en büyük ve en küçük olanın ortalamasını
    bularak elde edilen bu iki ortalamanın farkını bulan program
    """
    nums = []
    for i in range(1, n+1):
        print(i, ". sayi:")
        a = int(input())
        nums.append(a)

    avr = sum(nums) / len(nums)
    avr2 = (max(nums) + min(nums)) / 2

    return print("\nSonuc: ", abs(avr - avr2))


if __name__ == '__main__':
    step_find(5423) # example
