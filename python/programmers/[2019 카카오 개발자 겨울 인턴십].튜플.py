def solution(s):
    s = s[2:-2].split("},{")
    # print("split:",s)
    arr = []
    for i in range(len(s)):
        temp = s[i].split(",")
        arr.append(set(temp))

    # print("before sort:", arr)

    arr.sort(key=lambda x: len(x))

    # print("arr:",arr)

    res = []
    ans = set()
    for i in arr:
        tmp = i - ans
        # print("tmp:",tmp)
        res.append(list(tmp)[0])
        ans = ans | tmp  # union
    #     print("ans: " ,ans)
    # print(res)

    answer = [int(i) for i in res]
    return answer


##### solution 2 ##################


def solution(s):
    answer = []

    s1 = s.lstrip("{").rstrip("}").split("},{")

    new_s = []

    for i in s1:
        new_s.append(i.split(","))

    new_s.sort(key=len)
    # print(new_s)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
    return answer
