## Essential Questions

- How do we communicate our expectations to others?
- How do we decompose problems so they’re easy to understand?

## Lesson Plan

In this lesson, students are asked to work in pairs to create a version of
flappy bird that uses functions. To do this, we will first review functions and
reflect on how they were used in the race car game. Then, I will play flappy
in front of the students and have them identify: sprites, variables, functions.
Finally, with the reminder to design the functions first, the students will
create flappy bird.

### Setup

- `racecar_game.sb` loaded up in Scratch
- `flappy_bird.pdf` loaded up in Scratch
- `flappy_bird_skeleton.sb` loaded up in Schoology

### Lesson Plan

- Review
    - Variables
    - Functions
- PRIMM a few function things
- Race car game
    - Why did we use it
    - How did it work?
    - Show source code to show how function are being used
        - Emphasize game loop
        - "game loop on the right, functions on the left"
- Today going to create flappy bird
    - Play game to show what it looks like
    - See `flappy_bird.sb`
- Design discussion
    - What sprites did you see?
    - What variables did you see?
    - What functions do you see?
        - Abstraction: think big, fill in the details later
        - `bird_flap()`, `bird_glide()`, `pipes_reset()`
    - "game loop on the right, functions on the left... just like race cars"
    - Why design at this level
        - Think high level
        - Fill in details later
- How to test functions
    - Double click
- What should do in groups?
    - Create functions on right
    - Test functions
    - Create programs that uses functions on left
- Discuss
    - What was easy/hard?
    - What functions did you wish you had created?
    - What did this exercise show?

#### Extensions

- "Power up" / "super point" objects that randomly appear
- Make flap/glide use acceleration
    - Give them the minimal code `if (space) { speed+=1; } else { speed-=2; } change_y(speed);`
- Changing distance between pipes
