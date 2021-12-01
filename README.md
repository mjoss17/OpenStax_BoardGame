---
noteId: "c33bb8c0523811ecaae71f223f502a36"
tags: []

---

# Flat Message Passing Board Game
Author: Matt Joss
Date 30/11/2021

This is a refactored version of a board game that was send to Matt Joss by OpenStax as a coding assessment. The Previous version of the game can be found in refactoring_exercises.py and the previous README can be found in Instructions.md

This game is designed for extensibility first and foremost. The various components of the previous game and the actions associated with them have been abstracted into two types of interfaces - GameObjects and Messages. On the simplest level the board game is a loop in which Messages are passed between GameObjects until there is an exit condition and the game is over. 

## How to Run the Game 

The /test_suite directory holds 4 different python tests that can be used to ensure functionality, one of which is the run_game.py script. When this is run the full game will be printed to the console and a winner will be declared at the end

## Notes

This version of the game has a few extra features that are not directly being used but offer many interesting changes to the game. The TurnDecider GameObject allows messages and rules to alter the way that turns are alotted - such as in reverse order or skipping someone. The Gamemaster object allows non-player actions to alter the course of the game by modifying the board, the questions, the player scores, or the questions. 


