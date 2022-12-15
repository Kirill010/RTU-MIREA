A = [0] * 977
f = open("A.txt")
for i in range(976):
    s = float(f.readline())
    A[i] += s
z = 0
B = [0] * len(A)
f = open("Ya!.txt", 'w')
for i in range(1, 975):
    for j in range(976):
        if i + j < len(A):
            z += abs(A[j + i] - A[j])
        else:
            break
    z /= (j - 1)
    q =str(z)
    f.write(q + "\n")
f.close
f.close
f.close

