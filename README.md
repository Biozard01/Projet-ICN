> ## [Lien Vidéo](https://drive.google.com/uc?id=1uXVelz9Dwp40X9tER7hXdVI6R9gb3Nhp)

### Synopsis Du Projet
___
Notre projet est un jeu vidéo de type Rogue-Like.

*Le Rogue-Like est un genre de jeux vidéo dont le gameplay est inspiré de Rogue (jeu de 1980 sorti sur UNIX, une famille de systèmes d’exploitation multitâche). 
Traditionnellement, le joueur y explore au tour par tour un ou plusieurs souterrains générés aléatoirement. Nous nous sommes servis du jeu The Binding of Isaac comme support de comparaison.*

Le but du jeu est de survivire aux hordes d'ennemis pour pouvoir gagner la partie.

Pour ce faire, le héros (vous) doit utilisé le pouvoirs des céreales pour éliminer ses assaillant.

Ce jeu à aussi une connection avec la vrai vie. 

En effet, avant de commencer à joué, vous avez deux information a donné : un compte Tweeter et une difficulté.

Le compte Tweeter choisi va permettre aux jeu de choisir l’environnement du jeu (apparence des ennemies, fond de carte et nombres de créatures) grâce aux nombres de tweets du compte.


### Génèse Du Projet
___
Pour réaliser ce projet, nous avons donc utilisé certains sites tel que [Arcade Academy](http://arcade.academy/examples/index.html) pour trouver des idées, des aides de conception graphique, des méchanismes de jeu et des bouts de code.

A partir de cela, nous avons procédé par éliminations afin de choisir les sprites qui nous plaisaient, les fonds de salles et apparences.

Lors de notre première séance, nous avons réfléchis à l'orientation de notre jeu. Un système poussé avec de nombreuses salles, couloirs, boss et différentes classes. Très vite, nous avons compris que cela s'avérait trop complexe pour notre niveau actuel avec le temps que nous avions.

Nous nous sommes donc orienté vers un système plus simple et fluide.

Nous avons donc commencé a codé, en utilisant comme squelette différents exemple de code.

### Développement Du Jeu
___
Tout d'abord, nous avons commencé par la gestion des déplacements du joueur.

Pour cela, nous avons fait se déplacer un rectangle dans une fenêtre sans qu'il n'en sorte, en utilisant les flèches directionel du clavier.

A partir de la 3ème séance, c'est la que le jeu commence vraiment à ressembler à un jeu. 

Premièrement, c'est la première apparition des ennemis, il sont immobile mais tire sur le joueur selon c'est coordonnée en X et Y, à se stade là du développement, le joueur est encore invincible, c'est à dire qu'il ne peut pas perdre même si il est touché.

Deuxièmement, le rectangle a été remplacé par un sprite. Maintenant, en plus de pouvoir se déplacer, le joueur peut aussi tirer en visant avec la souris et en utilisant clique droit/gauche, quand il elimine des ennemis, un score en bas de la fenêtre augemente de 1.

Pendant la 4ème séance, nous avons rajouté un écran de début et de game over. Nous avons aussi, comme a chaque séance, fait des ajustement mineur et des simplification au niveau du code.

Lors de la 5ème séance, c'est l'arriver des céreales en tant que projectile du joueur.

Au fur et a mesure des séance suivantes d'autre nouveauté arrive, d'abord un écran en cas de victoire, puis le début des essais sur tweepy, la librairie python qui permet d'utiliser des fonctionnalité de Tweeter, l'ajout puis la suppression d'un boss qui rendait le jeu trop dur.


\pagebreak

<img src='https://drive.google.com/uc?id=1ULhP4z23JPrbuNZpZYj5kH3qzzxbEPY4' style='position:absolute; top:200px; left:-1000px; width:1600px;'>

<img src='https://drive.google.com/uc?id=1ULhP4z23JPrbuNZpZYj5kH3qzzxbEPY4' style='position:absolute; top:0px; left:0px; width:1500px;'>
