## Raquette

![Interface](introScratch/2_raquette/raquette.gif)

!!! note ""
	**Figure 2:** Objectif final: La raquette suit la souris.

Dans le casse briques, 3 acteurs sont sur la scène: la raquette, la balle et les briques. Voyons d'abord comment programmer la raquette puisqu'elle nous permettra de réinvestir ce que nous venons de voir au sujet de l'interface, tout en commençant avec un programme simple. 

!!! note "Exercice 3"
	Modifiez le fond d'écran comme bon vous semble et définissez le programme de la raquette pour qu'elle suive la souris horizontalement. Pour cela vous aurez besoin d'un événement déclencheur (le drapeau), d'un bloc *contrôle* et d'un bloc *mouvement*.

??? note "Solution exercice 3"
    ![ProgrammeRaquette](introScratch/2_raquette/progRaquette.png)
    Ici, *y* qui correspond à la position verticale de notre sprite. Comme 0 correspond au milieu de la scène et -180 au bas, on fixe y à -160. 

Ce premier exercice nous permet de découvrir 3 éléments essentiels en programmation:

- les **instructions**: les programmes sont constitués de séquences d'instructions. Chacune correspond à une action que l'ordinateur doit réaliser. Ici nous avonns utilisé l'instruction "aller à x:... y:..." qui nous permet de déplacer notre sprite à la position que nous souhaitons.
- les **événements**: De nombreux langages de programmation sont dits séquentiels: ils suivent une séquence d'instructions de manière chronologique. D'autres comme scratch sont événementiels: les instructions sont exécutées en fonction d'événements déclencheurs. En scratch on pourra ainsi facilement écrire un programme qui fera deux choses en même temps (du moins nous donner cette impression) quand le drapeau sera cliqué. Pour cela il suffira d'écrire deux sous-programmes commençant par l'événement drapeau.
- les **boucles**: pour programmer la raquette afin qu'elle aille à la position de la souris, puis qu'elle aille à la position de la souris, puis qu'elle aille à la position de la souris... nous aurions pu dupliquer le bloc mouvement et le coller un infinité de fois à la suite de mon événement. Cela  nous aurait demandé de cliquer... une infinité de fois. Heureusement les boucles permettent de faire cela pour nous et nous permettent de nous faciliter la vie, d'éviter les répétitions superflues et de rendre notre programme plus lisible.













