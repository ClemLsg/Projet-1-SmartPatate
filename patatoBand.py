import os
import pygame
from pygame.locals import *


pygame.init()


piano1 = pygame.mixer.Sound("piano1.wav")
piano2 = pygame.mixer.Sound("piano2.wav")
piano3 = pygame.mixer.Sound("piano3.wav")
battery1 = pygame.mixer.Sound("battery1.wav")
battery2 = pygame.mixer.Sound("battery2.wav")
battery3 = pygame.mixer.Sound("battery3.wav")

fenetre = pygame.display.set_mode((640, 480))


reset = 0
touch = 0
 

### MODE PIANO ###
    
def piano():
    print("Mode piano active")
    
    while 1:
        fichierVar = open("var.txt", "r")
        touch = fichierVar.read()
        if touch == "1" and reset == 0:
            reset = 1
            print("Contact 1 doigt")
            piano1.play()
        if touch == "2" and reset == 0:
            reset = 1
            print("Contact 2 doigts")
            piano2.play()
        if touch == "3" and reset == 0:
            reset = 1
            print("Contact 3 doigts")
            piano3.play()
        if touch == "0":
            reset = 0
        for event in pygame.event.get():  
            if event.type == QUIT:    
                continuer = 0   
            if event.type == KEYDOWN and event.key == K_SPACE:
                guitar()

### MODE GUITARE ###

def guitar():
    print("Mode guitar active")
    while 1:
        fichierVar = open("var.txt", "r")
        touch = fichierVar.read()
        if touch == "1" and reset == 0:
            reset = 1
            print("Contact 1 doigt")
            guitar1.play()
        if touch == "2" and reset == 0:
            reset = 1
            print("Contact 2 doigts")
            guitar2.play()
        if touch == "3" and reset == 0:
            reset = 1
            print("Contact 3 doigts")
            guitar3.play()
        if touch == "0":
            reset = 0
        for event in pygame.event.get():  
            if event.type == QUIT:    
                continuer = 0   
            if event.type == KEYDOWN and event.key == K_SPACE:
                batterie()

### MODE BATTERIE ###

def batterie():
    print("Mode batterie active")
    while 1:
        fichierVar = open("var.txt", "r")
        touch = fichierVar.read()
        if touch == "1" and reset == 0:
            reset = 1
            print("Contact 1 doigt")
            battery1.play()
        if touch == "2" and reset == 0:
            reset = 1
            print("Contact 2 doigts")
            battery2.play()
        if touch == "3" and reset == 0:
            reset = 1
            print("Contact 3 doigts")
            battery3.play()
        if touch == "0":
            reset = 0
        for event in pygame.event.get():  
            if event.type == QUIT:    
                continuer = 0   
            if event.type == KEYDOWN and event.key == K_SPACE:
                piano()

piano()

    


    
