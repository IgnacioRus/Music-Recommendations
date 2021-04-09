<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Tic Tac Toe
*Ignacio Rus Prados*

*DAFT-MAR21, Remote, 25/03/2021*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description

I decided to code my own version of the well-known Tic Tac Toe game. It provides a visual representation of the board and it is interactive, challenging the player to beat the computer (SPOILER ALERT: it's impossible). I chose this game because I thought it would be challenging to find a way to code the game rules, and even harder to code the AI without specifying every possible move.

## Rules

Tic Tac Toe challenges two players to beat each other by placing, one at a time and switching turns, noughts and crosses in a 3x3 board. The player who succeeds in placing three of their marks in a diagonal, horizontal, or vertical row is the winner.

## Workflow

First I created an extensive txt file with the pseudocode that helped me to organize the project and separate it in different sections. Then I proceeded to code the different parts of the code in (more or less) the following order:

-Visual interface and basic interaction: asking the player if they want to be first/second or if they want to play again)

-Interaction with the player: giving the ability to place markers

-Rules of the game: checking when a player has won (or if it's a tie)

-Computer AI: strategy to always find the best move.

I also took care of readibility, error handling and such throughout the whole process.

## Organization

I used the Trello template to organize my work and keep track of all remaining tasks.

My repository consists of:

- Folder: Project-Week-1-Build-Your-Own-Game
    - Kick-Off.md (Instructions for the project)
    - .gitignore 
    - Folder: your-project
        - DAFT Presentation Tic_Tac_Toe.key (presentation of the project)
        - README.md ("Read me" file including a summary of my project. You are literally looking at it)
        - Folder: TicTacToe 
            - pseudocode.txt (text file including the pseudocode)
            - TicTacToe.ipynb (a python3-jupyter-notebook file including all the code that makes up the game)
            - tictactoe.py (an python3 file that can run the game by typing "python3 tictactoe.py" in Terminal)

## Links

[Repository](https://github.com/IgnacioRus/Project-Week-1-Build-Your-Own-Game)  
[Trello](https://trello.com/b/ymfsxblR/tic-tac-toe-plan)  
