import random
import time
import matplotlib.pyplot as plt

# definition de la fonction quicksort
# use as: quickSort(liste), comme bulles()

def partition(l, low, high):
	i = (low-1)
	pivot = l[high]

	for j in range(low, high):
		if l[j] <= pivot:
			i = i+1
			l[i], l[j] = l[j], l[i] 
			
	l[i+1], l[high] = l[high], l[i+1]
	return (i+1)

def quickSort(l, low = 0, high = -1):
	if high == -1:
		high = len(l)-1
	if len(l) == 1:
		return l
	if low < high:
		pi = partition(l, low, high)
		quickSort(l, low, pi-1)
		quickSort(l, pi+1, high)

# fin de définition de Quicksort

list_tailles = range(100,1000,100)
temps_wrt_taille = [] # a remplir dans la boucle à l'aide du module time et de la fonction time.perf_counter()

for taille_liste in list_tailles:
	# pour chaque taille de liste, faire le tri
	quickSort(list_a_trier)

# plot result
plt.plot(list_tailles, temps_wrt_taille, label='Quicksort')
plt.legend()
plt.show()
