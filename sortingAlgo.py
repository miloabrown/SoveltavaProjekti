
#QuickSort
#Tarkoitus olla mahdollisimman nopea >ihan eniten täyzii
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


def algoritmi1(nums):

    def _quick_sort(items, low, high):
        if low < high:
        
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


  


#Bubble sort
#Tarkoitus olla hidas ja epäkäytännöllinen (Mä)
def algoritmi2(nums):
    vaihto = True
    while vaihto:
        vaihto = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                vaihto = True   