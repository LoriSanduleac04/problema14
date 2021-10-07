n=int(input('Introduceti numarul de linii: '))
matrice=[]
principal=0
secundar=0
msp=0
mjp=0
mss=0
mjs=0
for i in range (0,n):
    a=[]
    for j in range (0,n):
        a.append(int(input()))
    matrice.append(a)
for i in range(0,n):
    for j in range(0,n):
        print(matrice[i][j], end=" ")
    print()
for i in range(0, n):
        for j in range(0, n):
            # Diagonala principala
            if (i == j):
                principal += matrice[i][j]
            # Diagonala secundara
            if ((i + j) == (n - 1)):
                secundar += matrice[i][j]
            #Mai sus de diagonala principala
            if (i > j):
                msp += matrice[i][j]   
            #Mai jos de diagonala principala
            if (i < j):
                mjp += matrice[i][j]  
            #Mai sus de diagonala secundara
            if ((i+j) < (n-1)):
                mss += matrice[i][j]  
            #Mai jos de diagonala secundara
            if ((i+j) > (n-1)):
                mjs += matrice[i][j] 
            
print(principal,'suma componentelor care se află pe diagonala principală')
print(secundar,'suma componentelor care se află pe diagonala principală')
print(msp,'suma componentelor care se află mai sus de diagonala principală')
print(mjp,'suma componentelor care se află mai jos diagonala principală')
print(mss,'suma componentelor care se află mai sus de diagonala secundara')
print(mjs,'suma componentelor care se află mai jos diagonala secundara')