#Importer la bibliothèque Pygame, qui est utilisée pour créer des jeux en Python.
import pygame
#module sys qui est nécessaire pour gérer les événements système.
import sys
#importer le module random pour générer des nombres aléatoires.
import random

pygame.init()

FL, FH = 800, 800 #taille de la fenêtre de jeu

Taille_blocs = 50
POLICE = pygame.font.Font("font.ttf", Taille_blocs * 2) #établir la police

fenêtre = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Projet Personel")
horloge = pygame.time.Clock() #FPS


class Serpent:
    def __init__(état): #définir toutes les variable du serpent avec l'argument "état"
        état.x, état.y = Taille_blocs, Taille_blocs
        état.xdirection = 1
        état.ydirection = 0
        état.tête = pygame.Rect(état.x, état.y, Taille_blocs, Taille_blocs)
        état.corp = [pygame.Rect(état.x - Taille_blocs, état.y, Taille_blocs, Taille_blocs)]
        état.mort = False

    def nouveau(état):
        global pomme

        for carré in état.corp: #définir les conditions de mort (tête touche son propre corp ou les limites de l'écran)

            if état.tête.x == carré.x and état.tête.y == carré.y:
                état.mort = True
            if état.tête.x not in range(0, FL) or état.tête.y not in range(0, FH):
                état.mort = True

        if état.mort: #"Faire réappraitre lorsque le serpent meurt
            état.x, état.y = Taille_blocs, Taille_blocs
            état.tête = pygame.Rect(état.x, état.y, Taille_blocs, Taille_blocs)
            état.corp = [pygame.Rect(état.x - Taille_blocs, état.y, Taille_blocs, Taille_blocs)]
            état.xdirection = 1
            état.ydirection = 0
            état.mort = False
            pomme = POMME()

        état.corp.append(état.tête)

        for i in range(len(état.corp) - 1):
            état.corp[i].x, état.corp[i].y = état.corp[i + 1].x, état.corp[i + 1].y
        état.tête.x += état.xdirection * Taille_blocs
        état.tête.y += état.ydirection * Taille_blocs
        état.corp.remove(état.tête)


class POMME: #créer un rectanlque qui représente la pomme
    def __init__(état):
        état.x = int(random.randint(0, FL) / Taille_blocs) * Taille_blocs
        état.y = int(random.randint(0, FH) / Taille_blocs) * Taille_blocs    #Faire apparaitre au hasard la pomme
        état.rect = pygame.Rect(état.x, état.y, Taille_blocs, Taille_blocs)
    def nouveau(état):
        pygame.draw.rect(fenêtre, "orange", état.rect)


def dessinerGrille():
    for x in range(0, FL, Taille_blocs):
        for y in range(0, FH, Taille_blocs):
            rect = pygame.Rect(x, y, Taille_blocs, Taille_blocs)
            pygame.draw.rect(fenêtre, "#000000", rect, 1)


score = POLICE.render("1", True, "white")

score_pos = score.get_rect(center=(FL / 2, FH / 20))

dessinerGrille()

serpent = Serpent()

pomme = POMME()

while True:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            action.quit()
            sys.exit()
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_DOWN or action.key == pygame.K_s:
                serpent.ydirection = 1
                serpent.xdirection = 0
            elif action.key == pygame.K_UP or action.key == pygame.K_w:
                serpent.ydirection = -1
                serpent.xdirection = 0
            elif action.key == pygame.K_RIGHT or action.key == pygame.K_d:
                serpent.ydirection = 0
                serpent.xdirection = 1
            elif action.key == pygame.K_LEFT or action.key == pygame.K_a:
                serpent.ydirection = 0
                serpent.xdirection = -1

    serpent.nouveau()

    fenêtre.fill('grey')
    dessinerGrille()

    pomme.nouveau()

    score = POLICE.render(f"{len(serpent.corp) + 1}", True, "white")
   

    pygame.draw.rect(fenêtre, "blue", serpent.tête)

    for carré in serpent.corp:
        pygame.draw.rect(fenêtre, "green", carré)

    fenêtre.blit(score, score_pos)

    if serpent.tête.x == pomme.x and serpent.tête.y == pomme.y:
        serpent.corp.append(pygame.Rect(carré.x, carré.y, Taille_blocs, Taille_blocs))
        pomme = POMME()


    pygame.display.update()
    horloge.tick(7)