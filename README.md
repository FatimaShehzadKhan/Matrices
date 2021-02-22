# Matrices
A = []; B = []; C = []
for i in range(2):
    A.append([0]*2)
    B.append([0]*2)
    C.append([0]*2)


#print("\nmatrix(A) = ", A,"\nmatrix(B) = ",B)
print("For Matrix(A): ")
for i in range(2):
    for j in range(2):
        A[i][j]+= int(input("\nEnter the number for position "+"["+str(i)+"] ["+str(j) +"] : "))

print("\nMatrix(A) = \n")

for num_A in A :
    print(num_A)
print("\nFor Matrix(B): ")
for i in range(2):
    for j in range(2):
        B[i][j] += int(input("\nEnter the number for position " + "[" + str(i) + "] [" + str(j) + "] : "))
print("\nMatrix(B) = \n")
for num_B in B:
    print(num_B)

for i in range(len(C)):
    for j in range(len(B)):
        for k in range(len(B[j])):
            C[i][k] += A[i][j] * B[j][k]

print("\nMatrix(C) = \n")
for row in C:
    print(row)





