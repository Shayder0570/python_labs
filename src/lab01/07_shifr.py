stroka=str(input("in: "))
word=""
num="0123456789"
#первый символ
for i in range(len(stroka)):
    if stroka[0]!=(stroka[0]).upper() or stroka[0] in num:
        stroka=stroka[1::]
    else:
        word=stroka[0]
        break
#обрез после точки
for i in range(len(stroka)):
    if stroka[i]==".":
        stroka=stroka[0:i]
        break
#определитель шага между символами
k=0
for i in range(len(stroka)):
    if stroka[i] in num:
        k=i
        stroka=stroka[i+1::]
        break
#слово без первого символа    
n=0
while len(stroka)>(n*(k+1)):
    word=word+stroka[n*(k+1)]
    n+=1
print(f"out: {word}.")