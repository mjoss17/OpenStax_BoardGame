---
noteId: "c33bb8c0523811ecaae71f223f502a36"
tags: []

---

Flat Message Passing Board Game
Author: Matt Joss
Date 30/11/2021

This is a refactored version of a board game that was send to Matt Joss by OpenStax as a coding assessment. The Previous version of the game can be found in refactoring_exercises.py and the previous README can be found in Instructions.md

This game is designed for extensibility first and foremost. The various components of the previous game and the actions associated with them have been abstracted into two types of interfaces - GameObjects and Messages. On the simplest level the board game is a loop in which Messages are passed between GameObjects until there is some exit condition and the game is over. 

One can find this loop in Game.start()
Here the 

