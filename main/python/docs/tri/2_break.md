## Break et continue

Les déclarations *break* et *continue* permettent d'alterer le fonctionnement normal des boucles que vous avez découvert dans le chapitre précédent. Les boucles, comme nous l'avons vu, permettent de répéter un bloc d'instructions tant qu'un test défini avec la boucle est vérifié. Cependant il est parfois souhaité d'interférer avec ce fonctionnement depuis l'intérieur de la boucle, pour passer directement au bloc suivant (l'itération suivante), ou pour tout simplement arrêter la boucle. C'est exactement ce à quoi servent respectivement les déclarations *continue* et *break*.

!!! note "Exercice 2"
    Tester le programme suivant et à travers ce que vous avez appris dans cette section, modifier le programme du tri à bulles afin qu'il marche après avoir remplacé la boucle principale par une boucle *while True:*

```py
for i in range(10):
  if i == 5:
    continue
  print(i)

i = 0
while i < 10:
  print(i)
  if i == 5:
    break
  i = i + 1
```

