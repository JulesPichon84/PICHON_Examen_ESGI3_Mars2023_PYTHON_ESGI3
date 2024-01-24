# Importation du module Tkinter qui permet de créer une interface graphique.
from tkinter import *


#---Définition classe principale-----------
class Calcul:
    def __init__(self, root):
        self.root = root

#---Test seuil------------
    def testseuil(self, p, t, result_text):
        try:    # On vérifie si l'entrée du prix et du seuil sont bien des flotants positifs.
            p = float(p)
            t = float(t)
            if p <= 0 or p >= 1000 or t <= 1.08:
                    raise ValueError("Veuillez entrer le prix d'un article (n < 1000) et un taux d'inflation (n > 1.08)!")
        except ValueError as e: # On gère le cas où l'entrée n'est pas un nombre entier positif.
            result_text.delete(1.0, END)
            result_text.insert(END, f"Erreur de typage: {str(e)}\n")
            return
        
        Nombre_mois = 0
        while p < 1000:
            p *= t
            Nombre_mois += 1

        result_text.delete(1.0, END)  # Efface le texte précédent.
        result_text.insert(END, f"Le prix de l'article atteint 1000 après {Nombre_mois} mois. Prix final : {p:.2f}")
            
            

    #---Fonction Tkinter------------
    def affichage_exo1(self):

        exercise_frame = Frame(self.root)
        exercise_frame.pack(pady=20)

        # Définition police du texte.
        label = Label(exercise_frame, text="Bienvenue dans l'exercice du Seuil !", font=("Arial", 14))
        label.pack()

        entry_label = Label(exercise_frame, text="Entrez le prix d'un article (<1000):", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry_article = Entry(exercise_frame)
        entry_article.pack()

        entry_label = Label(exercise_frame, text="Entrez un taux d'inflation (>1.08):", font=("Arial", 10))
        entry_label.pack(pady=10)

        entry_taux = Entry(exercise_frame)
        entry_taux.pack()

        # Création bouton.
        check_button = Button(exercise_frame, text="Calculer le prix de l'article", font=("Arial", 10), command=lambda: self.testseuil(entry_article.get(), entry_taux.get(), result_text))
        check_button.pack(pady=10)

        # Création fenêtre pour afficher le résultat.
        result_text = Text(exercise_frame, height=10, width=70)
        result_text.pack()