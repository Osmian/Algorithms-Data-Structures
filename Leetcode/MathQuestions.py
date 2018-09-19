def finding():
    A = set([x for x in range(1,101) if x%2==0])
    B = set([i for i in range(10,101) if '5' in str(i)])
    C = set([j for j in range(1,101) if j%3==0])
    D = []
    for x in range(10,100):
        tmp = str(x)
        if int(tmp[0])+int(tmp[1])==10:
                D.append(x)
    D = set(D)
    final_set = B-A
    # final_set = f
    print(final_set)

def evens():
    ct =0
    for x in range(1,41):
        if(x%2==0):
            ct+=1
    print(ct)

evens()


# finding()
