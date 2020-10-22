## Choix de modélisation

Pour commencer, nous allons devoir répondre à la question: "Que dois-je simuler ?" que nous pourrions aussi exprimer comme "Que dois-je modéliser?". Commençons simplement et donnons-nous l'objectif de tester l'impact que le confinement a sur la propagation du virus. 

!!! question 1
	Avec pour objectif de simuler l'effet du déplacement des individus sur une pandémie, quels sont les éléments/entités qui devront faire partie de ma simulation ? Prenez un moment pour réfléchir à cette question avant de passer au paragraphe suivant.

Deux éléments sont fondamentaux dans notre contexte: il faudra bien sur que notre simulateur représente des humains, et pour représenter l'effet du déplacement, il va falloir que ces humains se déplace dans un environnement. 

!!! question 2
	Quelles propriétés les humains et l'environnement devront avoir dans la simulation ? Encore une fois prenez un moment pour essayer de répondre à cette question avant de continuer.

Ici, ce qu'il est important de comprendre, c'est qu'il va falloir choisir ce qui nous semble nécessaire, de ce qui ne l'est pas. Nous est-il nécessaire par exemple de savoir si tel individu porte un Tshirt vert ou une robe jaune ? A priori non, le virus ne semble pas s'intéresser à la mode. Modéliser cette information nous demanderait de faire des efforts inutiles, nous allons donc **faire abstraction** de cette information. 

!!! hint "Definition 1: _Abstraction_"
	L'abstraction est un processus qui permet de représenter des objets réels en objets informatiques simplifiés. Elle consiste donc à séléctionner les caractéristiques pertinentes et nécessaires des objets de celles qui ne le sont pas.


Pouvons-nous nous passer de représenter la position d'une personne dans l'environnement ? Non, cette information doit nécessairement être prise en compte pour tester l'influence du confinement et donc du déplacement de nos individus. Par ces deux exemples de question je vous espère convaincus de l'importance de l'abstraction pour réaliser un simulateur performant. 

Moi voilà, ça va plus loin, mon objectif à moi n'est pas de réaliser un simulateur pour influencer des décisions politiques, je laisse cette tâche aux épidémiologistes. Mon objectif à moi est de réaliser un simulateur pour enseigner l'informatique tout en ayant une introduction à ce qui peut se faire en épidémiologie. Pour cela je dois faire abstraction de plus d'information qu'un épidémiologiste le ferait. Je limiterais donc les informations modélisées à cela:

 * un humain a une position, il a un état de santé (en bonne santé, infecté, guéri), il a deux comportements possible (confiné ou pas).
 * l'environnement est un espace fini à deux dimensions (pas d'obstacles, de décors ou quoi que ce soit d'autre).

Comme Scratch vient par défaut avec un environnement qui est un espace fini à deux dimensions, il n'y a rien a faire à ce sujet. Donc passons directement à la modélisation d'un individu dans cet environnement.

