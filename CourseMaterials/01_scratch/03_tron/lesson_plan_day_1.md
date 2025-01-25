## Essential Questions

- How is a computer game like a puzzle?
- What different movement systems can the game loop reproduce?
- What are ways we can reduce the amount of repeated code?

## Lesson Plan

In this lesson, we increase the "fun" from the previous maze game and start
to investigate different types of motion by creating the game Tron. In
particular, we examine the difference between moves inside an `if` and moves
outside an `if`. In doing so, student practice using the game loop pattern to
structure their thinking. The overall goal is to have them create the program
with minimal hints and then appreciate how engaging it can be.

### Setup

- Have `drawing_game_skeleton.sb3` loaded up with the code hidden
- Have `tron.sb3` loaded up with the code hidden
- YouTube videos loaded up
    - https://youtu.be/hMT8tRrEMC4?t=84s
- Schoology assessment on "game loop algorithm" posted
    - See `assessment.md`

### Actual Lesson

- Reflection:
    - What did we do last class?
        - What is the game loop?
        - What are the parts of the game loop?
        - What is the difference between drawing shapes and the games?
            - infinite loop
            - No user input
- Let's see if you can figure out how one of my simple "games" works
    - Show `drawing_game_skeleton.sb3` (without showing code)
        - `drawing_game_skeleton.sb3` **has** `change color` block in it for demo
    - See if can recreate each part of game loop as a class
        - if/else for pen down
    - Once solve: turn it into four sprite drawing game by altering x, y multipliers
        - 4x reflection over the axes
- Today going to do another video game
    - https://youtu.be/hMT8tRrEMC4?t=84s
    - Show my version of Tron game
    - Play against volunteer as an example
- Talk about similarities/differences between previous game
    - Always moving!
- Show new blocks
    - `or` block
    - `touching edge` block
    - `stop all` block
- Pair up
    - This is a puzzle to see if you can figure it out on your own
    - Start!
- Reflection:
    - What is a game that this reminds you of?
    - What was easy?
    - What was hard?
    - What did you remember from last time?
    - What did you forget from last time?

### Homework

- Schoology assessment: `Homework: Parts of the Game Loop`
