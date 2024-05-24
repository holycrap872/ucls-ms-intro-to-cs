## Essential Questions

- How do we communicate our expectations to others?
- How do we decompose problems so they’re easy to understand?

## Lesson Plan

In this lesson, students are asked to work in pairs to create two versions of
the same game. The catch is that each will only create half of each version. To
do this, students will:

1. Discuss how to implement functions identified by the class as "core" to the game.
2. Separately implement the functions.
3. Exchange computers and use the functions (without modification) to create the final version.

The point here is that they rely on their partner to implement the functions
they will need. This will make them see that functions are useful abstractions
where the details of how it's implemented don't really matter.

> Note: a less advanced version of this would just be the students creating the functions together
> Note: a more advanced version of this would have students come up with their own functions

### Setup

- `racecar_game.sb` loaded up in Scratch
- `flappy_bird_skeleton.sb` loaded up in Schoology
- `flappy_bird.pdf` loaded up in Schoology

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
        - "Functions on the left, game loop on the right"
- Today going to create flappy bird
    - Play game to show what it looks like
    - See `flappy_bird.sb`
- Design discussion
    - What sprites did you see?
    - What variables did you see?
    - What functions do you see?
        - Abstraction: think big, fill in the details later
        - `bird_flap()`, `bird_glide()`, `pipes_reset()`
    - "Functions on the left, game loop on the right... just like race cars"
    - Why design at this level
        - Think high level
        - Fill in details later
- Discuss plan with students and iron out question:
    - Pair up
    - Discuss (5m)
    - Split and do part 1 (10m)
        - Can include animations
    - Swap and do part 2 (10m)
        - score, lives, lose screen
    - Check results (5m)
- Allow partners to discuss with computers (without coding) for 5m
- Put partners on opposite sides of the room
    - 10m to implement functions
- Switch computers
    - 10m to get game working
    - CANNOT change function code
- Come back together and see results
- Discuss
    - What was easy/hard?
    - What functions did you wish you had created?
    - What did this exercise show?

#### Extensions

- "Power up" / "super point" objects that randomly appear
- Make flap/glide use acceleration
    - Give them the minimal code `if (space) { speed+=1; } else { speed-=2; } change_y(speed);`
- Changing distance between pipes
