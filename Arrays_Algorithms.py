"""
DIZILER ALGORITMA PYTHON KODLAMALARI
> Diziler (Arrays) ile ilgili algoritma sorularının python ile çözümleri
"""
import numpy as np


def create_array(n): # n elemanlı bir sayı dizisinin girisini yapan fonksiyon
    # import numpy as np
    # arr = np.random.randint(50, size=n)
    arr = []
    for i in range(n):
        x = int(input("eleman: "))
        arr.append(x)

    return arr


def fibonacci_arr(n): # Fibonacci serisinin ilk 10 terimini dizi kullanarak bulan program
    if n <= 0:
        return [0]
    arr = [0, 1]
    while len(arr) <= n:
        next_value = arr[len(arr) - 1] + arr[len(arr) - 2]
        arr.append(next_value)
    return print(arr)


def word_length(word):  # kelimenin uzunluğunu bulan program
    len = 0
    for harf in word:
        len += 1

    return len


def array_max(): # Bir sayı dizisinin en büyük elemanını bulan program
    arr = [4, 3, 2]
    min = arr[0]
    for i in arr:
        if i > min:
            min = i
    return print(min)


def tersten_kelime(): # Girilen kelimeyi tersten yazdıran program
    word = "kelime"
    return print(word[::-1])


def min_array(arr): # random oluşturulan dizinin minimum elemanını bulan program
    # arr = create_array(5)
    min = arr[0]
    # print(arr)
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min


def find_min_variable_iteration(arr): # 10 elemanlı bir sayı dizisinde en küçük elemanın bu dizinin kaçıncı elemanı olduğunu bulan program
    for i in range(len(arr)):
        if arr[i] == min_array(arr):
            return print("iteration of minimum variable", i)


def check_int_average(arr): # 10 elemanlı bir sayı dizisinin ortalaması tam sayı ise bu sayıdan dizide kaç tane olduğunu veren program
    sum = 0
    count = 0
    print(arr)
    for i in range(len(arr)):
        sum += arr[i]

    avr = sum / len(arr)
    print("Ortalama: ", avr)

    if (sum % len(arr) == 0):
        for i in range(len(arr)):
            if arr[i] == avr:
                count += 1
        return print(count)
    else:
        print("Ortalama tam sayı degildir")


def letter_in_sentence(sentence): # Girilen cümlede, girilen karakterden kaç tane olduğunu bulan program
    letter = input("Harf giriniz: ")
    count = 0

    for ch in range(len(sentence)):
        if sentence[ch] == letter:
            count += 1

    return print(count, "adet", letter, "harfi var")


def polindrom_check(word): # Bir yazının polindrom olup olmadığını bulan program
    """
    Tersinden ve düzünden okunuşu aynı olan yazılara polindrom denir.
    """
    ters = word[::-1]

    # print("Word: ", word)
    # print("tersi: ", ters)

    if word == ters:
        print("polindrom")
    else:
        print("polindrom degil")


def reverse_array(arr): # Bir dizide dizi elemanlarının sondan başa gelecek şekilde düzenlenmesini sağlayan algoritma
    # print(arr[::-1])
    new_arr = []
    c = len(arr)
    while c > 0:
        new_arr.append(arr[c - 1])
        c -= 1
    return print(new_arr)


if __name__ == '__main__':




















