import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
# 전위 순회한 결과 입력
preOrder = []
while True:
    try:
        preOrder.append(int(input()))
    except:
        break


# 후위 순회한 결과
def solution(A):
    if len(A) == 0:
        return

    tempL, tempR = [], []
    # 첫번째 값을 루트 노드로 설정
    mid = A[0]
    # 나머지 배열에 대해 for문 돌며 루트보다 커지는 부분 기록해서 L,R나눔
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
        tempL = A[1:]
    # 왼쪽,오른쪽 순으로 재귀 후 루트 노드값 출력
    solution(tempL)
    solution(tempR)
    print(mid)


solution(preOrder)
