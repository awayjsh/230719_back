N, M= map(int, input().split(" "))

trees = list(map(int, input().split(" ")))

min, max = 1, max(trees)



while min <= max:

    mid = (min + max) // 2
    total = 0

    for i in trees :

        if i >= mid :

            total += i - mid

    if total >= M :

        min = mid + 1

    else :

        max = mid - 1

print(max)