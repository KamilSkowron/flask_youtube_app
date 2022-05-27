A = [1,2,3,4,4,5]

B = list(set(A))

for i in B:
	A.remove(i)
print(A)
