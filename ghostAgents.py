# ghostAgents.py
# --------------
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
from game import Actions
from game import Directions
import random
from util import manhattanDistance
import util

class GhostAgent( Agent ): # Define a new class named GhostAgent that inherits from the Agent class.
    # Define the constructor method for GhostAgent
    def __init__( self, index ):
        # Inside the constructor, assign the 'index' parameter passed to the constructor
        # to an instance variable named 'index'. This allows each GhostAgent instance
        # to store its own 'index' value.
        self.index = index

    def getAction( self, state ): # Define a method with two parameters 'self' (referring to the instance) and 'state'. 
        dist = self.getDistribution(state) # Call the 'getDistribution' method of the current instance (self) with 
        #the 'state' parameter,and store the result in a variable named 'dist'
        if len(dist) == 0:
            return Directions.STOP
        else:
            return util.chooseFromDistribution( dist ) 
        # If the distribution is not empty, use the 'util.chooseFromDistribution' function 
        # to select an action based on the given distribution, and return that action.

    def getDistribution(self, state):
        "Returns a Counter encoding a distribution over actions from the provided state."
        util.raiseNotDefined() # It raises a "NotImplementedError" exception 

class RandomGhost( GhostAgent ):
    "A ghost that chooses a legal action uniformly at random."
    def getDistribution( self, state ):
        dist = util.Counter() # Create an empty Counter object to store the action distribution.
        for a in state.getLegalActions( self.index ): dist[a] = 1.0 # Loop through all legal actions available to the ghost in the given 'state'.
        # Set the probability of taking the action 'a' to 1.0 in the 'dist' Counter.
        dist.normalize()  # Normalize the distribution so that the probabilities add up to 1.0.
        return dist # Returns the normalized distribution of actions

class DirectionalGhost( GhostAgent ):
    "A ghost that prefers to rush Pacman, or flee when scared."
    def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ):
        self.index = index
        self.prob_attack = prob_attack
        self.prob_scaredFlee = prob_scaredFlee

    def getDistribution( self, state ):
        # Read variables from state
        ghostState = state.getGhostState( self.index )
        legalActions = state.getLegalActions( self.index )
        pos = state.getGhostPosition( self.index )
        isScared = ghostState.scaredTimer > 0

        speed = 1
        if isScared: speed = 0.5

        # Create a list of vectors representing the movement direction for each legal action at a given 'speed'.
        actionVectors = [Actions.directionToVector( a, speed ) for a in legalActions]
        # Create a list of new positions by adding the direction vectors to the current position.
        newPositions = [( pos[0]+a[0], pos[1]+a[1] ) for a in actionVectors]
        # Get the current position of the Pacman agent from the 'state' object.
        pacmanPosition = state.getPacmanPosition()

        # Select best actions given the state
        # Calculate the Manhattan distances from each new position to the Pacman's current position.
        distancesToPacman = [manhattanDistance( pos, pacmanPosition ) for pos in newPositions]
        if isScared: # Check if the ghost is in a "scared" state (when it's fleeing from Pacman).
            bestScore = max( distancesToPacman )
            bestProb = self.prob_scaredFlee
        else:
            bestScore = min( distancesToPacman )
            bestProb = self.prob_attack
        bestActions = [action for action, distance in zip( legalActions, distancesToPacman ) if distance == bestScore]

        # Construct distribution
        dist = util.Counter()
        for a in bestActions: dist[a] = bestProb / len(bestActions)
        for a in legalActions: dist[a] += ( 1-bestProb ) / len(legalActions)
        dist.normalize()
        return dist
