def solution(N, stages):
    answer = []

    fail = {}
    people = len(stages)

    #stage 번호가 1부터 시작하기 때문에
    for i in range(1, N + 1):
        if people == 0:
            fail[i] = 0
        else:
            # i번 stage 수
            fail[i] = stages.count(i) / people
            people -= stages.count(i)

    answer = sorted(fail, key=lambda x: fail[x], reverse=True)

    return answer
