---
marp: true
markdown.marp.enableHtml: true 
html: true
style: |
  section.centered {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
  }
---

<style>

img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
div.answer {
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 4px;
  padding-right: 4px;
  margin-bottom: 10px;
  color: blue;
  border: thick double #32a1ce;
  font-style: italic;
  font-size: 12px;
  display: block;
}
    
.alert-success {
    color: #2c562d !important;
    background-color: #e3ede0 !important;
    border-color: #d9edf7 !important;
}
    
.alert-answer {
    color: #2c562d !important;
    background-color: #e3ede0 !important;
    border-color: #d9edf7 !important;
}

.alert-danger {
    color: #762321 !important;

    }
    
    
       
</style>



# Pratique des Machines - Intensif de rentrée 
---

Nom & Prénom : [==à compléter dans votre copie personnelle==]
N° d'étudiant⋅e : [==à compléter dans votre copie personnelle==]

[toc]

# Préambule : Comment utiliser ce fichier ?

Ce fichier est un "template" ou modèle dont vous allez créer une copie personnelle pour pouvoir le modifier et le remplir avec vos 

## 1. Créer une copie personnelle de ce fichier 

Ce fichier sert à la fois de **support de cours** et de **document de prise de notes** personnel. Le texte que vous voyez est ici mis en forme car vous le visualisez dans un navigateur qui interprète le ==langage markdown== dans lequel est écrit le fichier.


