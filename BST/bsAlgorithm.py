def binary_search(li, target):
    start=0
    end=len(li)-1

    while start<=end:
        middle=(start+end) //2
        if li[middle] == target:
            return middle
        elif li[middle]>target:
            end=middle-1
        else:
            start=middle+1
    return None
print(binary_search([0,1,2,3,4,5,6], 2))