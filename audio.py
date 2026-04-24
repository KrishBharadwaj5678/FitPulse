import pygame

# Init Pygame
pygame.mixer.init()
count_sound = pygame.mixer.Sound("sounds/counter.mp3")

def playSound():
    count_sound.play()