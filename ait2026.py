def aitsum(arr):
    sum = 0
    for i in arr:
        sum += i    
    return sum

def aitavg(arr):
    sum = 0 
    count = 0
    for i in arr:
        count += 1
        sum += i
    return sum / count


def aitmin(arr):
    min = float('inf')
    for i in arr:
        if min > i:
            min = i
    return min


def aitmax(arr):
    max = float('-inf')
    for i in arr:
        if max < i:
            max = i
    return max 

def aitcount(arr):
    count = 0
    for i in arr:
        count += 1
    return count
    