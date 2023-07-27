N, M = map(int, input().split(" "))
keyword = set()
ans = []

for i in range(N) :

    keyword.add(input())

for j in range(M) :

    memo_set = set(map(str, input().split(",")))

    keywords_to_remove = set(k for k in keyword if k in memo_set)
    
    keyword.difference_update(keywords_to_remove)

    ans.append(len(keyword))

for i in ans :

    print(i)
