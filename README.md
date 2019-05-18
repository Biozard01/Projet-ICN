<style>
/* background image*/
 .phb{ background : white;} 
/* Text */
 .phb { font-family: Cambria; font-size: 10,8pt}
 .phb h1+p::first-letter {float:none;font-family:Cambria;font-size:9.84pt;color:#000;line-height:1.3em;font-weight:normal;}
 .phb h4, .phb h3, .phb h2, .phb h1{font-family: Cambria;color: #000;font-weight: normal;}
 .phb h1{font-size:30pt;}
 .phb h2{font-size:21,84pt;}
 .phb h3{font-size:18pt; border-bottom:1pt solid #000}
 .phb h4{font-size:14,88pt;}
 .phb h5{font-family: Calibri;color:#000;font-size: 12pt;font-weight: normal;}
/* Tables */
 .phb table{font-family: Calibri;font-size: 9.84pt;}
 .phb table tbody tr:nth-child(odd){background-color:#f2f2f2;}/*change backing of rows*/
/* Class Table */  
 .phb .classTable{border-image-source: none;border: none;}
 .phb .classTable h5{font-family: Calibri;font-weight: bold;}
 .phb .classTable table tbody tr:nth-child(odd){background-color:#FFF;}
/* Description block */
 .phb .descriptive { padding-left:3px;background-color: #e6e6e6;border-image: none;border: none;font-family: Calibri;}
 .phb .descriptive p{font-size:9.84pt;}
 .phb .descriptive em{font-family:Calibri;}
 .phb .descriptive strong{font-family: Calibri;}
/* Note */
 .phb blockquote{font-family: Calibri;font-size:
 9.84pt;background-color:#e6e6e6;border-width:5px;border-image-outset:5px 0px; box-shadow:0px 1px 5px;}/* Stat Block */
 .phb hr+section blockquote{background: white;border: 3px solid #e6e6e6;box-shadow: none;}
 .phb hr+section blockquote h3{font-family:Calibri;border-bottom:1px solid #000;}
 .phb hr+section blockquote hr+ul{color: #000;}
 .phb hr+section blockquote table{color: #000;}
 .phb hr+section blockquote hr{background-image: url(https://gmbinder.com/images/MS0gM8Z.png)}
/* footer */
 .phb:after{display:none;} 
 .phb .pageNumber{color:#000;font-size:9.84pt;bottom:14mm;right:1.7cm}
 .phb .footnote{color:#000;font-size:9.84pt;bottom:14mm;left:1.7cm;text-align:left;width:600px;}
 .phb:nth-child(even) .pageNumber{left:18.19cm;}
 .phb:nth-child(even) .footnote{left:1.7cm;}
 .phb a{color:black;}
</style>

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
