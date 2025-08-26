#adjacency matrix
n=6
e=7
edges= [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)] #undirected and unweighted and two way from x to y and y to x
adjMatrix=[]
for i in range(n):
    adjMatrix.append([-1]*n)
for edge in edges:
    x=edge[0]
    y=edge[1]
    #undirected
    adjMatrix[x][y]=1
    adjMatrix[y][x]=1
    
for i in range(n):
    print(i,"->",adjMatrix[i])