from collections import Counter
from math import factorial
from time import clock


def m(*arg):
	p = 1
	for i in Counter(arg).values():
		p *= factorial(i)
	return p


def gen_consequences(n, k, hint = None):
	if hint == None:
		first = n-k+1
	else:
		first = min(hint, n-k+1)
	if k == 0 and n == 0:
		yield []
		return None
	if k == 0 and n != 0:
		return None
	if k == 1:
		yield [first]
		return None
	for first in range(first, 0, -1):
		if first*k < n:
			break
		for i in gen_consequences(n-first, k-1, first):
			i.append(first)
			yield i


Mn = []


def M_gen(N):
	global Mn
	Mn = []
	for n in range(0, N+1):
		sum = 0
		if n == 0:
			Mn.append(1)
			continue
		for k in range(1, n+1):
			sum += int((factorial(n)*n**(n-k-1))/factorial(n-k))
		Mn.append(sum)


def c(n, *arg):
	p = factorial(n)
	for i in arg:
		p = int(p/factorial(i))
	return p


def M_mult(*arg):
	p = 1
	for i in arg:
		p *= Mn[i]
	return p


Sn = []


def S_gen(N):
	global Sn
	Sn = [[0 for j in range(N+1)] for i in range(N+1)]
	Sn[0][0] = 1
	for n in range(1, N+1):
		for k in range(1, N+1):
			Sn[n][k] = Sn[n-1][k-1] + (n-1)*Sn[n-1][k]


def mean(ls):
	s = 0
	for n, i in enumerate(ls):
		s += n*i
	return s


def hf(*ls):
	prod = 1
	for e in ls:
		prod*=e**(e-1)
	return prod


if __name__ == "__main__":
	N = 10
	M_gen(N)
	print(Mn)
	res = open("res.txt", 'w')
	for n in range(1, N+1):
		start = clock()
		Cl = [0 for i in range(n+1)]
		for k in range(1, n+1):
			for ls in gen_consequences(n, k):
				Cl[k] += int((c(n, *ls)*M_mult(*ls))/m(*ls))
		print(n)
		print("all  : ", mean(Cl)/(n**n))
		res.write(str(mean(Cl)/(n**n))+"\n")
		print(Cl)
		S_gen(n)
		Cl = Sn[n]
		print(Cl)
		Cl = list(map((lambda x: x / (factorial(n))), Cl))
		print("biect: ", mean(Cl))
		print("time: ", clock()-start)
	res.close()

	n = 50
	sum = 0
	for lc in range(1, n+1):
		for k in range(0, n - lc+1):
			for ls in gen_consequences(n-lc, k):
				sum += int(c(n, *ls)*lc**(k-1) * hf(*ls) / m(*ls))
	print(sum)


