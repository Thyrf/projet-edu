## Fonctions

Connaissez-vous le langage appelé Assembleur ? Prenez quelques secondes pour le regarder sur wikipedia et essayez de déchiffrer ce que fait le programme dans l'image en haut à droite... Ce n'est pas le langage dans lequel vous voulez programmer tous les jours ! Prenez le temps de réfléchir à la chance que vous avez de ne pas avoir à en passer par là et d'utiliser plutôt python.

Cette chance, vous l'avez en partie grâce aux fonctions. Comme en mathématiques, les fonctions peuvent prendre des arguments et retourner une valeur. Vous devriez tous avoir déjà utilisé la fonction cosinus. Le cosinus prend un paramètre, un angle, et renvoie une valeur comprise entre -1 et 1. En informatique, les fonctions se présentent sous de nombreuses formes. Elles peuvent prendre un ou plusieurs arguments ou aucun. Elles peuvent renvoyer des valeurs, mais elles ne sont pas obligées de le faire (dans ce cas, on pourrait appeler cela une procédure). 

Un tel outil permet de rendre notre code lisible, moins répétitif, et de combiner et construire des fonctions les unes avec et sur les autres. C'est ainsi que, grâce à certains programmeurs, votre ordinateur peut comprendre un langage de haut niveau comme python, alors qu'à la base il ne peut comprendre que l'assemblage. Voyons comment utiliser cet outil incroyable sur python. 

```py
# Here are a few examples of function declarations (definition)
# printHelloWorld: no arguments, no output
def printHelloWorld():
  print("Hello world")

# div: input = 2 integers; output = 1 float
def div(a,b):
  return a/b

# splitStringAtComma: input = 1 string; output = list of strigns
def splitStringAtComma(s):
  return s.split(",")

# fibonacci: input = 1 integer; output = 1 integer
def fibonacci(n):
  x_nm2 = 0 # x_{n-1}
  x_nm1 = 1 # x_{n-2}
  for i in range(n):
    x_n = x_nm1 + x_nm2 # x_n
    x_nm2 = x_nm1
    x_nm1 = x_n
  return x_nm1

# those were only the definitions of the functions. Now that they are defined we can use them as such:
printHelloWorld()
f = div(1,4)
l = splitStringAtComma("str1,str2")
r = fibonacci(10)

print(f)
print(l)
print(r)

```


!!! note "Exercice 4"
    Définir une fonction avec un paramètre *n* qui calcule et retourne le nombre d'or en utilisant les *n*ième et *n+1*ième nombres de fibonacci.


