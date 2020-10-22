## Boucles

Une autre façon dont les ordinateurs et les robots changent notre vie est dans leur capacité à faire face à des tâches répétitives sans s'ennuyer. Mais le programmeur qui les a programmés s'ennuie facilement, il doit donc disposer d'un outil pour s'occuper des répétitions dans son code. C'est à cela que servent les boucles.

```py
# Imagine I want to increment a variable x from 0 to 5 and show its value changing. I could write:
print("No loop")
x = 0
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)
x = x + 1
print("x = ", x)

# But that is highly unreadable and unpractical. Therefore python and most other programming languages use loops. In python we'll use the for loop:

print("\nFor loop")
x = 0
for i in range(5):
  x = x + 1
  print("x = ", x)

# Note that the two previous bits of code give the same output. At first it can be fine to understand "for i in range(5):..." as "repeat 5 times...", although it means a bit more than that.

# Another thing to notice here is the use of indentations in python: the lines 20 and 21 start with a tabulation. This means that the two form a block, and this whole block will be repeated by the for loop in line 19.

# Repetitions can also be handled by while loops. Which leads us to a third way to do the same thing: 
print("\nWhile loop")
x = 0
while x < 5:
  x = x + 1
  print("x = ", x)


```

!!! note "Exercice 3"
    Ajoutez quelques lignes dans le script ci-dessus pour afficher les 20 premiers nombres de la séquence de Fibonacci.


