
def get(arr):
    even = 0
    odd = 0
    enenNo = None
    oddNo = None
    for i in arr:
        if i % 2 == 0:
            even += 1
            enenNo = i
        else:
            oddNo = i
            odd += 1

    if even == 1:
        return enenNo
    else:
        return oddNo


print(get([2,4,6,7,8,10]))


