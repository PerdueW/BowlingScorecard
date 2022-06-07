#!/usr/bin/python3

import os
import sys
from tkinter import *
import tkinter as tk
import re
import itertools

class bowling:
    print("Welcome to Warren's Bowling Game")
    print(" ")

    """
    This section of code gets the number of players for the game and ensures only
    the correct number is entered and is between 1 and 5 and then creates the 
    dictionary to contain the player(s) names, scores, and results
    """
    numPlayers = 0
    while True:
        numPlayers = input("Please enter the number of players. (1-5): ")
        if numPlayers.isdigit() and 1 <= int(numPlayers) <= 5:
            break
        else:
            print("Sorry, wrong number. Please enter a number between 1-5.")
            
    gameInfo = {}
    a = 1
    while a <= int(numPlayers):
        playerName = input("Please enter Player " + str(a) + "'s name: ")
        gameInfo[playerName] = {}
        a += 1
    print("")
    b = 1  #This initializes b which is used to keep track of each round
    score1 = 0
    score2 = 0
    roundT = 0
    scores = []
    while b < 10:
        for playerName in gameInfo:   
            while True:
                firstRoll = str(input("Please enter " + playerName + "'s Frame " + str(b) + " first roll result: "))
                firstRoll = firstRoll.upper()
                if re.match("^[X0-9-]+$", firstRoll):
                    score1 = firstRoll
                    scores.append(score1)
                else:
                    print("Please enter a number 0-9, -, or an X")
                    
                secondRoll = str(input("Please enter " + playerName + "'s Frame " + str(b) + " second roll result: "))
                secondRoll = secondRoll.upper()
                if re.match("^[X0-9/-]+$", secondRoll):
                    score2 = secondRoll
                    scores.append(score2)
                else:
                    print("Please enter a number 0-9, -, /, or X")
                break
            gameInfo[playerName][b] = scores
            scores = []        
        b += 1
    
    """
    This section of code will handle gathering the 10th frame scores
    and store them to the gameInfo dictionary.
    """
    for playerName in gameInfo:
        while True:
            firstRoll = str(input("Please enter " + playerName + "'s Frame 10 first roll result: "))
            firstRoll = firstRoll.upper()
            if re.match("^[X0-9-]+$", firstRoll):
                if firstRoll == "X":
                    score1 = firstRoll
                    scores.append(score1)
                    secondRoll = str(input("Strike! Please enter " + playerName + "'s Frame 10 second roll result: "))
                    secondRoll = secondRoll.upper()
                    if re.match("^[X0-9-]+$", secondRoll):
                        if secondRoll == "X":
                            score2 = secondRoll
                            scores.append(score2)
                            thirdRoll = str(input("Please enter " + playerName + "'s Frame 10 third roll result: "))
                            thirdRoll = thirdRoll.upper()
                            if re.match("^[X0-9-]+$", thirdRoll):
                                    score3 = thirdRoll
                                    scores.append(score3)       
                            else:
                                print("Please enter a number 0-9, an /, -, or X")
                        else:
                            score2 = secondRoll
                            scores.append(score2)
                            thirdRoll = str(input("Please enter " + playerName + "'s Frame 10 third roll result: "))
                            thirdRoll = thirdRoll.upper()
                            if re.match("^[0-9/-]+$", thirdRoll):
                                    score3 = thirdRoll
                                    scores.append(score3)
                            else:
                                print("Please enter a number 0-9, an /, -, or X")
                    else:
                        print("Please enter a number 0-9, an /, -, or X")                    
                elif firstRoll.isnumeric():
                    score1 = firstRoll
                    scores.append(score1)
                    secondRoll = str(input("Please enter " + playerName + "'s Frame 10 second roll result: "))
                    secondRoll = secondRoll.upper()
                    if re.match("^[0-9/-]+$", secondRoll):
                        if secondRoll == "/":
                            score2 = secondRoll
                            scores.append(score2)
                            thirdRoll = str(input("Please enter " + playerName + "'s Frame 10 third roll result: "))
                            thirdRoll = thirdRoll.upper()
                            if re.match("^[X0-9-]+$", thirdRoll):
                                score3 = thirdRoll
                                scores.append(score3)
                            else:
                                print("Please enter a number 0-9, -, or X")
                        else:
                            score2 = secondRoll
                            scores.append(score2)                      
                    else:
                        print("Please enter a number 0-9, an /, -, or X")
            else:
                print("Please enter a number 0-9, -, or an X")
            break
        gameInfo[playerName][10] = scores
        scores = []         
    print(" ")
    """
    This section will retrieve the game information from the dictionaries and lists and
    place them in to a list so that the next function can iterate over the list and do
    the calculations and display the total.
    """
    i = 1
    gameScoresperPlayer = {}
    gamePoints = []
    for player, value in gameInfo.items():
        while i <= 10:
            if i <= 9:
                roll1 = value[i][0]
                roll2 = value[i][1]
                gamePoints.append(roll1)
                gamePoints.append(roll2)
            if i == 10:
                length = len(value[10])
                if length == 2:
                    roll1 = value[10][0]            
                    roll2 = value[10][1]
                    gamePoints.append(roll1)
                    gamePoints.append(roll2)
                elif length == 3:
                    roll1 = value[10][0]            
                    roll2 = value[10][1]
                    roll3 = value[10][2]
                    gamePoints.append(roll1)
                    gamePoints.append(roll2)
                    gamePoints.append(roll3)

            i += 1
        gameScoresperPlayer[player] = gamePoints
        #gamePoints = []

    #print(gameScoresperPlayer)
    """
    This section will itereated over the the list and do the logic and calculate
    the scores and display the final results.
    """
    finalScore = 0
    for player, scores in gameScoresperPlayer.items():
        for score in scores:
            if score.isnumeric():
                finalScore = finalScore + int(score)
            else:
                if score == "-":
                    score = 0
                elif score == "/":
                    score = 10
                    finalScore = finalScore + int(score)
                elif score == "X":
                    score = 10
                    finalScore = finalScore + int(score)
    print(player, " total was: ", finalScore)
                

    
















































        
  
