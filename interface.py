# Importation du module Tkinter qui permet de créer une interface graphique
# Importation du module PIL pour gérer les photos.
# Importation du module pygame pour gérer les sons.
from exo.exo1 import Calcul
from exo.exo2 import Suite
from exo.exo3 import *
from tkinter import *
from PIL import Image, ImageTk
import pygame


def exo1():
    root = Tk()
    root.title("Exercice Seuil")   # Titre de la fenêtre.
    root.geometry('600x600')    # Taille de la fenêtre.
    calcul_obj = Calcul(root)   # Instancier l'objet Calcul.
    calcul_obj.affichage_exo1() # Appeler la méthode affichage sur l'objet.


def exo2():
    root = Tk()
    root.title("Exercice des calculs")   
    root.geometry('600x600')     
    calcul_obj = Suite(root)   # Instancier l'objet Calcul.
    calcul_obj.affichage_exo2()   # Appeler la méthode affichage sur l'objet.


def exo3():
    root = Tk()
    root.title("Exercice des listes")   
    root.geometry('600x600')
    calcul_obj = Materiel(root)  # Instancier l'objet Calcul
    calcul_obj.affichage_exo3()  # Appeler la méthode affichage sur l'objet.


def creer_menu():
    root = Tk()
    root.title("MENU PYTHON TP2 - Jules PICHON - ESGI3")
    root.geometry('1500x1500')


    # Redimensionne l'image de fond pour s'adapter à la taille de la fenêtre.
    def resize_image(event):   
        new_width = event.width
        new_height = event.height
        resized_image = background_image.resize((new_width, new_height), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)

    
    # Charge l'image de fond
    background_image = Image.open("Images/background.jpg") 
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
    background_photo = ImageTk.PhotoImage(background_image)


    # Lie la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
    root.bind("<Configure>", resize_image)


    # Initialisation de pygame.
    pygame.mixer.init()


    # Charge et joue de la musique sur la page d'accueil.
    pygame.mixer.music.load("Sounds/minecraft_main_theme.mp3")
    pygame.mixer.music.play(-1)  # Joue en boucle (-1 signifie en boucle infinie).


    def play_sound(sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.play()
    

    # Création d'un label pour afficher l'image de fond
    background_label = Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)
    background_label.photo = background_photo


    # Création d'un cadre (Frame) pour organiser le contenu.
    frame = Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")  # "nsew" permet l'expansion dans toutes les directions.

    # Création d'un label avec le texte centré.
    label = Label(frame, text="\nBienvenue dans le menu du TP3 consacré au langage de programmation Python !\nVoici la liste des exercices disponibles :\n", font=("Arial", 14))
    label.grid(row=0, column=0, columnspan=3, pady=0)  # On ajoute un espace en haut et en bas.


    # Création d'un sous-cadre (Frame) pour les boutons et les centrer.
    button_frame = Frame(frame)
    button_frame.grid(row=1, column=0, columnspan=3)

    
    # Création d'un bouton pour chaque exercice et association d'un son et d'une image à un bouton.
    btn1 = Button(button_frame, text="Exercice du Seuil !", command=lambda: (play_sound("Sounds/huh.mp3"), exo1()))
    btn2 = Button(button_frame, text="Exercice des suites", command=lambda: (play_sound("Sounds/bully.mp3"), exo2()))
    btn3 = Button(button_frame, text="Exercice des listes", command=lambda: (play_sound("Sounds/ez.mp3"), exo3()))


    # On met les boutons sur la même ligne.
    btn1.grid(row=0, column=0, padx=10)
    btn2.grid(row=0, column=1, padx=10)
    btn3.grid(row=0, column=2, padx=10)


    # Centrer le sous-cadre (Frame) des boutons.
    button_frame.grid_columnconfigure(0, weight=1)  # Permet d'étirer la colonne.

    # On démarre la boucle d'évènements.
    root.mainloop()


def main():
    creer_menu()

