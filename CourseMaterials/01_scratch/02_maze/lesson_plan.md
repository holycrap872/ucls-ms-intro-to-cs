## Essential Questions

- What are conditionals?
- What is the game loop?
- How can we combine conditionals and the game loop to formalize a problem we previously solved?

## Lesson Plan

### Setup

- `maze_final.sb3` loaded up for demonstration's purposes
    - https://scratch.mit.edu/projects/1068455229/editor/
- Maze worksheet published in Schoology
    - `user_maze.docx`

### Pacing

- Review (7m)
- Conditionals (8m)
- Game Loop + Move Cat (10m)
- Maze Game (30m)
    - If not long block, will likely need to give them time next class

### Actual Lesson

- Reflection:
    - What is a loop?
    - Why are loops useful?
    - Do a shape as a class
        - Triangle with triangles at the edges
- What is a conditional?
    - Real life conditionals
        - What are some conditionals you "evaluate" in the morning?
            - e.g., If cold then put on coat
    - Act out if/else
        - `if light is on, stand up, else, sit down`
        - `if light changes give me money`
    - Act out loop
        - `while light on, keep jumping`
- Today going to do first video game
    - How does the game loop work:
        - Initialization
        - Get user input
        - Move non-player characters
        - Collision
    - Frame rate
- Basic Exercises
    - Move Cat (together)
        - Cat starts on left and moves to right side of screen when green flag clicked
    - Only moves when space bar pressed
    - Drive Cat (together)
        - Arrow keys control direction of cat
        - Space bar makes it move forward
- Maze game
    - Show game that I made
        - https://scratch.mit.edu/projects/1068455229/editor/
        - Show `touching color` block
    - Come up with steps to work on together:
        - Delete old "deterministic" maze code
        - Get initialization working
        - Movement
        - Collisions
- Show rubric/worksheet
    - Read through it
    - Note that it's like a driving game
        - Avoid concept of `change x` and `change y` for now
- Go!
    - About half-way through, pause and go over common problems and ask why bad
        - Nested ifs
        - No forever loop
        - Inits inside of forever loop
- Reflection:
    - How do we get the impression of motion?
    - How is this similar to the deterministic maze game and how is it different?
    - What could we do if we wanted to play this game on opposite day?

### Homework

- None

### Possible Extensions

- Robozzle-like block-based puzzles
    - https://studio.code.org/s/express-2023/lessons/15/levels/3
