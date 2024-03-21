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

- `flappy_bird_skeleton.sb` loaded up in Schoology
- `flappy_bird.pdf` loaded up in Schoology

### Lesson Plan

- Review
    - Variables
    - Functions
    - Game loop
    - Race car game
- Today going to create flappy bird
    - Play game to show what it looks like
    - See `flappy_bird.sb`
- Design discussion
    - What functions do you see?
        - `bird_flap()`, `bird_glide()`, `pipes_reset()`
    - What behaviors do you see in those functions?
    - Testing functions
        - Double click on them to see if they're doing what you want
        - Functions are easy to test... another reason why they're useful
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
