# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import playsound
import pygame
from pygame import mixer,event
mixer.init()
pygame.init()
mixer.music.load('exe021.mp3')
mixer.music.play()
input()
event.wait()
#musica = 'Samie_Bower_-_Different.mp3'
#playsound.playsound(musica)



