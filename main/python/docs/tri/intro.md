Aller plus loin avec le tri
=====================

Dans ce chapitre nous allons découvrir certaines spécificités du langage python dans le contexte du tri de données. Pour réaliser la totalité des exercices de ce chapitre vous devrez avoir python3 d'installé sur votre machine.

## Le tri à bulles

L'un des algorithmes de tri le plus simple est le tri à bulles. Voici un programme en python qui montre son fonctionnement.  

```py
list_a_trier = [5,9,11,3,2,7,3,87,51,25,9,0]

print("avant tri")
print(list_a_trier)

b_permut = True

while b_permut == True:
  b_permut = False

  for index in range(0,len(list_a_trier)-1):
    # check if in order
    if list_a_trier[index]>list_a_trier[index+1]:
      buff = list_a_trier[index]
      list_a_trier[index] = list_a_trier[index+1]
      list_a_trier[index+1] = buff
      b_permut = True

print("après tri")
print(list_a_trier)
```

!!! note "Exercice 1"
    Lire le programme du tri à bulles, comprendre son fonctionement et le tester.




