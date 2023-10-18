# pacmanAgents.py
# ---------------
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


from pacman import Directions
from game import Agent
import random
import game
import util

class LeftTurnAgent(game.Agent): #aceasta clasa reprezinta un agent care intotdeauna vireaza la stanga in fiecare oportunitate in joc
    "An agent that turns left at every opportunity"

    def getAction(self, state):
        legal = state.getLegalPacmanActions() #aici se obtin actiunile legale pe care le poate face pacman in joc
        current = state.getPacmanState().configuration.direction #se obtine directia actuala in care se afla pacman in joc
        if current == Directions.STOP: current = Directions.NORTH #daca directia actuala este "stop" (pacman sta pe loc) atunci se seteaza directia curenta la "north" (pacman merge in sus)
        left = Directions.LEFT[current] #se obtine directia la stanga in functie de directia curenta
        if left in legal: return left #daca directia la stanga este una legala atunci se returneaza acea directie
        if current in legal: return current #daca directia curenta este o actiune legala, atunci se returneaza acea directie
        if Directions.RIGHT[current] in legal: return Directions.RIGHT[current] #daca directia la dreapta in functie de directia curenta este o actiune legala, atunci se returneaza acea directie (la dreapta)
        if Directions.LEFT[left] in legal: return Directions.LEFT[left] #daca directia la dreapta in functie de directia curenta este o actiune legala, atunci se returneaza acea directie (la stanga)
        return Directions.STOP #daca niciuna dintre actiuni nu este legata pacman se opreste

class GreedyAgent(Agent):
    def __init__(self, evalFn="scoreEvaluation"):
        self.evaluationFunction = util.lookup(evalFn, globals())
        assert self.evaluationFunction != None

    def getAction(self, state):
        # Generate candidate actions
        legal = state.getLegalPacmanActions()
        if Directions.STOP in legal: legal.remove(Directions.STOP)

        children = [(state.generateChild(0, action), action) for action in legal]
        scored = [(self.evaluationFunction(state), action) for state, action in children]
        bestScore = max(scored)[0]
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        return random.choice(bestActions)

def scoreEvaluation(state):
    return state.getScore()
