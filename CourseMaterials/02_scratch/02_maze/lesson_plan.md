Game loop intro

## EQ's:

- What are conditionals?
- What is the game loop?
- How can we combine conditionals and the game loop to formalize a problem we previously solved?

## Lesson Plan

### Setup

- `maze_final.sb3` loaded up for demonstration's purposes
- Maze worksheet published in Schoology

### Actual Lesson

> NOTE: Have them minimize scratch whenever need attention

- Reflection:
    - What did we talk about last lesson?
    - What is a loop?
        - Why are loops useful?
        - Do a shape together
            - Triangle with triangles at the edges
- What is a conditional?
    - Conditionals from real life
        - What are some conditionals you "evaluate" in the morning
            - Ask the class
            - e.g., If cold then put on coat
    - Act out if/else
        - `if light is on, stand up, else, sit down`
        - `if light changes give me money`
    - Act out loop
        - `while light on, keep jumping`
- Today going to do games
    - How does the game loop work
        - Initialization
        - User input
        - Collision
    - Frame rate
- Scratch initialization
    - Basic Exercises
        - Move Cat (together)
            - Cat starts on left and moves to right side of screen when green flag clicked
        - Only moves when spacebar pressed
        - Drive Cat (together)
            - Arrow keys control direction of cat
            - Space bar makes it move forward
    - Pause and go over common problems and ask why bad
        - Nested ifs
        - No forever loop
        - Inits inside of forever loop
    - Maze game
        - Show game that I made
            - Show how to make own background
            - Show if `touching color` block command
        - Come up with steps to work on together:
            - Delete old "deterministic" maze code
            - Get initialization working
            - Movement
            - Collisions
    - Hand out worksheet
        - Read through it
            - Note that it's like a driving game
                - Avoid concept of `change x` and `change y` for now
            - Right arrow -> turn right
            - Left arrow -> turn left
            - Space -> Move forward
        - Partner up (same as with shapes)
        - Go!
- Reflection:
    - How do we get the impression of motion?
    - If we wanted to simulate this as humans, what would we have to do?
    - How is this similar to the deterministic maze game and how is it different?
    - What would we need to do to make this a professional video game?
    - What could we do if we wanted to play this game on opposite day?
    - What other types of input could we use?

### Homework

- None

### Resources

- Robozzle-like block-based puzzles
    - https://studio.code.org/s/express-2023/lessons/15/levels/3
