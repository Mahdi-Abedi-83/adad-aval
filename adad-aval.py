def tabe(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
			break
	else:
			return True
			
sum = 0
last = 0
for i in range(2, 1000000):
	if tabe(i):
		last = i
		sum += 1
		print(i)
		
		
		
print("----------------")
print("tedad adad ha=", sum)
print("last adad=", last)
