from itertools import permutations

bol = ['Dhaa','Dhin','Ga','Ka','Kat','Naa','Na','Taa','Tak','Tee','TiRaKiTa','Tita','Tin','Too']
theka = ['Dhaa','Dhin','Dhin','Dhaa','Dhaa','Dhin','Dhin','Dhaa','Dhaa','Tin','Tin','Naa','Naa','Dhin','Dhin','Dhaa']
for i in bol:
    print(bol.index(i)+1,")",i)
print("Select bol to be added: ")
selectbol = list(input().split(" "))
permlist = []
for i in theka:
    permlist.append(i)
for i in selectbol:
    if i not in permlist:
        permlist.append(i)
print(permlist)
print()
permlist = list(permutations(permlist,16))
"""for i in permlist:
    for j in i:
        print(j,end=" ")
    print()"""
print(len(permlist))