### 1.1 Créer une première note vide
:::info
**À faire :**
- dans un nouvel onglet, rendez-vous sur [https://pads.up8.edu](https://pads.up8.edu) 
- connectez-vous avec vos identifiants (les mêmes que pour talk.up8.edu)
- créez un nouveau pad en cliquant sur le bouton "Nouvelle Note". 
:::

Cette nouvelle note est vide.

### 1.2 Créer une copie de cette note "template"
:::info

- de retour sur ce template, naviguez entre les différentes icônes oeil / double fenêtre / crayon en haut à gauche pour voir les différentes ==vues== possibles : 
![](https://pads.up8.edu/uploads/1b3d69b8-8dd7-4369-87ec-49775e34373b.png)

- à partir de la vue ==Modifier== qui correspond au crayon, 
    -  faites Ctrl-a  (deux touches simultanément) pour sélectionner l'ensemble du texte, 
    -  puis Ctlr-c (deux touches simutanément) pour copier le texte.
- collez le texte dans la note que vous avez créée à l'étape 1.2 avec Ctrl-v (deux touches simultanément).
- éditez vos noms, prénoms et numéro d'étudiant⋅e en haut du fichier
- renseignez le lien vers votre copie personnelle de ce pad ici : https://lite.framacalc.org/4j2npe6aix-anh3
:::

C'est bon, vous avez maintenant votre propre copie toute propre du fichier "template".

[retour au plan](https://pads.up8.edu/QokDSHdeQFOuQufP-G0aQQ?both#Pratique-des-Machines---Intensif-de-rentr%C3%A9e-2026-2027)

## 2. Modifier et Compléter le fichier soi-même 


Vous devez indiquer vos réponses chaque fois que vous verrez ceci dans le fichier source (icône crayon) :  

```
<div class="answer">
    [réponse attendue]
</div>
```
c'est à dire ceci (2) dans le fichier interprété (icône oeil) : 

<div class="answer">
    [réponse attendue]
</div>

Vous devrez alors remplacer le texte `[réponse attendue]` par votre réponse.

**Mise en application** : Modifiez le texte ci-dessous

:::info
Quel est votre groupe (A/B/C) ?
:::

<div class="answer">
    Je suis dans le groupe X 
</div>


## 3. Comprendre ce qui est écrit 
Les gris comme celui-ci qui commencent par le caractère `$` sont des commandes que vous allez taper dans le terminal : 
```bash
$ commande
```

:warning: Le signe `$` est un caractère spécial qui indique ici la fin de l'==invite de commande==. Il ne fait pas partie de la commande en tant que telle et ne devra pas être recopié.

---
<!-- _class: centered -->

Début du cours !

---

# 1. Généralités 

## 1.1 Système d'exploitation de type ==Unix== 

Au cours de votre formation et de votre pratique de l'informatique, vous allez travailler le plus fréquemment sur des machines dont le système d'exploitation est de type **Unix**.

![](https://pads.up8.edu/uploads/0f6c8072-bdd8-4be6-b97d-79b8530ef128.png)


MacOS, comme les **distributions Linux** présentées ci-dessus sont des systèmes Unix.

Pour connaître le système d'exploitation de la machine sur laquelle vous travaillez, rendez-vous dans la section "À propos" (ou équivalent) de votre gestionnaire de paramètres.

:::info
Quel est le système d'exploitation sur lequel vous vous trouvez ?
:::

<div class="answer">
Ubuntu 22.04.5 LTS
</div>

## 1.2 Système de fichiers 

Le **système de fichiers** (*file system*) est l'organisation hiérarchique des fichiers au sein du système d'exploitation : il est composé de ce que nous appelons des **répertoires** (les dossiers) et des **fichiers**.

L'arborescence contient TOUS les fichiers contenus dans une machine donnée, et peut contenir des fichiers appartenant à des périphériques externes lorsqu'ils sont branchés à la machine.

:::info
Donnez différents types de fichiers.
:::

<div class="answer">

- texte (.txt ; .py ; .sh ; .md ; .csv ; .html ; .css ; .php)
  
- pdf (.pdf)
    
- binaire (.exe - Windows)

- sons (.wav)

- images, videos (.jpg ; .png ; .bmp ; .gif ; .mp3 ; .mp4)

- images de disque (.img pour les backups)

- archives (.zip ; .rar ; .7z ; .tgz)
    
- docx ; xls 


</div>

Ceux-ci sont organisés sous forme d'arborescence (comme un arbre), comme illustré sur la Figure 1. 

note : du point de vue du système, *Everything is a file*, c'est à dire que tout est un fichier (Voir [la réponse à la question "What are directories, if everything on Linux is a file?"](https://askubuntu.com/questions/1073802/what-are-directories-if-everything-on-linux-is-a-file) pour plus de détails.). C'est pourquoi dans la suite de ce cours et dans la documentation des commandes, `[FILE]` pourra désigner un fichier ou un répertoire.

![](https://pads.up8.edu/uploads/b06ef894-74fa-4498-9bf7-0af066b72d73.png)



La **racine du système** est le dossier qui contient tous les autres dossiers.

## 1.3 Trouver son chemin dans l'arborescence de fichier 

### 1.3.1 Le chemin absolu
Chaque répertoire et chaque fichier est identifié dans le système de fichiers par un **chemin absolu** unique. Ce chemin est une chaîne de caractère qui contient les noms des répertoires qu'il faut traverser depuis la **racine du système** pour atteindre sa destination. Les noms des dossiers sont séparés par des "**/**". Le symbole utilisé pour la racine du système étant lui même "**/**", un chemin absolu commence toujours par ce caractère.

On dit qu'un répertoire qui contient un autre répertoire est son répertoire `parent`.

:::success
**Exemple** : 
- `home` est le répertoire parent des répertoires `aron`, `lydia`, `carlos`.
- le chemin absolu du répertoire `home` de la Figure 1 est `/home` 
- le chemin absolu du répertoire `homework` de la Figure 1 est `/mnt/zip/homework`
:::

:::info
Quels sont les chemins absolus des dossiers `carlos` et `modules` ?
:::

<div class="answer">

- /home/carlos

- /usr/X1R6/lib/modules

</div>

 
### 1.3.2 Les chemins relatifs

Pour désigner l'emplacement d'un fichier (ou dossier), on peut également utiliser une infinité de **chemins relatifs** : ce sont tous les chemins permettant de l'atteindre qui ne démarrent pas à la racine, c'est à dire qui partent d'ailleurs dans l'arborescence. 

Voici une autre manière de représenter la structure arborescente du système de fichier, avec la racine en haut. On voit que celle-ci est toujours identifiée par le caractère "/".


![](https://pads.up8.edu/uploads/d8fce373-6695-42dc-abcf-9505a3a71a61.png)

Pour trouver son chemin dans l'arborescence, on peut soit :  
- rentrer dans un dossier pour le traverser et s'enfoncer dans l'arborescence, et on utilise pour cela le nom du dossier suivi du caractère "==/==" comme vu précedemment
- remonter dans le dossier parent et se rapprocher de la racine. Le répertoire parent est alors désigné par les caractères "==**.\.**==".

:::success
**Exemple :**
- le chemin absolu du dossier `documents` est : `/home/elsa/documents`.
- le chemin **relatif** de la racine *depuis* le dossier `documents` est : 
`../../../`
    - le premier `..` permet de remonter dans le dossier `elsa`
    - le second `..` permet de remonter dans le dossier `home`
    - le troisième `..` permet de remonter dans le dossier `/`
:::

:::danger
:warning: On aurait pu croire que le chemin pour "remonter vers la racine depuis `documents`" serait `documents/elsa/home/`, mais **ce n'est pas le cas** : quand on indique le nom d'un dossier c'est pour s'enfoncer dans l'arborescence, dès qu'on "remonte", alors le dossier est `..`.
:::

:::success
**Remarque** : un chemin vers un fichier se termine par le nom du fichier avec son extension 
**Exemple** : un chemin relatif vers `photo_1.jpg` depuis le dossier `cpu` est : `../../home/max/images/photo_vac/photo_1.jpg`
:::

:::info
Donner un chemin relatif du fichier `rapport.odt` depuis le dossier `grub`.
:::

<div class="answer">
    [réponse attendue]
</div>


## 1.3.3 Répertoires remarquables


- 💼 **répertoire de travail** :  On a parfois besoin de désigner le répertoire courant, ou répertoire de travail, dans ce cas on utilise le symbole "**==.==**" (point). 
- 🏠 **répertoire "home"** : vous avez dû remarquer un dossier s'appelant `home` dans les arborescences ci-dessus. Ce dossier contient tous les **dossiers personnels** des **users** d'une machine donnée. Ces dossiers ont pour nom le nom du **user** lui-même (voir ci-dessus les dossiers `max` et `elsa`).
:warning: le dossier qu'on désignera comme *votre* "home" est le dossier qui a le nom de votre login. C'est le dossier qui s'ouvre par défaut quand vous ouvrez ==l'explorateur de fichiers==.

:::info
Vérifiez que l'explorateur de fichiers s'ouvre bien dans votre `home`. Généralement en faisant un clic droit dans un espace blanc du dossier vous pouvez afficher les `propriétés` de ce dossier.
Le "dossier parent" de votre home est il affiché dans les propriétés ? Si oui quel est-il ?
:::

<div class="answer">
    [réponse attendue]
</div>

Votre "home" est un dossier important car c'est celui dans lequel vous allez ranger tous vos fichiers personnels. Nous explorerons un peu les autres dossiers (par exemple le dossier `bin`), mais la majorité de votre travail se déroulera dans votre home ou dans un de ses sous-dossiers.

# 2. Découverte du terminal et de quelques commandes usuelles

## 2.1 Le terminal

Un **==terminal==** (ou émulateur de terminal, ou console) est un logiciel qui sert de point d’accès de communication entre l’humain et la machine. On l'appelle terminal dans le même sens qu'un terminal d'aéroport, car c'est par là qu'on transite. 

Le plus souvent, on entend par terminal une interface graphique (c'est à dire une "fenêtre") dans laquelle est lancé un programme particulier qui s'appelle un ==**shell**==. 
Ce programme : 
1. lit les commandes que vous allez inscrire dans le terminal,
2. ==**interprète**== ces commandes, et exécuter ce qu'il faut.
 
On appelle donc le shell un ==**interpréteur de commande**==. Notez que parfois, l'exécution se traduit par un affichage dans le terminal, parfois non. 

On "lance" le terminal en cliquant sur une icône qui ressemble généralement à ceci :
![](https://pads.up8.edu/uploads/acb84a18-9c82-4df6-b457-01ca0a806920.png)

:::info
Ouvrez le terminal sur votre machine.
:::

Doit s'ouvrir une fenêtre qui ressemble à ceci : 


![](https://pads.up8.edu/uploads/0c6ae804-edea-46fc-b5fe-6c8c96e14dfa.png)

Un **shell** est un *interpréteur de commande*. Il en existe plusieurs, comme nous allons le voir dans ce TP.
Les **commandes** saisies au clavier sont interprétées par le shell lorsqu'on tape "entrée".


## 2.2 L'invite de commande

Par défaut, l'**invite de commande** (qui comme son nom l'indique vous invite à lui fournir une commande) est composée de votre **login**, puis d'un **@**, puis du **nom de la machine** sur laquelle vous êtes connecté.e, puis d'un **`:`**, puis du **répertoire de travail**, et enfin d'un **$** qui signifie que vous pouvez entrer une commande.

:::info 
Quelle est l'invite de commande qui s'affiche dans votre terminal par défaut ?
::: 
<div class="answer">
    [réponse attendue]
</div>


Par défaut encore, le répertoire de travail correspond à votre **répertoire personnel**, ou « *home directory* », qui est la racine de la partie du système de fichier *qui appartient à votre compte*. 

Le symbole tilde `~` (altgr-2) que vous voyez correspond à un alias (raccourci) du chemin absolu de votre répertoire de travail.


## 2.3 Premières commandes 

Une **ligne de commande** est composée d'une **commande**, d'éventuelles **options** (précédées du caractère "**-**" et d'éventuels **arguments**) : 

```
$ commande -option1 -option2 -option3 argument1 argument2`
```

- tout ce qui commence par un tiret est une option
- tout ce qui ne commence pas par un tiret est un argument 

Chaque commande a un fonctionnement qui lui est propre : toutes les commandes n'attendent pas d'arguments, mais certaines ont des arguments obligatoires, tout dépend de ce que la commande est censée faire.

:::danger
:warning: Attention ! Le shell est sensible à la casse et aux espacements, donc si vous ajoutez des espaces aux mauvais endroits (par exemple entre le caractère `-` et une option OU que vous ne placez pas bien un espace (par exemple si vous l'oubliez entre deux options), le comportement que vous obtiendrez ne sera pas celui que vous attendiez ! :warning: 
:::

:::info
Tapez la commande suivante : 
```
$ date
```
Ici, on a une commande utilisée sans option et sans arguments. Qu'obtenez-vous ? 
:::

<div class="answer">
    [réponse attendue]
</div>

:::info

Même question pour la commande suivante, à laquelle on a ajouté une **option** à la commande `date` :
```
$ date -u
```
:::
<div class="answer">
    [réponse attendue]
</div>

:::info

Même question pour la commande suivante ; ici, la commande n'a pas d'option mais a un argument :
```!
$ echo "Bonjour $USERNAME, ton home correspond au dossier $HOME, et ton interpréteur de commande est $SHELL"
```
On remarque ici que l'argument est une ==chaîne de caractères== entourée par des guillemets. Dans ce cas, les espaces à l'intérieur de la chaîne ne constituent évidemment pas des séparateurs d'arguments. La chaîne de caractère correspond à 1 argument.
:::
<div class="answer">
    [réponse attendue]
</div>

:::info
J'ai dit plus haut que "~" correspondait à votre "home", vérifiez que c'est vrai en tapant la commande suivante : 
```
$ echo ~
```
qu'obtenez-vous ?
:::
 
<div class="answer">
    [réponse attendue]
</div>


# 3. Commandes `cd`, `pwd`, `ls`, `mkdir`, `rm`, `touch`

Nous avons tout à l'heure ouvert l'explorateur de fichiers. Gardez-le ouvert et naviguez à la souris pour pouvoir visualiser dans l'interface les modifications opérées depuis le terminal. Bientôt, vous n'utiliserez plus l'explorateur de fichiers car tout passera par le terminal (c'est beaucoup plus rapide !), mais pour une première fois, c'est utile d'avoir les deux ;).

## 3.1 Se déplacer dans la hiérarchie des fichiers via le terminal

### 3.1.1 `cd`
:::success
Commande `cd`, pour **c**hange **d**irectory. Cette commande prend un argument, qui est un chemin vers un répertoire de destination, et déplace le **répertoire de travail** vers cette destination. C'est l'équivalent de double cliquer sur des dossiers lorsque vous êtes dans l'explorateur de fichiers.
:::

Usage :
```
`$ cd <chemin vers un répertoire>` 
```


:::info
Exécutez ces commandes dans le terminal les unes après les autres et observez les changements de votre **prompt**:

```bash
cd ..
cd ~
cd Documents
cd 
```
Comment votre "prompt" évolue-t-il ? Quel est le répertoire de travail une fois que vous avez exécuté la dernière commande ?
:::


<div class="answer">
    [réponse attendue]
</div>


Vous devriez avoir constaté que pour la commande `cd` l'argument est optionnel : si vous exécutez "`cd`" seul, vous vous déplacez dans votre "home", c'est une sorte de raccourci.


### 3.1.2 Savoir "où" vous êtes avec `pwd`

Quand on se pose la question "Où suis-je ?" dans le terminal, on cherche à connaître le **répertoire** de travail, dans lequel votre invite de commande est située. Votre localisation influe naturellement sur le chemin vous permettant d'accéder à un fichier contenu dans votre hiérarchie de fichiers.

Découvrons la commande `pwd`. Normalement, suite aux dernières commandes que vous avez exécutées vous devriez être revenu.e dans votre *home*. Si ce n'est pas le cas, exécutez une des commandes permettant de situer votre prompt dans votre *home*.


Usage :

```bash
$ pwd
```
:::info
Exécutez ces commandes dans le terminal les unes après les autres et observez le résultat :
```
pwd
cd ..
pwd
cd ~
pwd
cd Documents
pwd
```

Quel est le résultat affiché par pwd après chaque commande ? Que remarquez-vous ?
:::
<div class="answer">
    [réponse attendue]
</div>

Vous devriez avoir constaté que la commande `pwd` n'a pas besoin d'argument : elle affiche simplement le **chemin absolu du répertoire de travail courant**. Contrairement à `cd`, elle ne modifie pas le répertoire de travail.


## 3.2 Intéragir avec le contenu d'un répertoire depuis le terminal 

### 3.2.1 Voir ce qui se trouve dans un répertoire avec `ls`

:::info
Commande `ls`, pour **l**i**s**t. Cette commande permet d'afficher le contenu d'un répertoire : elle liste les fichiers et les répertoires qui se trouvent dans le répertoire de travail courant = répertoire de travail.
:::

Usage :

```bash
$ ls
```


:::info
Exécutez ces commandes dans le terminal les unes après les autres et observez les résultats :

```
$ pwd
$ ls
$ cd ..
$ ls
$ cd ~
$ ls
$ cd Documents
$ ls
```

Que contient le résultat de la commande ls ? Le résultat est-il le même dans tous les répertoires ?
:::

<div class="answer">
    [réponse attendue]
</div>

Vous devriez avoir constaté que la commande `ls` affiche les **fichiers et répertoires présents dans le répertoire courant**. Le résultat dépend donc du répertoire dans lequel vous vous trouvez.


Il est également possible de préciser le répertoire dont on souhaite afficher le contenu :

```bash
$ ls <chemin vers un répertoire>
```

:::info
Qu'obtenez-vous en tapant les commandes suivantes ?

```bash
ls ~
ls Documents
ls ..
```
:::

<div class="answer">
    [réponse attendue]
</div>


La commande `ls` accepte également plusieurs options permettant de modifier la manière dont les informations sont affichées. Par exemple, l'option -l permet d'obtenir une liste détaillée :

``` 
$ ls -l
``` 

Essayez également :

```
$ ls -a
$ ls -la
``` 
:::info
Que remarquez-vous ? Quels fichiers supplémentaires apparaissent avec ls -a ?
:::

<div class="answer"> [réponse attendue] </div>

Vous devriez avoir constaté que l'option -a permet d'afficher tous les fichiers, y compris les fichiers cachés (dont le nom commence généralement par .). L'option -l affiche quant à elle davantage d'informations sur chaque élément, comme ses permissions, son propriétaire, sa taille et sa date de modification.


### 3.2.2 Créer un répertoire avec `mkdir`

Usage :

```bash
$ mkdir <nom_de_répertoire>
```
:::danger
:warning: Attention ! le nom de votre répertoire **ne peut pas contenir d'espace** ! si vous tapez la commande : 
```bash
$ mkdir pratique des machines
```
chaque élément séparé des autres par une espace sera interprété comme un nouvel argument. Résultat : 3 dossiers seront créés ! Le dossier `pratique` le dossier `des`, le dossier `machines`
:::


:::info
Quelle est la commande a exécuter pour créer un dossier contenant tous les fichiers du cours de "Pratique des machines" ?
:::


<div class="answer">
    [réponse attendue]
</div>

:::info
Exécutez les commandes suivantes et observez les effets sur votre prompt.

```bash
$ cd ~
$ mkdir Cours
$ ls
$ ls Cours
$ mkdir Cours/pdm
$ ls Cours/pdm
$ cd Cours/pdm
$ pwd
$ ls
```
:::

Vous devriez avoir constaté que `mkdir` permet de **créer un nouveau répertoire**, mais que la commande ne vous déplace pas automatiquement dans ce répertoire. Après avoir exécuté `mkdir pdm`, le répertoire `pdm` apparaît dans le résultat de `ls`, mais votre répertoire de travail reste inchangé.

### 3.2.3 Créer un fichier avec `touch`

La commande `touch` permet notamment de **créer un nouveau fichier vide**. Elle prend en argument le nom ou le chemin du fichier à créer.

Usage :

```bash
$ touch <nom_du_fichier>
```
:::danger
Même remarque que plus haut : ne mettez pas d'espaces dans vos noms de fichier au risque d'avoir de mauvaises surprises ! Utilisez les caractères "`-`" ou "`_`" pour séparer les mots si vous le souhaitez.
:::

:::info
Essayez les commandes suivantes :

```bash
pwd
ls
touch fichier.txt
ls
```

Que s'est-il passé après l'exécution de `touch fichier.txt` ?
:::

<div class="answer">
    [réponse attendue]
</div>

Vous devriez avoir constaté qu'un nouveau fichier appelé `fichier.txt` a été créé dans le **répertoire de travail courant**.

Vous pouvez également créer plusieurs fichiers avec une seule commande :

```bash
touch fichier1.txt fichier2.txt fichier3.txt
```

Les trois fichiers seront alors créés dans le répertoire courant.

Si le fichier indiqué existe déjà, `touch` ne crée pas de nouveau fichier. Il met notamment à jour sa **date de dernière modification**, comme nous le reverrons plus tard.


### 3.2.4 Supprimer des éléments avec `rm`

Usage :

```bash
$ rm <nom du fichier>
```

:::info
Nous allons commencer par créer quelques dossiers et fichiers pour pouvoir les supprimer. Exécutez les commandes suivantes en suivant ce qui se passe dans l'explorateur de fichiers :

```
cd ~/Documents
mkdir test_rm
cd test_rm
touch fichier1.txt
touch fichier2.txt
ls
rm fichier1.txt
ls
```

Quel fichier a disparu après l'exécution de rm fichier1.txt ? Que devient fichier2.txt ?
:::

<div class="answer">
    [réponse attendue]
</div>

Vous devriez avoir constaté que `rm` permet de **supprimer un fichier**. Après l'exécution de `rm fichier1.txt`, celui-ci n'apparaît plus dans le résultat de `ls`, tandis que `fichier2.txt` est toujours présent.

Pour supprimer un répertoire vide, on peut utiliser l'option `-d` :

```bash
rm -d <nom du répertoire>
```

Par exemple :

```bash
mkdir dossier
rm -d dossier
```

Pour supprimer un répertoire **et son contenu**, on utilise généralement l'option `-r` :

```bash
rm -r <nom du répertoire>
```

:::info
utilisez la commande `rm` pour faire le ménage dans votre répertoire home : si vous avez créé des fichiers et des dossiers au cours de ce TP, supprimez-les.
:::


# 4. Messages d'erreur courants !

Lorsque vous utilisez une commande dans le terminal, il est possible que celle-ci ne fonctionne pas. Dans ce cas, le terminal affiche généralement un :ghost: **message d'erreur** :ghost:

Ces messages permettent de comprendre **pourquoi la commande n'a pas pu être exécutée**. Il est donc important de prendre l'habitude de les lire plutôt que de simplement constater que "ça ne marche pas".

Il est préférable d'avoir un message d'erreur, qui indique que l'action demandée n'a pas eu lieu, plutôt que de ne pas avoir de message d'erreur mais un comportement inattendu (voir l'exemple de la création de 3 dossiers au lieu d'un seul en raison de l'utilisation d'espaces).

## 4.1 Erreurs avec `cd`

Essayez les commandes suivantes :

```bash
cd toto
cd /chemin/qui/nexiste/pas
cd fichier.txt
```

Observez les messages affichés par le terminal. Que vous indiquent-ils ?

<div class="answer">
    [réponse attendue]
</div>

Lorsque le répertoire demandé n'existe pas, vous obtenez généralement un message similaire à :

```text
bash: cd: toto: No such file or directory
```

Le message **No such file or directory** signifie que le chemin indiqué ne correspond à aucun fichier ou répertoire existant.

Si le chemin correspond à un fichier et non à un répertoire, vous pouvez obtenir un message similaire à :

```text
bash: cd: fichier.txt: Not a directory
```

Le message **Not a directory** signifie que l'élément existe, mais qu'il ne s'agit pas d'un répertoire. La commande `cd` ne peut donc pas être utilisée dessus.

Lorsque vous obtenez une erreur avec `cd`, vérifiez notamment :

* l'orthographe du nom du répertoire ;
* les majuscules et minuscules ;
* que le chemin est correct ;
* que l'élément existe bien ;
* que l'élément est un répertoire et non un fichier.

## 4.2 Erreurs avec `ls`

Essayez les commandes suivantes :

```bash
ls toto
ls /chemin/qui/nexiste/pas
```

Observez les messages affichés par le terminal. Que vous indiquent-ils ?

<div class="answer">
    [réponse attendue]
</div>

Lorsque le fichier ou le répertoire demandé n'existe pas, vous obtenez généralement un message similaire à :

```text
ls: cannot access 'toto': No such file or directory
```

Le message **No such file or directory** indique, là encore, que le chemin fourni ne correspond à aucun élément existant.

Contrairement à `cd`, `ls` peut également être utilisé directement sur un fichier :

```bash
ls fichier.txt
```

Dans ce cas, `ls` indique simplement que le fichier existe, sans afficher son contenu.

Une erreur avec `ls` ne signifie donc pas nécessairement que `ls` est incorrect. Le problème vient souvent du **chemin fourni en argument**.

## 4.3  Erreurs avec `mkdir`

Essayez les commandes suivantes :

```bash
mkdir test
mkdir test
mkdir /chemin/qui/nexiste/pas/test
```

Observez les messages affichés par le terminal. Que vous indiquent-ils ?

<div class="answer">
    [réponse attendue]
</div>

Si vous essayez de créer un répertoire qui existe déjà, vous obtenez généralement :

```text
mkdir: cannot create directory 'test': File exists
```

Le message **File exists** signifie que l'élément `test` existe déjà. `mkdir` ne peut donc pas créer un nouveau répertoire portant exactement le même nom au même endroit.

Si le répertoire parent n'existe pas, vous pouvez obtenir :

```text
mkdir: cannot create directory '/chemin/qui/nexiste/pas/test': No such file or directory
```

Le message **No such file or directory** indique que le chemin demandé n'existe pas.

Lorsque vous obtenez une erreur avec `mkdir`, vérifiez notamment :

* que le nom du répertoire n'est pas déjà utilisé ;
* que le chemin indiqué existe ;
* que vous avez les droits nécessaires pour créer le répertoire à cet emplacement.

:::info
**Récapitulatif** :

| Message                     | Signification                                                      |
| --------------------------- | ------------------------------------------------------------------ |
| `No such file or directory` | Le fichier ou répertoire indiqué n'existe pas.                     |
| `Not a directory`           | L'élément existe, mais ce n'est pas un répertoire.                 |
| `File exists`               | Un élément portant ce nom existe déjà.                             |
| `Permission denied`         | Vous n'avez pas les droits nécessaires pour effectuer l'opération. |

Prenez donc l'habitude de **lire le message d'erreur** : il contient souvent directement l'information nécessaire pour corriger votre commande.
:::

## 4.4 :bulb: Éviter les erreurs en utilisant la touche magique de votre clavier  `↹`

Vous disposez sur votre clavier d'une touche utilisée constamment lorsqu'on travaille dans le terminal : la touche **tabulation**.


La touche **Tabulation** ( ` ↹ `) est très utile dans le terminal pour **compléter automatiquement** les noms de fichiers, de répertoires et de commandes. Commencez à taper les premières lettres d'un nom, puis appuyez sur `↹` : le terminal complète automatiquement le nom lorsqu'il n'y a pas d'ambiguïté. Si plusieurs possibilités existent, appuyez une seconde fois sur `↹` pour les afficher.

Par exemple, si le répertoire courant contient un répertoire `Documents`, vous pouvez taper :

```bash
cd Doc
```

puis appuyer sur `↹`. Le terminal complétera automatiquement :

```bash
cd Documents/
```

La touche `↹` permet donc de 
- gagner du temps
- d'**éviter les erreurs de frappe** dans les noms de fichiers et de répertoires.

Prenez l'habitude de l'utiliser dès que possible, cela deviendra rapidement un réflexe qui vous évitera bien des erreurs.


# 5. Manier le terminal


Quelques astuces et raccourcis clavier pour utiliser le terminal :

- `Ctrl + Maj + t` : ouvrir un nouvel onglet dans le terminal
- `Ctrl + d` : arrêter le processus en cours ou fermer le terminal (ex : lancez la commande `cat` puis arrêtez le processus)
- la tabulation permet d'auto-compléter
- flèches du haut / bas : se déplacer dans l’**historique** des commandes lancées
- `Ctrl + a` : aller au début de la ligne
- `Ctrl + e` : aller à la fin de la ligne
- `Ctrl + k` : couper jusqu’à la fin de la ligne
- `Ctrl + Maj + C` : clic droit “copier” : copier la région en surbrillance
- `Ctrl + Maj + V` : clic droit “coller” ou clic molette ou `Ctrl + y` (seulement au sein du terminal) : coller
- `Ctrl + c` : arrêter la commande en cours
- `clear` ou `Ctrl + l` : effacer les commandes précédentes de l’interface graphique
- `reset` : réinitialiser l’environnement du shell
- `↹` : complétion de commande
- Sur un Linux, une autre manière d'ouvrir le terminal est de faire `ctrl+alt+t` au clavier (cela est valide depuis une machine où ces touches clavier existent, pour les machines Apple je vous laisse chercher vous-même).


# Rappels sur le nommage des fichiers & dossiers
:::danger
> **⚠️ Nommage des fichiers et dossiers**
- **n'utilisez pas d'espaces dans vos nom de répertoires ou de fichiers** 
- n'utilisez pas de caractères spéciaux ou de ponctuation. Vous n'avez droit qu'aux caractères de a à z, aux chiffres et à "-" et "_" 
- donnez toujours une **extension** aux fichiers que vous créez. Les dossiers, eux, n'ont pas d'extension 



