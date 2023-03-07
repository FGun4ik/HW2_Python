a = 1
result = 1
N = int(input())
for i in range(N, 0, -1):   
    a = a * i
    result += a
result = result / a
print(result)