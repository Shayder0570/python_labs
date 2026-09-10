n=int(input())
och=0
zaoch=0
for i in range(n):
    fam,name,age,lab=str(input()).split()
    if lab=="True":
        och+=1
    elif lab=="False":
        zaoch+=1
print(f"{och} {zaoch}")