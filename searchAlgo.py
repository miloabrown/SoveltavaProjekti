"""

Tänne kaks funktioo (omavalintaiset hakualgoritmit, kunhan on suunnitelmassa mainittujen aikakompleksien sisällä), jotka ottaa listan, sekä haettavan luvun x parametriks.

Printtaa tulos, ei tarvi palauttaa mitään


"""

def algoritmi1(list,x): #O(n)
    ans = -1
    for index,i in enumerate(list):
        if i == x:
            ans = index
            break
        else:
            continue
    # print(ans)
    return ans

def algoritmi2(list,x): #O(log(n))
    first = 0
    last = len(list)-1
    index = -1
    while (first<=last) and (index == -1):
        mid = (first+last)//2
        if list[mid] == x:
            index = mid
        else:
            if x<list[mid]:
                last = mid -1
            else:
                first = mid +1
    # print(index) 
    return index    