## Chiffrement et déchiffrement

def decaleCaractere(c,n):
	ord_shift = ord(c)+n
	if ord_shift<97:
		ord_shift = ord_shift+26
	if ord_shift>122:
		ord_shift = ord_shift-26
	return chr(ord_shift)


def decaleChainearactere(s,n):
	res = ""
	for c in s:
		res += decaleCaractere(c,n)
	return res

print(decaleChainearactere("bienjouevousavezterminelexercicedeux",10))
print(decaleChainearactere(decaleChainearactere("bienjouevousavezterminelexercicedeux",10),-10))


print(decaleChainearactere("vousavezreussiadechiffrerlemessagebienvenudanslemondedelacryptographiefelicitation",17))
mdgchiffre = decaleChainearactere("vousavezreussiadechiffrerlemessagebienvenudanslemondedelacryptographiefelicitation",17)

def compteOccurrence(caractere, s):
	res = 0
	for c in s:
		if c == caractere:
			res += 1
	return res

def histogrammeLettres(ma_chaine):
	res = []

	for i in range(26):
		c = chr(97+i)
		res.append(compteOccurrence(c, ma_chaine))
		
	return res

def idMaxVal(l):
	res = 0
	max_temp = l[0]
	for i in range(len(l)):
		if l[i]>max_temp:
			max_temp = l[i]
			res = i
	return res
histostart = histogrammeLettres("vousavezreussiadechiffrerlemessagebienvenudanslemondedelacryptographiefelicitation")
print(histostart)
idE = idMaxVal(histostart)
print(idE)


histo = histogrammeLettres(mdgchiffre)
idNewE = idMaxVal(histo)
diff = 4-idNewE
print(decaleChainearactere(mdgchiffre,diff))


