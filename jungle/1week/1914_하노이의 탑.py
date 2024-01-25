n = int(input())


def hanoi(n, start, end, sub):
    if n == 1:
        print(start, end)  # 1에서 3으로 옮김
    else:
        hanoi(n - 1, start, sub, end)  # 젤 밑의 원판을 제외한 n-1개를 1에서 2로 옮김
        print(start, end)  # 1에서 3으로 옮긴거 출력
        hanoi(n - 1, sub, end, start)  # 젤 밑의 원판을 제외한 2에서 3으로 옮김


print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)
