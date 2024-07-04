def build_suffix_array(s):
    n = len(s)
    SA = list(range(n))
    g = [ord(c) for c in s]
    g.append(-1)  # 배열의 끝을 표시하기 위해 -1을 추가
    t = 1

    # SA 배열을 정렬하는 과정
    while t <= n:
        # SA를 (g[x], g[x + t])의 순서쌍을 기준으로 정렬
        SA.sort(key=lambda x: (g[x], g[x + t] if x + t < n else -1))
        tg = [0] * n  # 임시 그룹 번호 배열
        for i in range(1, n):
            prev, curr = SA[i - 1], SA[i]
            # prev + t 혹은 curr + t가 배열의 범위를 넘어가면 -1을 사용
            prev_t_val = g[prev + t] if prev + t < n else -1
            curr_t_val = g[curr + t] if curr + t < n else -1
            # 현재와 이전 요소 비교하여 임시 그룹 번호 할당
            if g[prev] != g[curr] or prev_t_val != curr_t_val:
                tg[curr] = tg[prev] + 1
            else:
                tg[curr] = tg[prev]
        g = tg[:]  # g 배열 업데이트
        t <<= 1  # t를 2배 증가시킴
    return SA


def build_lcp(s, SA):
    n = len(s)
    lcp = [0] * n  # LCP 배열 초기화
    r = [0] * n  # 역순위 배열 초기화
    for i in range(n):
        r[SA[i]] = i
    length = 0  # 현재의 LCP 길이
    for i in range(n):
        if r[i] > 0:
            k = SA[r[i] - 1]
            # LCP 길이 계산
            while i + length < n and k + length < n and s[i + length] == s[k + length]:
                length += 1
            lcp[r[i]] = length
            # LCP 길이 감소시키기
            if length > 0:
                length -= 1
    return lcp


def longest_common_substring(str1, str2):
    str_combined = str1 + "!" + str2  # 두 문자열을 결합
    SA = build_suffix_array(str_combined)
    LCP = build_lcp(str_combined, SA)

    ans = 0
    res = ""
    for i in range(1, len(SA)):
        # 서로 다른 문자열에서 온 접미사인지 확인
        if (SA[i - 1] < len(str1) and SA[i] >= len(str1) + 1) or (
            SA[i - 1] >= len(str1) + 1 and SA[i] < len(str1)
        ):
            # 최장 공통 부분 문자열 업데이트
            if ans < LCP[i]:
                ans = LCP[i]
                res = str_combined[SA[i] : SA[i] + ans]
    return ans, res


str1 = input()
str2 = input()
length, substring = longest_common_substring(str1, str2)
print(length)
print(substring)
