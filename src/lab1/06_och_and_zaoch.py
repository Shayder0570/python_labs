n=int(input())
och=0
zaoch=0
for i in range(n):
    fam,name,age,lab=input().split()
    if lab=="True":
        och+=1
print(f"{och} {n-och}")