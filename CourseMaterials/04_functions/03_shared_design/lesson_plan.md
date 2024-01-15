## Essential Questions

- How do we communicate our expectations to others?
- How do we break down tasks so they are easily understandable?

## Lesson Plan

In this lesson, students are asked to work in pairs to create two games. The
catch is that each will only create half of each game. To do this, students
will first discuss which functions will be useful for the game. They will then
separately implement them. Then, they will exchange computers and try to use
the functions (without modification) to try and create the final game. The
point here is that they rely on the other to design the functions that they
will need. This will make them see that functions are useful abstractions
where the details of how it's implemented don't really matter.

### Setup

- `flappy_bird_skeleton.sb` loaded up in Schoology

### Lesson Plan

- Review
    - Variables
    - Functions
    - Game loop
- Today going to create flappy bird
    - Play game to show what it looks like
    - See `flappy_bird.sb`
- Describe the algorithm for gravity
    - Give them the minimal code `if (space) {speed+=1} else {speed-=2} change_y(speed)`
- Goal today:
    - Must create at least 2 functions in each sprite
        - Up to you which ones
        - Hint: Game loop functions (move, check collisions) are a good start
    - Will need:
        - Score variable
        - Speed variable
        - Use of:
            - random block
    - Extensions:
        - "Power up" / super point objects
        - Lives
        - Changing distance between pipes
        - Flap animation
- Plan:
    - Pair up
    - Discuss (5m)
    - Split (10m)
    - Swap (10m)
    - Check results (5m)
- Discuss how to test functions:
    - Just double click on them
- Allow partners to discuss with computers (without coding) for 5m
- Put partners on opposite sides of the room
    - 10m to program functions
- Switch computers
    - 10m to get game working
    - CANNOT change function code
- Come back together and see results
- Discsuss
    - What was easy/hard?
    - What functions did you wish you had created?
