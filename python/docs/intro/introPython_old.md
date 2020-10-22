Introduction à Python
=====================

Pour pouvoir communiquer avec les machines, il faut être en mesure de communiquer avec elles. Pour cela une multitudes de langages existent. Cette page vous propose de découvrir le langage Python très en vogue dans le milieu de l'éducation tout autant que dans le milieu de la recherche pour résoudre des problèmes aussi pointus que ceux d'apprentissage autonome.

Au travers des exercices suivant vous découvrirez des éléments essentiels de tout langage informatique que sont: l'utilisation de variables, de boucles, de conditions et de fonctions. 

## Commentaires et instructions simples

Pour chaque section de cette page, j'utiliserai un code intégré qui vous permettra d'exécuter des scripts python sans quitter cette page, et d'interagir avec le code comme vous le souhaitez. Alors allons-y : lisez le code, essayez de prévoir ce qui va se passer dans le terminal (en noir), et appuyez sur le bouton d'exécution.

Si le programme en python n'apparait pas et que le chargement semble bloqué, essayez de cliquer en haut à gauche sur *open in repl.it* pour l'ouvrir dans un autre onglet. Sinon vous pouvez accéder à une [**version de cette page sans repl.it**](introPythonOff.md).

<iframe height="800px" width="100%" src="https://repl.it/@amauryd/MobileRoboticsSummerschool1Hello?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origine allow-scripts allow-modals"></iframe>

!!! note "Exercice 1"
	Changer le code, changez le texte, est-ce *print()* ça marche sans les gillements ? Pour cela, vous pouvez aussi taper directement des instructions dans le terminal.

## Variables et opérations standard

Les ordinateurs ne font pas que répéter les mêmes choses encore et encore. Ils nous sont utiles car ils peuvent s'adapter à différentes situation. Comment cela marche ? Grâce à des données qui sont collectées et fournies à l'ordinateur. Dans ons programmes, nous appelerons ces données des variables. Une variable est comme une boîte dans laquelle nous mettons des informations auquel notre programme peut accéder autant que nécessaire et changer le contenu.

<iframe height="800px" width="100%" src="https://repl.it/@amauryd/MobileRoboticsSummerschool2Variables?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origine allow-scripts allow-modals"></iframe>

!!! note "Exercice 2"
	Modifiez le code, faites-le planter ! Définissez de nouvelles variables. Peut-on assigner du texte à une variable qui correspondant à un entier précédement ? Peut-on ajouter un entier à une chainge de caractère ? Testez et ainsi vous pourrez devenir autonome en vous familiarisant au message d'erreur que l'ordinateur vous donnera en cas de problème.

## Boucles

Une autre façon dont les ordinateurs et les robots changent notre vie est dans leur capacité à faire face à des tâches répétitives sans s'ennuyer. Mais le programmeur qui les a programmés s'ennuie facilement, il doit donc disposer d'un outil pour s'occuper des répétitions dans son code. C'est à cela que servent les boucles.

<iframe height="800px" width="100%" src="https://repl.it/@amauryd/MobileRoboticsSummerschool3Loops?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origine allow-scripts allow-modals"></iframe>

!!! note "Exercice 3"
	Ajoutez quelques lignes dans le script ci-dessus pour afficher les 20 premiers nombres de la séquence de Fibonacci.


## Fonctions

Connaissez-vous le langage appelé Assembleur ? Prenez quelques secondes pour le regarder sur wikipedia et essayez de déchiffrer ce que fait le programme dans l'image en haut à droite... Ce n'est pas le langage dans lequel vous voulez programmer tous les jours ! Prenez le temps de réfléchir à la chance que vous avez de ne pas avoir à en passer par là et d'utiliser plutôt python.

Cette chance, vous l'avez en partie grâce aux fonctions. Comme en mathématiques, les fonctions peuvent prendre des arguments et retourner une valeur. Vous devriez tous avoir déjà utilisé la fonction cosinus. Le cosinus prend un paramètre, un angle, et renvoie une valeur comprise entre -1 et 1. En informatique, les fonctions se présentent sous de nombreuses formes. Elles peuvent prendre un ou plusieurs arguments ou aucun. Elles peuvent renvoyer des valeurs, mais elles ne sont pas obligées de le faire (dans ce cas, on pourrait appeler cela une procédure). 

Un tel outil permet de rendre notre code lisible, moins répétitif, et de combiner et construire des fonctions les unes avec et sur les autres. C'est ainsi que, grâce à certains programmeurs, votre ordinateur peut comprendre un langage de haut niveau comme python, alors qu'à la base il ne peut comprendre que l'assemblage. Voyons comment utiliser cet outil incroyable sur python. 

<iframe height="800px" width="100%" src="https://repl.it/@amauryd/MobileRoboticsSummerschool4functions?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origine allow-scripts allow-modals"></iframe>


!!! note "Exercice 4"
	Définir une fonction avec un paramètre *n* qui calcule et retourne le nombre d'or en utilisant les *n*ième et *n+1*ième nombres de fibonacci.


## Conditions

Dans nos programmes, en fonction de certaines variables, parfois nous voulons faire des choses, parfois nous ne le faisons pas. Pour cela, le dernier ingrédient qui nous manque dans notre arsenal d'outils est la condition. Les conditions sont assez simples et nous les utilisons tous les jours : Est-ce qu'il pleut ? Oui/Non => Prenez un parapluie/ne le prenez pas. Notez qu'en informatique, les conditions sont composées de : un test aboutissant à un booléen (Vrai ou Faux), ce qu'il faut faire si le test est Vrai, et parfois ce qu'il faut faire s'il ne l'est pas.

!!! note "Exercice 5"
	Modifiez le code en suivant les instructions qu'il contient.

<iframe height="800px" width="100%" src="https://repl.it/@amauryd/MobileRoboticsSummerschool5conditions?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origine allow-scripts allow-modals"></iframe>

## Listes

Quand vous vous préparez pour aller faire des courses (ou que vos parents le font), que faites-vous ? Vous prenez autant de bout de papier que vous avez d'achats à faire, ou bien vous prenez un seul bout de papier sur lequel vous notez tout ? J'espère que vous utilisez la deuxième option, pour vos poches et la planète. En programmation c'est pareil. Si on a une liste d'éléments à retenir sur lesquels nous devons faire les mêmes types d'opération, souvent on n'utilisera pas plusieurs variables mais seulement une seule liste.  

!!! note "Exercice 6"
	Dans l'exercice précédent nous avons utilisé la fonction *int()* pour convertir une chaine de caractère en entier. Pour découvrir l'utilisation des listes, reprogrammez la fonction *int()* que nous appelerons *str_to_int(s)*. Utilisez pour cela la chaine de caractère fournine en argument comme une liste de caractères. Accéder pour cela à chacun des caractères à l'aide des crochets ([]). Vous pourrez également utiliser la fonction *ord()* qui retourne le nombre entier correspondant à l'Unicode d'un caractère.


<iframe height="800px" width="100%" src="https://repl.it/@amauryd/MobileRoboticsSummerschool6lists?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origine allow-scripts allow-modals"></iframe>

## Aller plus loin

!!! note "Exercice 7"
    Allez sur un interpreteur quelconque ([repl](https://repl.it/) ou [*trinket*](trinket.html) par exemple) et faites un programme pour:

    - calculer les nombres *pi* et *e* en utilisant des suites.
    - calculer le pgdc de deux nombres en utilisant l'algorithme d'Euclide
    - calculer les n premiers nombres premiers


## Conclusion

Vous voici maintenant équipé pour vous attaquer à de plus gros projets de programmation.

