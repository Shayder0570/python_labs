def transpose(mat: list[list[float | int]]) -> list[list]:


    
    transposed = []
    for i in range(len(mat[0])):
        row = [mat[j][i] for j in range(len(mat))]
        transposed.append(row)
    return transposed


print("transpose")
print(f"[[1, 2, 3]]→{transpose([[1, 2, 3]])}")
print(f"[[1], [2], [3]]→{transpose([[1], [2], [3]])}")
print(f"[[1, 2], [3, 4]]→{transpose([[1, 2], [3, 4]])}")
#print(f"[]→{transpose([])}")
#print(f"[[1, 2], [3]]→{transpose([[1, 2], [3]])}")
