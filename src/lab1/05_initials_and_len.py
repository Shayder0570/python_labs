name=" ".join(str(input("ФИО:")).split())
splt_name=name.split()
short_name="".join([word[0].upper() for word in splt_name]) + "."
print(f"Инициалы: {short_name}")
print(f"Длина (символов): {len(name)}")