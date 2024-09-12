X = [[12,4,6],
     [9,6,8],
     [4,5,8]]
Y = [[3,4,5],
     [9,2,3],
     [7,8,9]]
result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(X)):

     for j in range(len(X[0])):
                 result[i][j] = X[i][j] + Y[i][j]

for r in result:
                     print(r)
