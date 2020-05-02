# Coursera Python Training 1
# Lucas Silva
# Week 5 - Exercício Extra 2 - Maior entre 3 números

def maximo(n1,n2,n3):
	if n1>n2:
		if n1>n3:
			return n1
	elif n2>n3:
		return n2
	else:
		return n3