## Modules

Tout comme on utilise des intercalaires dans un classeur pour séparer différents types de documents, lorsque l'on travaille sur des programmes complexes il est important pour s'y retrouver de découper de tels programmes en plusieurs morceaux. Les modules sont l'équivalents des intercalaires en python.

Un module est un fichier python qui contient des définitions et des déclarations. Vous apprendrez ici comment créer et utiliser un module python. D'abord créer un ficher *exemple.py* contenant les lignes suivantes:

```py
# Exemple de module python

def multiplier(a, b):
  return a * b
```
Voici notre module exemple crée, qui nous donne accès à la fonction multiplier. Pour utiliser ce module dans un autre programme, il faudra d'abord l'importer à l'aide de l'instruction *import exemple*. Il sera alors possible d'utiliser la fonction *multiplier*, à condition de spécifier où elle se trouve en écrivant par exemple *exemple.multiplier(3,5)*.

!!! note "Exercice 4"
    Créer un module *ModuleTri* qui contient les fonctions *permute()* et *bulles()* et adapter votre programme principal pour qu'il l'utilise. Sans compter les *print*, il ne devrait rester que 3 lignes dans ce programme (import, initialisation de liste, tri).

