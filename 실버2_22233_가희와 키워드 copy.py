N, M = map(int, input().split(" "))
keyword = dict()

for i in range(N) :

    keyword[input()] = 1

res = N

for j in range(M) :

    input_list = input().split(",")
    
    for k in input_list :

        if k in keyword.keys() :

            if keyword[k] == 1 :

                keyword[k] -= 1
                res -= 1

    print(res)
