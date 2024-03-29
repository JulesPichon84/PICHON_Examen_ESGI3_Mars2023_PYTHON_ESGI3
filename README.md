    _____________________________   __________          __  .__                   
    \__    ___/\______   \_____  \  \______   \___.__._/  |_|  |__   ____   ____  
      |    |    |     ___/ _(__  <   |     ___<   |  |\   __\  |  \ /  _ \ /    \ 
      |    |    |    |    /       \  |    |    \___  | |  | |   Y  (  <_> )   |  \
      |____|    |____|   /______  /  |____|    / ____| |__| |___|  /\____/|___|  /
                                \/             \/                \/            \/ 

<div align="center">

  [![Typing SVG](https://readme-typing-svg.demolab.com?font=Lato&size=30&pause=1000&color=FF8C06&background=FFFFFF00&center=true&vCenter=true&multiline=true&random=false&height=100&lines=TP2+Python;Work+smarter%2C+not+harder)](https://git.io/typing-svg)

  ![Static Badge](https://img.shields.io/badge/Version-1.0-brightgreen?style=for-the-badge&color=F907FF)![Static Badge](https://img.shields.io/badge/Python-3.11-brightgreen?style=for-the-badge&logo=Python&color=FF8C06)

  ![Static Badge](https://img.shields.io/badge/OS-Windows-blue?style=flat-square&logo=windows11) ![Static Badge](https://img.shields.io/badge/OS-Linux-blue?style=flat-square&logo=linux)
</div>

# Bienvenue dans le TP3 consacré au langage de programmation Python

## Voici l'arborescence du dossier:
    TP3
     |
     |___README.md
     |___main.py
     |___interface.py
     |___Images/
     |___Sounds/
     |___requirements.txt
     |
     |___exo/
          |
          |___pycache
          |___exo1.py
          |___exo2.py
          |___exo3.py
     

## Lors de votre arrivée dans la racine du projet, vous trouverez plusieurs fichiers et dossiers:
  1- Le fichier *main.py* représente le point d'entrée du programme, c'est par lui que tout commence.<br>
  2- Le fichier *interface.py* définit l'interface utilisateur du programme à l'aide du module Tkinter et permet d'appeler les différents exercices du TP.<br>
  3- Le fichier *requirements.txt* contient la liste des modules nécessaires pour le bon fonctionnement du programme.<br>
  4- Les dossiers *Images* et *Sound* contiennent toutes les images et les sons pour l'interface utilisateur.<br>
  5- Enfin, le dossier *exo* contient tous les exercices du TP.

Si vous souhaitez avoir un exécutable sous **Windows**, il vous suffit d'exécuter le code suivant:
  ```shell
  pyinstaller --onefile main.py
  ```

Si vous souhaitez avoir un exécutable sous **Linux**, il vous suffit d'exécuter le code suivant:
  ```shell
  pip install cx_Freeze
  ```

Créer ensuite un fichier setup.py et placez les lignes de code suivantes:
  ```python
   from cx_Freeze import setup, Executable

   setup(
        name="",
        version="",
        description="",
        executables=[Executable("main.py")])
  ```
Puis exécuter la commande suivante:
  ```shell
   python setup.py build
  ```

Volume horaire concernant le TP2:

| Tâches  | Minutes |
| ------------- | ------------- |
| Développement des Scripts Python  | 60 |
| Développement du GUI  | 15 |
| Liaison du GUI aux Scripts | 15 |
| Rédaction documentation| 5 |
| Total | 95 |

Ce qui a été fait:
- [X] Les scripts pour les 5 exercices.
- [X] Développement UI 
- [X] Création d'une documentation pour l'utilisateur.

Reste à faire:
- [ ] Réaliser les tests unitaires.
- [ ] Centrer le cadre contenant le titre et les boutons au centre de la fenêtre tkinter.
- [ ] Création d'un Dokerfile en cours mais problème au moment d'exécuté le conteneur. Non prise en charge de tkinter de façon native.
- [ ] Bonus: Ajouter une étape de sécurité avant de lancer le programme.

> [!TIP]
> Si vous souhaitez personnalisez vous mêmes les courbes, voici deux liens menant vers la documentation des modules *seaborn* et *matplotlib*:
>  - Visit https://seaborn.pydata.org/index.html
>  - Visit https://matplotlib.org/stable/tutorials/pyplot.html


> [!WARNING]
> Si vous rencontrez des problèmes avec le programme, vous pouvez m'envoyer un message !

## Amusez-vous bien avec ce TP, et surtout n'oubliez pas d'activer le son de votre ordinateur !
