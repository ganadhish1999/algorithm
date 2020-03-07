def add(X, Y):
    result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
    return result

def sub(X, Y):
    result = [[X[i][j] - Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
    return result

def mul(x, y, n):
    if(n==2):
        p = (x[0][0]+x[1][1])*(y[0][0]+y[1][1])
        q = (x[1][0]+x[1][1])*y[0][0]
        r = x[0][0]*(y[0][1] - y[1][1])
        s = x[1][1]*(y[1][0]-y[0][0])
        t = (x[0][0]+x[0][1])*y[1][1]
        u = (x[1][0]-x[0][0])*(y[0][0]+y[0][1])
        v = (x[0][1]-x[1][1])*(y[1][0]+y[1][1])
        temp =[[0,0], [0,0]]
        temp[0][0] = p+s-t+v
        temp[0][1] = r+t
        temp[1][0] = q+s
        temp[1][1] = p+r-q+u
        return temp
    m = n//2
    a1 = [[x[i][j] for j in range(m)] for i in range(m)]
    a2 = [[x[i][j] for j in range(m, n)] for i in range(m)]
    a3 = [[x[i][j] for j in range(m)] for i in range(m, n)]
    a4 = [[x[i][j] for j in range(m, n)] for i in range(m, n)]
    
    b1 = [[y[i][j] for j in range(m)] for i in range(m)]
    b2 = [[y[i][j] for j in range(m, n)] for i in range(m)]
    b3 = [[y[i][j] for j in range(m)] for i in range(m, n)]
    b4 = [[y[i][j] for j in range(m, n)] for i in range(m, n)]

    p = mul(add(a1,a4), add(b1, b4), m)
    q = mul(add(a3, a4), b1, m)
    r = mul(a1, sub(b2, b4), m)
    s = mul(a4, sub(b3, b1), m)
    t = mul(add(a1,a2), b4, m)
    u = mul(sub(a3, a1), add(b1, b2), m)
    v = mul(sub(a2, a4), add(b3, b4), m)
    
    c1 = add(sub(p,t), add(s,v))
    c2 = add(r, t)
    c3 = add(q, s)
    c4 = add(sub(p, q), add(r, u))
    

    for i in range(n):
        for j in range(n):
            if i<m and j<m:
                x[i][j] = c1[i][j]
            elif i<m and j>=m:
                x[i][j] = c2[i][j-m]
            elif i>=m and j<m:
                x[i][j] = c3[i-m][j]
            else:
                x[i][j] = c4[i-m][j-m]
    return x
    
a = [[5,2,6,1], [0,6,2, 0], [3, 8, 1, 4], [1, 8, 5, 6]]
b = [[7,5,8,0], [1,8,2, 6], [9, 4, 3, 8], [5, 3, 7, 9]]
print(mul(a, b, 4))