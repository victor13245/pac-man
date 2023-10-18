# keyboardAgents.py
# -----------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import Agent
from game import Directions
import random

# seteaaza tastele a -> stanga, d -> dreapta, w-> sus, s-> jos si q -> stop precum si sagetile

class KeyboardAgent(Agent):
    """
    An agent controlled by the keyboard.
    """
    # NOTE: Arrow keys also work.
    WEST_KEY  = 'a'
    EAST_KEY  = 'd'
    NORTH_KEY = 'w'
    SOUTH_KEY = 's'
    STOP_KEY = 'q'  #Se definesc tastele de la tastatură asociate cu mișcările în diferite direcții și oprirea

    # starea initiala

    def __init__( self, index = 0 ):

        self.lastMove = Directions.STOP #retine ultima micsare efectuata de agent
        self.index = index #indexul agentului 
        self.keys = [] #se creeaza o lista goala in care se stocheaza tastele apasate

    #functie care verifica daca au fost apasate tastele si returneaza miscarea care se va efectua

    def getAction( self, state):
    def getAction( self, state):  #primeste ca argument starea jocului si returneaza o actiune pe baza tastelor apasate
        from graphicsUtils import keys_waiting
        from graphicsUtils import keys_pressed
        keys = list(keys_waiting()) + list(keys_pressed()) #preia starea tastelor (apasat sau in asteptare)
        if keys != []: #daca lista nu este goala
            self.keys = keys 
        keys = list(keys_waiting()) + list(keys_pressed())  #exista o lista de taste apasate si una de taste asteptate stocate in keys
        if keys != []: #daca in lista exista taste apasate 
            self.keys = keys #se actualizeaza lista agentului cu noile taste apasate 

        legal = state.getLegalActions(self.index)
        move = self.getMove(legal) #determina urmatoarea miscare pe baza actiunilor legale
        legal = state.getLegalActions(self.index)  #Se obțin acțiunile legale disponibile pentru agent în starea curentă a jocului si se stocheaza in legal (acțiuni legale = agentul poate alege să le efectueze în acea stare specifică fără a încălca regulile jocului sau restricțiile mediului)
        move = self.getMove(legal)  #determina mișcarea dorită de agent pe baza tastelor apăsate și a acțiunilor legale

        if move == Directions.STOP: #daca miscare este oprirea
            # Try to move in the same direction as before
            if self.lastMove in legal:  #se verifica daca ultima miscare e legala 
                move = self.lastMove #daca da, agentul continua in aceeasi directie 

        if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP 
        if (self.STOP_KEY in self.keys) and Directions.STOP in legal: move = Directions.STOP
        #Dacă tasta de oprire (STOP_KEY) este apăsată și oprirea este legală atunci agentul se va opri

        if move not in legal:
            move = random.choice(legal) #in cazul in care miscarea nu este legaal, se alege o miscare random
        if move not in legal:  #daca nu este legala 
            move = random.choice(legal)  #va alege random o miscare legala

        self.lastMove = move #actualizam ultima miscare cu cea curenta si returnam miscarea curenta
        return move
        self.lastMove = move #se actualizeaza ultima miscare cu miscarea curenta 
        return move  #se returneaza miscarea curenta 

    
    #realizeaza miscarea pe directia aleasa
    def getMove(self, legal):
        move = Directions.STOP
    def getMove(self, legal):  #primește o listă de acțiuni legale și returnează mișcarea dorită pe baza tastelor apăsate
        move = Directions.STOP  #se initializeaza miscarea cu oprirea 
        if   (self.WEST_KEY in self.keys or 'Left' in self.keys) and Directions.WEST in legal:  move = Directions.WEST
       #Se verifică dacă tasta asociată mișcării spre vest este apăsată sau dacă tasta "Left" este apăsată 
       #și mișcarea spre vest este legală. 
       #Dacă da, mișcarea devine Directions.WEST


        if   (self.EAST_KEY in self.keys or 'Right' in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if   (self.NORTH_KEY in self.keys or 'Up' in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if   (self.SOUTH_KEY in self.keys or 'Down' in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move  #se returneaza miscarea calculata

# seteaaza tastele j -> stanga, l -> dreapta, i-> sus, k-> jos si u -> stop precum si sagetile

class KeyboardAgent2(KeyboardAgent):
class KeyboardAgent2(KeyboardAgent):  #similara cu clasa KeyboardAgent1
    """
    A second agent controlled by the keyboard.
    """
    # NOTE: Arrow keys also work.
    WEST_KEY  = 'j'
    EAST_KEY  = "l"
    NORTH_KEY = 'i'
    SOUTH_KEY = 'k'
    STOP_KEY = 'u' #Se definesc tastele de la tastatură asociate cu mișcările în diferite direcții și oprirea

    def getMove(self, legal): #se suprascrie metoda getMove pt a utiliza noile taste apasate miscarilor
        move = Directions.STOP
        if   (self.WEST_KEY in self.keys) and Directions.WEST in legal:  move = Directions.WEST
        if   (self.EAST_KEY in self.keys) and Directions.EAST in legal: move = Directions.EAST
        if   (self.NORTH_KEY in self.keys) and Directions.NORTH in legal:   move = Directions.NORTH
        if   (self.SOUTH_KEY in self.keys) and Directions.SOUTH in legal: move = Directions.SOUTH
        return move #se returneaza miscarea calculata 
