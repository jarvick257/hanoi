import math

def error():
	print("INVALID MOVE!")

class tower:
	def __init__(self, N):
		self.max = N
		self.k = 0
		self.e = []
		for i in range(0,N):
			self.e.append("|")

	def show(self):
		i = self.max-1
		while i>=0:
			print(self.e[i])
			i = i-1

	def put(self, el):
		if self.k == 0 or self.e[self.k-1] > el:
			self.e[self.k] = el
			self.k = self.k+1
			return 0
		else:
			error()
			return -1

	def pop(self):
		self.k = self.k-1
		e = self.e[self.k]
		self.e[self.k] = "|"
		return e

	def peek(self,i):
		return self.e[self.max - 1 - i]

def printt():
	for i in range(0,t1.max):
		s = str(t1.peek(i)) + "  " + str(t2.peek(i)) + "  "  + str(t3.peek(i))
		print(s)

def move(a, b):
	if a.k == 0:
		error()
		return -1
	else:
		el = a.pop()
		if b.put(el):
			a.put(el)
			return -1
	return 0
########################################################################################
N=0
while N<3:
	N = input("How many disk do you want? ")
	N = int(N)
	if N < 3:
		print("You need at least 3 disks!")

t1 = tower(N)
t2 = tower(N)
t3 = tower(N)

T = [t1 ,t2, t3]


for i in range(0,N):
	t1.put(N-i)

printt()
count = 0
while t3.k != t3.max:
	i = int(input("Move from tower "))-1
	j = int(input("to tower "))-1
	if i >= 0 and i < 3 and j >= 0 and j < 3 and i!=j:
		move(T[i],T[j])
		count = count +1
	else: error()
	printt()
	
print("FINISHED in",count,"moves. Ideal:", pow(2,N)-1 )
