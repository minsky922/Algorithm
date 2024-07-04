n, k = map(int, input().split())

use = list(map(int, input().split()))

plugs = []
cnt = 0

# 플러그 안에 전기용품 들어 있으면 continue
for i in range(k):
    if use[i] in plugs:
        continue
    # 플러그가 비어 있으면 집어넣는다
    if len(plugs) != n:
        plugs.append(use[i])
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_one = 0
    temp = 0
    # 현재 꽂혀있는 플러그들 확인
    for plug in plugs:
        # 앞으로 사용할 플러그에 없으면
        if plug not in use[i:]:
            temp = plug
            break
        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면
        elif use[i:].index(plug) > far_one:
            far_one = use[i:].index(plug)
            temp = plug
    plugs[plugs.index(temp)] = use[i]
    cnt += 1

print(cnt)
