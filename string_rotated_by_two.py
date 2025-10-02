def is_rotated_by_two(a, b):
    if len(a) != len(b):
        return 0
    return 1 if a[2:] + a[:2] == b or a[-2:] + a[:-2] == b else 0

a = "amazon"
b = "azonam"
print(is_rotated_by_two(a, b))  
