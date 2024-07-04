def solution(str1, str2):
    upstr1 = str1.upper()
    upstr2 = str2.upper()
    print(upstr1)
    print(upstr2)
    a_list = []
    b_list = []
    for i in range(len(str1) - 1):
        str = upstr1[i : i + 2]
        if str.isalpha():
            a_list.append(upstr1[i : i + 2])
    for i in range(len(str2) - 1):
        str = upstr2[i : i + 2]
        if str.isalpha():
            b_list.append(upstr2[i : i + 2])

    if len(a_list) == 0 and len(b_list) == 0:
        j = 1 * 65536
    else:
        # 다중 합집합
        a_temp = a_list.copy()
        union = a_list.copy()
        for i in b_list:
            if i not in a_temp:  # b에만 존재하면 합집합에 추가
                union.append(i)
            else:
                a_temp.remove(i)  # 공통으로 존재하면 중복되므로 제거
        inter = []
        # 다중 교집합
        for i in b_list:
            if i in a_list:
                a_list.remove(i)
                inter.append(i)

        j = len(inter) / len(union) * 65536

    answer = int(j)

    return answer
