matrix=[]
for i in range(2):
    matrix.append([0]*2)


for i in range(2):
    for j in range(2):
        matrix[i][j]+= int(input("Enter the number for position "+"["+str(i)+"] ["+str(j) +"] : "))

print("\nMatrix(A) :")
for m in matrix:
    print("\t\t",m)

#A^-1 = Adj(A)/Det(A)
# Adjoint of a matrix A
adjoint= [[matrix[1][1],-matrix[0][1]],
      [-matrix[1][0],matrix[0][0]]]
determinant=( matrix[0][0]* matrix[1][1]) - (matrix[0][1] * matrix[1][0])
print("\nDeterminant(A) = ",determinant)



print("\nAdjoint(A) : ")
for rows in adjoint:
    print("\t\t",rows)
#print(deter)
B=[]
for i in range(len(matrix)):
    B.append([0]*2)
#print(B)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        B[i][j] += (adjoint[i][j] // determinant)

print("\n\t\t\t\tAdjoint(A) \nInverse(A) = --------------\n\t\t\t  Determinant(A)")
print("\nInverse(A) : ")
for each_row in B:
    print("\t\t",each_row)