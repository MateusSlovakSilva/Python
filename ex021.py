import pygame
msg = ('Exercícios 021 Play music')
print(msg)
pygame.init()
pygame.mixer.music.load('imagine.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
