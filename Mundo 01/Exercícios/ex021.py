#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/gabri/PycharmProjects/Python3-Mundo1/Exercícios/ex021.mp3')
pygame.mixer.music.play()
