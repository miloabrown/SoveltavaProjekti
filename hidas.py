
def bubble_sort(nums):
    vaihto = True
    while vaihto:
        vaihto = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                vaihto = True

  
