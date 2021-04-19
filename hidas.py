import unittest

def bubble_sort(nums):
    vaihto = True
    while vaihto:
        vaihto = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                vaihto = True

def bubble_sort_testi():
    print("Testataan satunnaisilla numeroilla")
    random_lista_nums = [5, 8, 9, 10, 100, 1, 64, 80, 35, 18]
    bubble_sort(random_lista_nums)
    print(random_lista_nums)
  

bubble_sort_testi()
