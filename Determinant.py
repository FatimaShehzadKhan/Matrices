#hardquoting values of rows and columns
mat_1=[]
rows = 3
cols = 3
for i in range(rows):
    mat_1.append([0]*cols)

print("Your matrix has now been created")
for i in mat_1:
    print(i)

for i in range(len(mat_1)):
    for j in range(len(mat_1[i])):
        mat_1[i][j]+= int(input("Enter the number for position "+"["+str(i)+"] ["+str(j) +"] : "))


for m in mat_1:
    print(m)

deter=( mat_1[0][0]* mat_1[1][1]) - (mat_1[0][1] * mat_1[1][0])
print(deter)
