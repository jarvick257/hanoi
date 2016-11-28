import math
import time

def error(a,b):
	print("INVALID MOVE!  - from", a.idx, "to",b.idx )

class tower:
	def __init__(self, N, idx):
		self.max = N
		self.k = 0
		self.e = []
		self.idx = idx
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

	def read(self,i):
		return self.e[self.max - 1 - i]

	def isEmpty(self):
		if self.k==0: return 1
		else: return 0

	def peek(self):
		if self.isEmpty() == 0:
			return self.e[self.k-1]
		else: return 0

def printt():
	for i in range(0,t1.max):
		s = str(t1.read(i)) + "  " + str(t2.read(i)) + "  "  + str(t3.read(i))
		print(s)
	print("---------")

def move(a, b):
	if a.k == 0:
		error(a,b)
		exit()
		return -1
	else:
		el = a.pop()
		if b.put(el):
			a.put(el)
			error(a,b)
			exit()
			return -1
	printt()
	return 0

def move3(a,b):
	q = 3 - a - b
	a = T[a]
	b = T[b]
	q = T[q]
	d = 0.2
	time.sleep(d)
	move(a,b)
	time.sleep(d)
	move(a,q)
	time.sleep(d)
	move(b,q)
	time.sleep(d)
	move(a,b)
	time.sleep(d)
	move(q,a)
	time.sleep(d)
	move(q,b)
	time.sleep(d)
	move(a,b)
	time.sleep(d)

def isValidSingleMove(a,b):
	if a.isEmpty(): return 0
	if a.peek() == 1: return 0
	if b.isEmpty(): return 1
	if a.peek() > b.peek() : return 0
	return 1

def automove1():
	if isValidSingleMove(t1,t2): move(t1,t2)
	elif isValidSingleMove(t1,t3): move(t1,t3)
	elif isValidSingleMove(t2,t1): move(t2,t1)
	elif isValidSingleMove(t2,t3): move(t2,t3)
	elif isValidSingleMove(t3,t1): move(t3,t1)
	elif isValidSingleMove(t3,t2): move(t3,t2)

def isEven(n):
	return n%2==0

def automove3(start):
	if isEven(t1.peek()) and t1.peek() != 0:
		move3(start,0)
		return 0
	elif isEven(t2.peek()) and t2.peek() != 0:
		move3(start,1)
		return 1
	elif isEven(t3.peek()) and t3.peek() != 0:
		move3(start,2)
		return 2
	elif t1.isEmpty():
		move3(start,0)
		return 0
	elif t2.isEmpty():
		move3(start,1)
		return 1
	elif t3.isEmpty():
		move3(start,2)
		return 2

########################################################################################
N=0
while N<3:
	N = input("How many disk do you want? ")
	N = int(N)
	if N < 3:
		print("You need at least 3 disks!")

t1 = tower(N,1)
t2 = tower(N,2)
t3 = tower(N,3)

T = [t1 ,t2, t3]


for i in range(0,N):
	t1.put(N-i)

printt()
print(t1.peek())
count = 0

mode = input("Automatic or Manual mode? a/m")
if mode == "m":
	while t3.k != t3.max:
		i = int(input("Move from tower "))-1
		j = int(input("to tower "))-1
		if i >= 0 and i < 3 and j >= 0 and j < 3 and i!=j:
			move(T[i],T[j])
			count = count +1
		else: error()
	print("FINISHED in",count,"moves, Ideal:", pow(2,N)-1)
else:
	pos3 = 0;
	if isEven(N):
		move3(0,1)
		pos3 = 1
	else:
		move3(0,2)
		pos3 = 2

	while t3.k != t3.max:
		automove1()
		pos3 = automove3(pos3)
