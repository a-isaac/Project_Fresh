#-------------------------------------------------------------------------------
# Name:        module2
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

"""Creates a wall object using given dimensions and colour
input: x,y,width,height,colour
return: none"""

class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a wall, of the size specified in the parameters and colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x