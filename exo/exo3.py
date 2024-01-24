# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *

#---Définition classes principales-----------
class Materiel:
    def __init__(self, root, type_support, identifiant):
        self.root = root
        self.type_support = type_support
        self.identifiant = identifiant


class Clavier(Materiel):
    def __init__(self, root, type_support, identifiant, nombre_touches):
        super().__init__(root, type_support, identifiant)
        self.nombre_touches = nombre_touches


class Ecran(Materiel):
    def __init__(self, root, type_support, identifiant, taille_ecran):
        super().__init__(root, type_support, identifiant)
        self.taille_ecran = taille_ecran


class PC(Materiel):
    def __init__(self, root, type_support, identifiant, clavier, ecran):
        super().__init__(root, type_support, identifiant)
        self.clavier = clavier
        self.ecran = ecran

    # Fonction permettant d'enregistrer les données dans un fichier passé en paramètre par l'utilisateur.
    def sauvegarder_configuration(self, fichier):
        with open(fichier, 'w') as f:
            f.write(f"Type de support: {self.type_support}\n")
            f.write(f"Identifiant: {self.identifiant}\n")
            f.write(f"Clavier - Nombre de touches: {self.clavier.nombre_touches}\n")
            f.write(f"Ecran - Taille: {self.ecran.taille_ecran}\n")

    # Fonction permettant de lire les données dans un fichier sauvegarder par l'utilisateur.
    def relire_configuration(self, fichier):
        with open(fichier, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())

def afficher_liste(self, type_support, identifiant, nombre_touches, taille_ecran, result_text):
    # Création d'une instance de la classe Clavier
    clavier_instance = Clavier(self.root, type_support, identifiant, int(nombre_touches))

    # Création d'une instance de la classe Ecran
    ecran_instance = Ecran(self.root, type_support, identifiant, taille_ecran)

    # Création d'une instance de la classe PC
    pc_instance = PC(self.root, type_support, identifiant, clavier_instance, ecran_instance)

    # Vous pouvez également sauvegarder ou relire la configuration ici si nécessaire
    # pc_instance.sauvegarder_configuration("configuration_pc.txt")
    # pc_instance.relire_configuration("configuration_pc.txt")


#---Fonction Tkinter------------
def affichage_exo3(self):
    exercise_frame = Frame(self.root)
    exercise_frame.pack(pady=20)

    # Définition police du texte.
    label = Label(exercise_frame, text="Bienvenue dans l'exercice des listes !", font=("Arial", 14))
    label.pack()

    entry_label_type = Label(exercise_frame, text="Entrez un type de materiel:", font=("Arial", 10))
    entry_label_type.pack(pady=10)

    entry_type = Entry(exercise_frame)
    entry_type.pack()

    entry_label_identifiant = Label(exercise_frame, text="Entrez un identifiant du materiel:", font=("Arial", 10))
    entry_label_identifiant.pack(pady=10)

    entry_identifiant = Entry(exercise_frame)
    entry_identifiant.pack()

    entry_label_nombre_touches = Label(exercise_frame, text="Entrez le nombre de touches du clavier:", font=("Arial", 10))
    entry_label_nombre_touches.pack(pady=10)

    entry_nombre_touches = Entry(exercise_frame)
    entry_nombre_touches.pack()

    entry_label_taille_ecran = Label(exercise_frame, text="Entrez la taille de l'écran:", font=("Arial", 10))
    entry_label_taille_ecran.pack(pady=10)

    entry_taille_ecran = Entry(exercise_frame)
    entry_taille_ecran.pack()

    # Création bouton.
    check_button = Button(exercise_frame, text="Afficher liste", font=("Arial", 10),command=lambda: afficher_liste(entry_type.get(), entry_identifiant.get(), entry_nombre_touches.get(), entry_taille_ecran.get(), result_text))
    check_button.pack(pady=10)

    # Création fenêtre pour afficher le résultat.
    result_text = Text(exercise_frame, height=10, width=70)
    result_text.pack()



