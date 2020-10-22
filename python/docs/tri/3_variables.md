## Copies de variables

L'avantage de la simplicité du langage de python a un certain coût. Lisez le programme suivant, prédisez le résultat et testez votre prédiction en l'exécutant.

```py
a = 0
b = a
a = 1
print(b)

liste = [1,2,3]
liste2 = liste
liste[0] = 0
print(liste2)
liste = []
print(liste2)
```
Ce résultat est souvent surprenant pour ceux qui découvrent python. On pourrait s'attendre à ce que le premier *print(liste2)* nous indique *[1,2,3]* puisque nous n'avons pas demandé de changer *liste2* et que c'est une copie de *liste*. Mais ce n'est pas le cas. Les valeurs de *liste* ne sont pas copiées dans une nouvelle liste nommée *liste2*.  *liste2* est tout simplement défini pour pointé vers le même emplacement mémoire que *liste*.

La différence est donc que lorsque l'instruction *a = 1* est exéctuée, *a* est défini pour pointer vers un nouvel espace mémoire, alors que lorsque l'instruction *liste[0] = 0* est exéctuée c'est bien la valeur dans l'espace mémoire pointé par *liste[0]* qui est changé.

Cette particularité a de grandes implications concernant l'utilisation des fonctions. En effet, comme le montre le petit programme suivant, une variable donnée comme argument pourra être modifiée par cette fonction si cette variable est une liste, sinon ça ne sera pas le cas.

```py
def change_non_list_arg(n):
  n = 0

v = 1
change_non_list_arg(v)
print(v)

def change_list_arg(liste):
  liste[0] = 0

l = [1]
change_list_arg(l)
print(l)
```

!!! note "Exercice 3"
    - 3.1.  Tout en sachant qu'une fonction peut modifier les listes qui lui sont données en argument, factoriser le programme du tri à bulles en définissant une procédure *permute(liste, index)* qui intervertit les éléments *index* et *index + 1* de *liste*. 
    - 3.2.  Continuner de factoriser le programme en définissant une procédure *bulles(liste)*

