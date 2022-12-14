# OpenClassrooms: Projet 7 - Algorithme d'optimisation

## Installation:
- Commencez par installer Python.

https://www.python.org/downloads/

- Ensuite, clonez ce repository.
```
git clone https://github.com/MatBlanchard/Projet7_AlgoInvest-Trade.git
```
## Données:
Sont fournis, 3 jeux de données dans le répertoire data :
- Un jeu comportant 20 actions (dataset_1.csv)
- Deux jeux comportant 1000 actions chacun (dataset_2.csv et dataset_3.csv)

## Utilisation:
- Créez un nouvel environnement virtuel :
```
python -m venv env
```
- Activez le.
```
env\scripts\activate
```
Les 2 algorithmes n'utilisent pas de packages extérieurs à Python, il n'est donc pas nécessaire d'utiliser la commande pip.
- Pour utiliser l'algorithme de force brute utilisez la commande :
```
python bruteforce.py [chemin du fichier .csv]
```
Attention, n'utilisez l'algorithme de force brute que sur le premier dataset (dataset_1.csv). En effet, si vous l'utilisez sur l'un des dataset comportant 1000 actions, le temps de calcul sera très largement supérieur à l'âge de l'univers. C'est donc très déconseillé.
- Pour utiliser l'algorithme optimisé utilisez la commande :
```
python optimized.py [chemin du fichier .csv]
```
## Générer le rapport flake8
- Créez un nouvel environnement virtuel :
```
python -m venv env
```
- Activez le.
```
env\scripts\activate
```
- Installez les packages.
```
pip install -r requirements.txt
```
- Enfin, tapez la commande:
```
flake8 --format=html --htmldir=flake-report
```
