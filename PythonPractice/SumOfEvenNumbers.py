#Your code goes here
def even_number(n):
	sum_even=0;
	for i in range(1,n+1):
		if i%2==0:
			sum_even+=i
	return sum_even


n=int(input())
ans = even_number(n)
print(ans)



























