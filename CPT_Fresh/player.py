#-------------------------------------------------------------------------------
# Name:        module5
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

#set all colours
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = ( 0,   0,   255)
green     = ( 51,   255,   51)
blueFresh     = (   1, 157, 255)
bluStew = (19,82,149)
orange = (155,131,106)
rBlue = (17,40,110)

#player choice input
p1 = input("1 for fresh 2 for stewie")

"""This class represents the player that the player controls"""
class Player(pygame.sprite.Sprite):

    # -- Attributes
    # Set speed vector of player
    change_x=0
    change_y=0
    levelCount = 0

    # Triggered if the player wants to jump.
    jump_ready = False

    # Count of frames since the player hit 'jump' and we
    # collided against something. Used to prevent jumping
    # when we haven't hit anything.
    frame_since_collision = 0
    frame_since_jump = 0
    frame = 0

    """loads images based on user input"""
    # -- Methods
    # Constructor function
    def __init__(self,x,y):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # List that the fresh images will be saved in.
        self.images=[]
        self.jump_images=[]
        # Load all the fresh images and put them in corresponding list
        if p1 == 1:
            for i in range(1,13):
                img = pygame.image.load("fresh"+str(i)+".png").convert()
                img.set_colorkey(blueFresh)
                self.images.append(img)
        elif p1 ==2:

            for i in range(1,9):
                img = pygame.image.load("stewie"+str(i)+".png").convert()
                img.set_colorkey(bluStew)
                self.images.append(img)
        else:
            for i in range(1,13):
                img = pygame.image.load("fresh"+str(i)+".png").convert()
                img.set_colorkey(blueFresh)
                self.images.append(img)


        # Use default image
        if p1 == 1:
            self.image = self.images[6]
        elif p1 == 2:
            self.image = self.images[5]
        else:
            self.image = self.images[6]

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # Change the speed of the player
    def changespeed_x(self,x):
        self.change_x = x

    def changespeed_y(self,y):
        self.change_y = y

    """Updates the players position for when it moves/collides as well as performing a player animation"""
    # Find a new position for the player
    def update(self,block_list):

        # Save the old x position, update, and see if we collided.
        old_x = self.rect.x
        new_x = old_x + self.change_x
        self.rect.x = new_x

        # Save the old y position, update, and see if we collided.
        old_y = self.rect.y
        new_y = old_y + self.change_y
        self.rect.y = new_y


        # Did this update cause us to hit a wall?
        collide = pygame.sprite.spritecollide(self, block_list, False)
        if collide:
            # Whoops, hit a wall. Go back to the old position
            self.rect.x=old_x


        block_hit_list = pygame.sprite.spritecollide(self, block_list, False)

        for block in block_hit_list:
            # We collided. Set the old pre-collision location
            self.rect.y = old_y
            self.rect.x = old_x

            # Stop our vertical movement
            self.change_y = 0

            # Start counting frames since we hit something
            self.frame_since_collision = 0

        #Update the fresh player
        if p1 == 1:
            if self.change_x < 0:
                # Update our frame counter
                self.frame += 1

                # We go from 0...3. If we are above image 6, reset to 0
                # Multiply by 4 because we flip the image every 4 frames
                if self.frame > 6*4:
                    self.frame = 0

                # Grab the image, do floor division by 4 because we flip
                # every 4 frames.
                # Frames 0...3 -> image[0]
                # Frames 4...7 -> image[1]
                # etc.
                self.image = self.images[self.frame//6]

            # Move left to right.
            if self.change_x > 0:
                self.frame += 1
                if self.frame > 6*4:
                    self.frame = 0
                self.image = self.images[self.frame//6+6]

        #update the stewie animation
        elif p1 ==2:
            if self.change_x < 0:
            # Update our frame counter
                self.frame += 1

                # We go from 0...3. If we are above image 6, reset to 0
                # Multiply by 4 because we flip the image every 4 frames
                if self.frame > 5*4:
                    self.frame = 0

                # Grab the image, do floor division by 4 because we flip
                # every 4 frames.
                # Frames 0...3 -> image[0]
                # Frames 4...7 -> image[1]
                # etc.
                self.image = self.images[self.frame//4]

            # Move left to right.
            if self.change_x > 0:
                self.frame += 1
                if self.frame > 3*4:
                    self.frame = 0
                self.image = self.images[self.frame//4+4]
        else:
            if self.change_x < 0:
                # Update our frame counter
                self.frame += 1

                # We go from 0...3. If we are above image 6, reset to 0
                # Multiply by 4 because we flip the image every 4 frames
                if self.frame > 6*4:
                    self.frame = 0

                # Grab the image, do floor division by 4 because we flip
                # every 4 frames.
                # Frames 0...3 -> image[0]
                # Frames 4...7 -> image[1]
                # etc.
                self.image = self.images[self.frame//6]

            # Move left to right.
            if self.change_x > 0:
                self.frame += 1
                if self.frame > 6*4:
                    self.frame = 0
                self.image = self.images[self.frame//6+6]


        # If the player recently asked to jump, and we have recently
        # had ground under our feet, go ahead and change the velocity
        # to send us upwards
        if self.frame_since_collision < 6 and self.frame_since_jump < 6:
            self.frame_since_jump = 100
            self.change_y -=7.7

        # Increment frame counters
        self.frame_since_collision+=1
        self.frame_since_jump+=1

    # Calculate effect of gravity.
    def calc_grav(self):
        self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= 585 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 585
            self.frame_since_collision = 0

    # Called when user hits 'jump' button
    def jump(self,blocks):
        self.jump_ready = True
        self.frame_since_jump = 0