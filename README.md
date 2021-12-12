# Projet-M2-Image-Harmonisation-des-couleurs

projet de Melvin BARDIN et Laurine JAFFRET


# Version testé:

python 3.7.12, python 3.6.9


# Comment installer les librairies utilisées

# Pour l'application:

pip install opencv-python
pip install pillow
pip install matplotlib
pip install PyQt5
pip install imutils


# Pour le transfert de style avec deep learning:

pip install tensorflow==2.0


# Si probleme de version entre OpenCV et Qt:

install opencv-python==4.1.1.26

# Application Principale:

Executer "Interface.py"

- Possibilité de charger et sauvegarder une image
- Choix entre les 6 harmonie de couleur
- Affichage de la palette de couleur utilisé pour l'harmonie selectionné
- Deux possibilité pour la couleur dominante:
    - choix de l'utilisateur à l'aide du cercle chromatique
    - choix automatique, l'application choisis la couleurs dominante la plus adapté.

# Scripts deepLearning de transfert de couleur:

Executer "transfertStyle.py"

