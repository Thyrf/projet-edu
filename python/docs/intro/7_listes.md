## Listes

Quand vous vous préparez pour aller faire des courses (ou que vos parents le font), que faites-vous ? Vous prenez autant de bout de papier que vous avez d'achats à faire, ou bien vous prenez un seul bout de papier sur lequel vous notez tout ? J'espère que vous utilisez la deuxième option, pour vos poches et la planète. En programmation c'est pareil. Si on a une liste d'éléments à retenir sur lesquels nous devons faire les mêmes types d'opération, souvent on n'utilisera pas plusieurs variables mais seulement une seule liste.  

!!! note "Exercice 6"
    Dans l'exercice précédent nous avons utilisé la fonction *int()* pour convertir une chaine de caractère en entier. Pour découvrir l'utilisation des listes, reprogrammez la fonction *int()* que nous appelerons *str_to_int(s)*. Utilisez pour cela la chaine de caractère fournine en argument comme une liste de caractères. Accéder pour cela à chacun des caractères à l'aide des crochets ([]). Vous pourrez également utiliser la fonction *ord()* qui retourne le nombre entier correspondant à l'Unicode d'un caractère.


```py
def str_to_int(s):
  # fonction to be defined
  # here is an exemple that shows you how to access the elements of a string as a list of characters
  for i in range(len(s)):
    print(s[i])
  ...

while True:
  s = input('Type a number. I''ll square it for you : ')
  n = str_to_int(s)
  print("The square of this number is :"+str(n*n))

```


