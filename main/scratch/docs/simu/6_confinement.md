## Modéliser le confinement

Joli travail ! Mais voilà, pour l'instant, nous n'avons pas beaucoup de contrôle sur ce qui se passe. Et pour répondre à notre question de "Qu'est ce qui se passerait si...", il nous manque quelque chose. 

Si vous vous souvenez bien, quelques paragraphes plus haut, nous parlions de confinement. Nous avons même une caractéristique de chacun de nos individus qui permet de l'immobiliser si cette caractéristique de confinement est définie comme vrai (ou "oui" dans notre programme pour être exact). L'objectif est maintenant d'utiliser cette caractéristique pour répondre à notre question: "Que se passerait-il si *n*% de la population était confinée". Représentons ce *n* par une variable.

!!! question 3
	Est-ce que *n* doit être privée ou globale (une valeur indépendante pour chaque individu ou une valeur partagée par tous) ?

??? note "Réponse"
	Cette variable doit être globale. Elle caractérise toute la population. Si 10% de la population est confinée, ce pourcentage est valable pour chaque individu.

!!! note "Exercice 6"
	Créer une variable globale nommée *PourcentageConfiné* et à l'aide de la fonction "nombre aléatoire entre ... et ..." changer votre programme pour que *PourcentageConfiné* % de la population reste confiné (immobile). 

??? note "Solution exercice 6"
	![Confinement image](simulateur/exercice6/6_confiner.png)
	Créer la fonction DéfiniConfinemenet et appelez là dans les fonction. Si vous avez un problème pour comprendre ce programme, imaginez que vous ayez un énorme dé à 100 faces. "nombre aléatoire entre 1 et 100" vous donne le résultat d'un tel dé. Maintenant imaginez que *PourcentageConfiné* est égal à 20. Je voudrais avoir 20 chances sur 100 que ma variable *confiné* soit définie comme "oui" et c'est bien cec qui se passe si je le fait pour toutes les valeurs de dé inférieures à 20.

Définissez le pourcentage à différentes valeurs et regardez la propagation du virus. Remarquez que vous pouvez choisir quelles variables sont affichées sur votre environnement en cochant ou non la boîte à gauche de vos variables dans l'onglet code>Variables. Puisque seul le pourcentage est globale, seule cette variable devrait être affichée. En faisant un clic droit sur cette variable dans l'environnement vous pouvez aussi séléctionner l'option "Barre de défilement" ainsi que "change slider range" qui vous permettront d'intéragir facilement avec votre simulateur sans avoir à changer votre programme (le visuel auquel vous devriez pouvoir arriver est visible dans la solution de l'exercice précédent).

