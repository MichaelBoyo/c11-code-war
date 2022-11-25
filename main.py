def get(arr):
    even, odd = 0, 0
    even_no, odd_no = None, None
    for i in arr:
        if i % 2 == 0:
            even += 1;
            even_no = i
        else:
            odd_no = i
            odd += 1
    return even_no if even == 1 else odd_no


print(get([2, 4, 6, 7, 8, 10]))
