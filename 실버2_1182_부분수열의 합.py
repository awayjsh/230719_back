N, S = map(int, input().split(" "))

lst = list(map(int, input().split(" ")))

subsets = [[]]

ans_list = []

for num in lst :

    size = len(subsets)

    for y in range(size) :

        subsets.append(subsets[y]+[num])

for i in subsets :

    if S == int(sum(i)) :

        ans_list.append(i)

if S == 0 :

    print(len(ans_list) - 1)

else :

    print(len(ans_list))