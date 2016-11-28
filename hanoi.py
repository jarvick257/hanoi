import math
import time

def error():
	print("INVALID MOVE!")

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

def move(a,b):
	if a.k == 0:
		error()
	else:
		el = a.pop()
		if b.put(el):
			a.put(el)
			error()
	time.sleep(delay)
	printt()

def move3(a,b):
	q = T[3 - (a.idx-1) - (b.idx-1)]
	move(a,b)
	move(a,q)
	move(b,q)
	move(a,b)
	move(q,a)
	move(q,b)
	move(a,b)

def isValidSingleMove(a,b):
	if a.isEmpty(): return 0
	if a.peek() == 1: return 0
	if b.isEmpty(): return 1
	if a.peek() > b.peek() : return 0
	return 1

def isValid3Move(a,b,i):
	if a.peek() != 1: return 0
	if b.peek()%2 != 0: return 0
	if i==0:
		if b.isEmpty(): return 0
	return 1

def automove1():
	if   isValidSingleMove(t1,t2): move(t1,t2)
	elif isValidSingleMove(t1,t3): move(t1,t3)
	elif isValidSingleMove(t2,t1): move(t2,t1)
	elif isValidSingleMove(t2,t3): move(t2,t3)
	elif isValidSingleMove(t3,t1): move(t3,t1)
	elif isValidSingleMove(t3,t2): move(t3,t2)

def automove3():
	for i in range(0,2):
		if   isValid3Move(t1,t2,i): move3(t1,t2); break
		elif isValid3Move(t1,t3,i): move3(t1,t3); break
		elif isValid3Move(t2,t1,i): move3(t2,t1); break
		elif isValid3Move(t2,t3,i): move3(t2,t3); break
		elif isValid3Move(t3,t1,i): move3(t3,t1); break
		elif isValid3Move(t3,t2,i): move3(t3,t2); break

########################################################################################
N=0
while N<3:
	N = input("How many disk do you want? ")
	N = int(N)
	if N < 3:
		print("You need at least 3 disks!")

t1 = tower(N, 1)
t2 = tower(N, 2)
t3 = tower(N, 3)

T = [t1 ,t2, t3]


for i in range(0,N):
	t1.put(N-i)

printt()
count = 0

mode = input("Automatic or Manual mode? a/m ")
if mode == "m":
	starttime = time.time()
	delay = 0
	while t3.k != t3.max:
		i = int(input("Move from tower "))-1
		j = int(input("to tower "))-1
		if i >= 0 and i < 3 and j >= 0 and j < 3 and i!=j:
			if T[i].peek() < T[j].peek() or T[j].isEmpty():
				move(T[i],T[j])
				count = count + 1
			else: error()
		else: error()
else:
	delay = input("Set delay (float, default: 0.2): ")
	starttime = time.time()
	if delay == "": delay = 0.2
	else: delay = float(delay)

	if N%2 == 0:
		move3(t1,t2)
	else:
		move3(t1,t3)
	count = 7
	while t3.k != t3.max:
		automove1()
		automove3()
		count = count + 8

ideal = pow(2,N)-1
endtime = time.time()
print("FINISHED in",count,"moves (Ideal:", ideal, ") and ", endtime - starttime, "seconds")
