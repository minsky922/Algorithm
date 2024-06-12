def recursive(n):
    if n<2:
        return n
    return recursive(n-1) + recursive(n-2)
print(recursive(int(input())))