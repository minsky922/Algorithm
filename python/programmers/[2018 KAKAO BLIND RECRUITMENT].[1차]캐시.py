def solution(cacheSize, cities):
    cache = []
    cnt = 0
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.upper()
        if city not in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                # print(cache)
                cnt += 5
            else:
                cache.pop(0)
                cache.append(city)
                # print(cache)
                cnt += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            # print(cache)
            cnt += 1
    answer = cnt

    return answer
