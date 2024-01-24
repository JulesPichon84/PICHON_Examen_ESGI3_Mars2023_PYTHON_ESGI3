# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *


#---Définition classe principale-----------
class Suite:
    def __init__(self, root):
        self.root = root

    def testsuite(self, A, B, N, result_text):
        try:    # On vérifie si les nombres rentrés sont positif.
            N = int(N); A = float(A); B = float(B) 
            if N <= 0:
                raise ValueError("Veuillez entrer un entier N (> 0)!")
            if A <= 0:
                raise ValueError("Veuillez entrer un réel A (> 0)!")
            if B <= 0:
                raise ValueError("Veuillez entrer un réel B (> 0)!")
        except ValueError as e: # On gère le cas où l'entrée n'est pas un nombre entier positif.
            result_text.delete(1.0, END)
            result_text.insert(END, f"Erreur de typage: {str(e)}\n")
            return

        # Initialisation des premiers termes de la suite
        Un = A
        Un_1 = B

        for n in range(2, N + 1):
            Un, Un_1 = (Un + Un_1) / 2.0, 2 / (1 / Un_1 + 1 / Un)

        # Affichage du résultat dans la fenêtre
        result_text.delete(1.0, END)
        result_text.insert(END, f"Suite calculée pour N={N}, A={A}, B={B}\n")
        result_text.insert(END, f"Un: {Un}\nUn-1: {Un_1}\n")   

    #---Fonction Tkinter------------
    def affichage_exo2(self):

        exercise_frame = Frame(self.root)
        exercise_frame.pack(pady=20)

        # Définition police du texte.
        label = Label(exercise_frame, text="Bienvenue dans l'exercice de la suite !", font=("Arial", 14))
        label.pack()

        entry_label = Label(exercise_frame, text="Entrez un nombre entier N (>0):", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry_N = Entry(exercise_frame)
        entry_N.pack()

        entry_label = Label(exercise_frame, text="Entrez un nombre réel A (>0):", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry_A = Entry(exercise_frame)
        entry_A.pack()

        entry_label = Label(exercise_frame, text="Entrez un nombre réel B (>0):", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry_B = Entry(exercise_frame)
        entry_B.pack()

        # Création bouton.
        check_button = Button(exercise_frame, text="Calculer le prix de l'article", font=("Arial", 10), command=lambda: self.testsuite(entry_A.get(), entry_B.get(), entry_N.get(), result_text))
        check_button.pack(pady=10)

        # Création fenêtre pour afficher le résultat.
        result_text = Text(exercise_frame, height=10, width=70)
        result_text.pack()