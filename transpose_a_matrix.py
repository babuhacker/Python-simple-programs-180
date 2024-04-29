# Program to find Transpose a Matrix
# using nested loop
'''
A = [[1,2,3],
     [4,5,6]]

T = [[0,0],
     [0,0],
     [0,0]]

for i in range(len(A)):
     for j in range(len(A)):
          T[j][i] = A[i][j]

for i in T:
     print(i)
'''
# using list comprehension

A = [[1,2,3],
     [4,5,6]]

T = [[A[j][i]for j in range(len(A))] for i in range(len(A[0]))]
for i in T:
     print(i)

