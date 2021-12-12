# Projet-M2-Image-Harmonisation-des-couleurs
projet de Melvin BARDIN et Laurine JAFFRET


# version testé:
python 3.7.12, python 3.6.9


#comment installer les librairies utilisées
#pour l'application:
pip install opencv-python
pip install pillow
pip install matplotlib
pip install PyQt5
pip install imutils


#pour le transfert de style avec deep learning:
pip install tensorflow==2.0


#si probleme de version entre OpenCV et Qt:
install opencv-python==4.1.1.26

#Application Principale:
- Possibilité de charger et sauvegarder une image
- Choix entre les 6 harmonie de couleur
- Affichage de la palette de couleur utilisé pour l'harmonie selectionné
- Deux possibilité pour la couleur dominante:
        - choix de l'utilisateur à l'aide du cercle chromatique
        - choix automatique, l'application choisis la couleurs dominante la plus adapté.

