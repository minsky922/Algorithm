def solution(dartResult):
    cnt = []
    start_idx = 0
    score = {"S": 1, "D": 2, "T": 3}

    for i in range(len(dartResult)):
        temp = dartResult[i]
        # print(temp)
        if temp in score:
            print(temp)
            cnt.append(int(dartResult[start_idx:i]) ** score[temp])
        elif temp == "*":
            cnt[-2:] = [x * 2 for x in cnt[-2:]]
        elif temp == "#":
            cnt[-1] = -cnt[-1]

        if not temp.isnumeric():
            start_idx = i + 1

    # print(cnt)
    answer = sum(cnt)
    return answer
