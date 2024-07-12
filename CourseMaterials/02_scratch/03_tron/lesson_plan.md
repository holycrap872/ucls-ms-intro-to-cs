# Tron

## Essential Questions

- How is a computer game like a puzzle?
- What different movement systems can the game loop reproduce?
- What are ways we can reduce the amount of repeated code?

## Lesson Plan

In this lesson, we increase the "fun" from the previous maze game and start
to investigate different types of motion. In particular, we examine the
difference between moves inside an `if` and moves outside an `if`. In doing
so, student practice using the game loop pattern to structure their thinking.
The overall goal is to have them create the program with minimal hints and then
appreciate how engaging it can be.

### Setup

- Have `drawing_game_skeleton.sb3` loaded up with the code hidden
- Have `tron.sb3` loaded up with the code hidden
- Have YouTube clip from tron: https://youtu.be/hMT8tRrEMC4?t=84s

### Actual Lesson

#### Day 1

- Reflection:
    - What did we do last class?
        - What is the game loop?
        - What are the parts of the game loop?
        - What is the difference between drawing shapes and the games?
            - infinite loop
            - No user input
- Let's see if you can figure out how one of my simple "games" works
    - Show `drawing_game_skeleton.sb3`
    - See if can recreate each part of game loop as a class
        - if/else for pen down
        - Change color constantly
    - Once solve: turn it into four sprite drawing game by altering x, y multipliers
        - 4x reflection over the axes
- Today going to do another video game
    - https://youtu.be/hMT8tRrEMC4?t=84s
    - Show my version of tron game and play with two people as an example
- Talk about similarities/differences between previous game
    - Always moving!
- Show new blocks
    - OR block
    - touching wall block
- Pair up
    - This is a puzzle to see if you can figure it out on your own
    - Start!
- Reflection:
    - What is a game that this reminds you of?
    - What was easy?
    - What was hard?
    - What did you remember from last time?
    - What did you forget from last time?

##### Homework

- Schoology assessment on game loops
- Questions:
    1. Which of the following are parts of the "game loop" algorithm?
        - initialization
        - get user input
        - move characters
        - check for collisions
        - pause and get a soda
    2. What is the Computer Science translation of the sentence "when it rains I wear my coat"?
        - forever is_raining, then wear coat
        - if is_raining, then wear coat
        - if is_raining, forever wear coat
    3. Why is a forever loop a better option than a repeat loop with a game?
        - If statements only go into forever loops.
        - Repeats are only for shapes.
        - You don't know how long the user is going to play.
    4. Fill in the blanks to make a square:
        ```
        when green flag clicked
        goto 0, 0
        point in direction 90
        erase all
        pen down
        repeat _:
            move 100 steps
            turn right _ degrees
        ```

#### Day 2

- Reflection
    - Game loop
    - Conditionals
    - Tron
- Going to get back to game, but first: real life conditionals
    - Conditionals don't just have to be in computer programs
    - Can think of your life as a program
    - Some examples:
        - If hungry, then eat
        - repeat until not thirst: drink
    - What are a few you can think of?
        - if, if/else, repeat
    - Hand out worksheet
        - `conditionals_worksheet_long.docx` if have long block
        - `conditionals_worksheet_short.docx` if regular class
        - Work with elbow partner for ~6m
        - The crazier the better!
    - Reconvene and discuss
        - Have each group share out their best one
        - The reason it's written this way is because it's the same as Python
- Review Tron
    - Get started again
- When finished, have rotate so can play other people's games
    - Allow to play 2 or 3 other games
- Reflection
    - What was good about other people's games
    - What could be improved
    - Important to accept feedback and improve
        - Helps find bugs
        - Helps improve products
