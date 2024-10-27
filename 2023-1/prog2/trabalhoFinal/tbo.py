from random import randint
from time import time

def troca(l, x, y):
	aux = l[x]
	l[x] = l[y]
	l[y] = aux

def bubble1(l):
	n = len(l)
	
	for i in range(n):
		for j in range(n-1):
			if l[j] > l[j+1]:
				troca(l, j, j+1)

def bubble2(l):
	n = len(l)
	
	for i in range(n):
		for j in range(n-1-i):
			if l[j] > l[j+1]:
				troca(l, j, j+1)

def bubble3(l):
	n = len(l)
	
	for i in range(n):
		trocou = False
		for j in range(n-1-i):
			if l[j] > l[j+1]:
				troca(l, j, j+1)
				trocou = True
				
		if not trocou: return


def ssort(l):
	for i in range(len(l)-1):
		
		menor = i
		for j in range(i+1, len(l)):
			if l[j] < l[menor]:
				menor = j
				
		troca(l, i, menor)

def isort(l):
	for k in range(1, len(l)):
		pos = k
		
		while pos > 0 and l[pos] < l[pos-1]:
			troca(l, pos, pos-1)
			pos = pos-1


def mSort(l):
	if len(l) > 1:
		meio = len(l) // 2
		lEsq = l[:meio]
		lDir = l[meio:]
		
		mSort(lEsq)
		mSort(lDir)
		
		merge(l, lEsq, lDir)
		
def merge(l, lEsq, lDir):
	i = 0
	j = 0
	k = 0
	
	while i < len(lEsq) and j < len(lDir):
		if lEsq[i] < lDir[j]:
			l[k] = lEsq[i]
			i += 1
		else:
			l[k] = lDir[j]
			j += 1
		k += 1
		
	while i < len(lEsq):
		l[k] = lEsq[i]
		i += 1
		k += 1
			
	while j < len(lDir):
		l[k] = lDir[j]
		j += 1
		k += 1
			

def qsort(l, inf, sup):
	if sup > inf:
		pos = particao2(l, inf, sup)
		qsort(l, inf, pos-1)
		qsort(l, pos+1, sup)
		
		
def particao2(l, inf, sup):
	pivot = l[inf]
	i = inf+1
	j = sup
	
	while i <= j:
		while i <= j and l[i] < pivot: i += 1
		while i <= j and l[j] >= pivot: j -= 1
		
		if i <= j: troca(l, i, j)
	
	troca(l, inf, j)
	return j
	
	
	
	
	
def particao(l, inf, sup):
	pivot = l[inf]
	menores = []
	maiores = []
	
	#print("particao", l, inf, sup)
	
	for i in range(inf+1, sup+1):
		#print(i)
		if l[i] < pivot:
			menores.append(l[i])
		else:
			maiores.append(l[i])
	
	l2 = menores + [pivot] + maiores
	
	#print(l2)

	#print(l, inf, sup)
	#print(l2, inf, sup)
	
	for i in range(len(l2)):
		l[i + inf] = l2[i]
	
	#print(l)
	return len(menores) + inf





def ordenada(l):
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			return False
	
	return True

def criaLista(n):
	l = []
	
	for i in range(n):
		l.append( randint(0, n) )	
		#l.append( i )
		
	return l
	
def main(args):
	n = int(input("Digite o tamanho da lista: "))
	l1 = criaLista(n)
	l2 = l1.copy()
	l3 = l1[:]
	l4 = l1[:]
	l5 = l1[:]
	l6 = l1[:]
	l7 = l1[:]
	
	t1 = time()
	qsort(l7, 0, len(l7)-1)
	t2 = time()
	
	print( "Quick Sort", ordenada(l7), t2-t1 )
	
	t1 = time()
	mSort(l6)
	t2 = time()
	
	print( "Merge Sort", ordenada(l6), t2-t1 )
	
	t1 = time()
	ssort(l4)
	t2 = time()
	
	print( "Selection", ordenada(l4), t2-t1 )
	
	t1 = time()
	isort(l5)
	t2 = time()
	
	print( "Insertion", ordenada(l5), t2-t1 )
	
	t1 = time()
	bubble3(l3)
	t2 = time()
	
	print( "Bubble 3", ordenada(l3), t2-t1 )
	
	t1 = time()
	bubble2(l2)
	t2 = time()
	
	print( "Bubble 2", ordenada(l2), t2-t1 )
	
	t1 = time()
	bubble1(l1)
	t2 = time()
	
	print( "Bubble 1", ordenada(l1), t2-t1 )
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
