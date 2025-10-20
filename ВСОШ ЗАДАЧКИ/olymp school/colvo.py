n = int(input())
counts = [] 
for _ in range(n):
  counts.append(int(input()))
t=0 
for i in range(n-1):
  t_k=counts[i]
  k_t=counts[i+1]
  t+=t_k*k_t
print(t)
