"""
DIZILER ALGORITMA PYTHON KODLAMALARI
> Diziler (Arrays) ile ilgili algoritma sorularının python ile çözümleri
"""


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



if __name__ == '__main__':
    # import numpy as np
    # arr = np.random.randint(50, size=6)
    # print(arr)
    # print("\nminimum variable: ", min_array(arr))
    # find_min_variable_iteration(arr)








