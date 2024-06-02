import pygame
import random

pygame.init()

Hauteur_Écran = 600
Largeur_Écran = 400

écran = pygame.display.set_mode((Hauteur_Écran, Largeur_Écran))
pygame.display.set_caption("Collision")

#Créer le rect principale
rect_1 = pygame.Rect(0, 0, 25, 25)

#créer un liste vide et ensuite ajouter 16 obstacles dans la liste
obstacles = []
for _ in range(16):
  obstacle_rect = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
  obstacles.append(obstacle_rect)

#Definir les couleurs
Fond_écran = (50, 50, 50)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

#Cacher la souris
pygame.mouse.set_visible(False)

exécute = True
while exécute:
  #rafraichir le fond d'écrans
  écran.fill(Fond_écran)

  #vérifier les collisions et changer de couleur
  couleur = VERT
  if rect_1.collidelist(obstacles) >= 0:
    print(rect_1.collidelist(obstacles))
    couleur = ROUGE

  #utiliser les coordonnées de la souris pour le rectangle
  pos = pygame.mouse.get_pos()
  rect_1.center = pos

  #dessiner tout les rectangles
  pygame.draw.rect(écran, couleur, rect_1)
  for obstacle in obstacles:
    pygame.draw.rect(écran, BLEU, obstacle)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exécute = False

  #rafraichir l'écran
  pygame.display.flip()

pygame.quit()