## Conditions

Dans nos programmes, en fonction de certaines variables, parfois nous voulons faire des choses, parfois nous ne le faisons pas. Pour cela, le dernier ingrédient qui nous manque dans notre arsenal d'outils est la condition. Les conditions sont assez simples et nous les utilisons tous les jours : Est-ce qu'il pleut ? Oui/Non => Prenez un parapluie/ne le prenez pas. Notez qu'en informatique, les conditions sont composées de : un test aboutissant à un booléen (Vrai ou Faux), ce qu'il faut faire si le test est Vrai, et parfois ce qu'il faut faire s'il ne l'est pas.

!!! note "Exercice 5"
    Modifiez le code en suivant les instructions qu'il contient.

```py
# fibonacci: input = 1 integer; output = 1 integer
def fibonacci(n):
  x_nm1 = 0
  x_nm2 = 1
  for i in range(n):
    x_n = x_nm1 + x_nm2
    x_nm2 = x_nm1
    x_nm1 = x_n
  return x_nm1

# I'll take this opportunity to show you one more little instruction: input. When you use input, the user is asked to type something in the terminal which is returned to the program,  allowing to make the code interactive.

while True:
  s = input('Which Fibonacci number do you want? ')
  # as input returns a string and we want a number
  # we convert it to integer
  n = int(s)
  # print the result
  print("Fibonacci(",n,") = ",fibonacci(n),"\n")

# Try it out and try to understand what is going on. One problem you will find (especially if you try to make things crash as I asked you to do) is that if someone types something like "non a number" as an input, the code will crash. Indeed the function int() does not accept to convert non digits. 
# To prevent this we can use a condition and check if our string is made of digits such as:

if s.isdigit():# s.isdigit() returns either True or False
  print("s is a positive number")
  # dosomethingmore
else:
  print("s is not a positive nunmber")
  # dosomethingmore

# (Note that this piece of code will never be executed because it comes after a while True loop)
# Try to add such a condition inside the while loop to remind the user to put numbers if he's not doing so.

```

