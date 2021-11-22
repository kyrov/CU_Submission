score = {}
num = {}
OT = {}
BNK = {}
op2 = []
op3 = []
ans = ''
a = input()
while(len(a)!=1):
    ota,bnk,sco = a.split()
    if(score.get(bnk,5) == 5):
        score[bnk] = 0
    score[bnk] -= int(sco)
    if(num.get(bnk,5) == 5):
        num[bnk] = set()
    num[bnk].add(ota)
    if(OT.get(ota,"no") == "no"):
        OT[ota] = {}
    if(OT[ota].get(bnk,5) == 5):
        OT[ota][bnk] = 0
    OT[ota][bnk] += int(sco)
    a = input()
if(a=='1'):
    for i in score.keys():
        op2.append([score[i],i])
    op2.sort()
    cou = 0
    for i in op2:
        if(cou < 3):
            ans += i[1] + ', '
            cou += 1
elif(a=='2'):
    for i in num.keys():
        op2.append([-len(num[i]),i])
    op2.sort()
    cou = 0
    for i in op2:
        if(cou < 3):
            ans += i[1] + ', '
            cou += 1
elif(a=='3'):
    for i in OT.keys():
        op3 = []
        for j in OT[i].keys():
            op3.append([-OT[i][j],j])
        op3.sort()
        if(BNK.get(op3[0][1],"nope") == "nope"):
            BNK[op3[0][1]] = 0
        BNK[op3[0][1]] += 1
    cou = 0
    for i in score.keys():
        op2.append([-BNK.get(i,0),i])
    op2.sort()
    for i in op2:
        if(cou < 3):
            ans += i[1] + ', '
            cou += 1
print(ans[:len(ans)-2])    
