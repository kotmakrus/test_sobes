f = open('27_A.txt')
n = int(f.readline())
k, s = 89, 0
max_sum = 0
min_len = 10 ** 10

elements = {0: (0, 0)}
res = []

for j in range(1, n + 1):
    s += int(f.readline())
    if s % k in elements:
        if s - elements[s % k][0] > max_sum:
            max_sum = s - elements[s % k][0]
            min_len = 10 ** 10
        if s - elements[s % k][0] == max_sum:
            min_len = min(min_len, j - elements[s % k][1])
    else:
        elements[s % k] = (s, j)

print(min_len)
