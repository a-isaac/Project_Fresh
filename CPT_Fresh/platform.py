#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      User
#
# Created:     20/01/2013
# Copyright:   (c) User 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import pygame
import random
import math
import os
os.environ['SDL_VIDEODRIVER']='windib'

"""This class represents the platform we jump on"""
class Platform (pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
