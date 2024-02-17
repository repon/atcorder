N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A)
B = sorted(B)
m_min = 10 ** 9 + 1
if max(min(A), min(B)) > min(max(A), max(B)):
    m_min = abs(max(min(A), min(B)) - min(max(A), max(B)))
else:
    for n in range(N):
        for m in range(M):
            diff = abs(A[n] - B[m])
            if diff <= m_min:
                m_min = diff
            else:
                break

print(m_min)
