import unittest

def partition(nums, low, high):
    
    vipu = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < vipu:
            i += 1

        j -= 1
        while nums[j] > vipu:
            j -= 1

        if i >= j:
            return j

       
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):

    def _quick_sort(items, low, high):
        if low < high:
        
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

def testi_luokat():
    
    print("Testataan quick_sortia alkioilla")
    random_lista_nums = [10, 2, 55, 8, 91, 35, 65, 100, 105, -1]    
    quick_sort(random_lista_nums)
    print(random_lista_nums)

testi_luokat()

