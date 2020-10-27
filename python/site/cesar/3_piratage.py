## Piratage

Maintenant nous sommmes un pirate
Premiers pas vers le déchiffrement sans la clef
Comment faire: en français il y a plus de *e*. => va suffir d'analyser un message chiffré pour trouver quelle est la lettre la plus fréquente. Il faudra alors décaler le message pour que cette lettre devienne un *e*.


```py
def compteOccurrence(caractere, s):
	res = 0
	for c in s:
		if s == caractere:
			res += 1
	return res
print("compteOccurrence('n','compteOccurrence')")
print(compteOccurrence('n','compteOccurrence'))
```
```py
def histogrammeLettres(ma_chaine):
	res = []

	for i in range(26):
		c = chr(97+i)
		res.append(compteOccurrence(c, ma_chaine))
		
	return res


print("print(histogrammeLettres('aaabbc')) =>")
print(histogrammeLettres('aaabbcz'))
```

```py

def idMaxVal(l):
	res = 0
	max_temp = l[0]
	for i in range(len(l)):
		if l[i]>max_temp:
			max_temp = l[i]
			res = i
	return res
```


```py
# Autre façon de faire:
def creerListeDeZeros(n):
	res = []
	for i in range(n):
		res.append(0)	
	return res
print("creerListeDeZeros(26)")
print(creerListeDeZeros(26))
```

```py
def histogrammeLettres(ma_chaine):
	nb_occurrences_lettres = creerListeDeZeros(26)

	for c in ma_chaine:
		index = getIndexCaractere(c)
		if index>=0 and index<=25:
			nb_occurrences_lettres[index] += 1

	return nb_occurrences_lettres


print("print(histogrammeLettres('aaabbc')) =>")
print(histogrammeLettres('aaabbcz'))
```




