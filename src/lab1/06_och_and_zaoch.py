n=int(input("in_1: "))
och=0
zaoch=0
for i in range(n):
    fam,name,age,lab=input(f"in_{(i+2)}: ").split()
    if lab=="True":
        och+=1
print(f"out: {och} {n-och}")