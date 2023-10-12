## Purpose

The theme has been that technology and magic are similar, so why not make that
explicit here.

> More and more this is seeming like a "wrap up" exercise

## Setup:

- You're Harry
- You're in terminal
- You have a trusty Cat
- You need to tell me where you're going before you go anywhere
- When you finish, you get your reward

### Materials

- Worksheet with list of personal spells learned

## The story:

1. Harry wakes up at the Dursely's
2. Next to him is a `note.txt` and `random_boot` that tells him to hurry to Diagon Alley
    - `note.txt`:
        - `cd` -> Change doors
        - `cd ~` -> Apparate home
        - `ls` -> lumos
    - `random_boot`:
        ```
        # You know a thing is a program if it's green
        # Activate a program by typing `./PROGRAM`
        # For example, activate this "Port Key" program by typing `./random_boot`
        PATH=base64(...)
        cd ${PATH}
        ```
3. Meets Hagrid at Diagon Alley
    - Prove it's you Harry, who asks him some quiz question
        - I know you've been studying a lot about abstraction lately, What is abstraction? 
    - Once gets question right, gives him next stop (Platform 9-3/4)
    - Tells him about "revelio" (`ls -al`)
    - Talking to Hargid reveals and new Port Key
4. Takes Port Key to Platform 9-3/4
    - Finds hidden platform
    - Talks to conductor who gives him a quiz before he can get on
        - What color are folders?
        - What color are files?
        - What color are programs?
        - What does `cp gold another_gold` do? (they can figure it out themselves)?
            - Joke about creating money
    - Once gets it right, takes train (`sl -f`) to Hogwarts
5. At Hogwarts, eerily quiet.
    - Maze sprung up...
    - Crumpled up piece of paper (right size terminal window) to get library clue
        - Ascii art of "Do'ye know the two Deweys? XXXX.XX.XXX" (Dewey decimal system)
    - Get 8x8 BitPic map on actual paper from Library
6. Goes through maze
    - Teach `pwd` here so can "aparate to the beginning of the maze"
    - `cd` through a series of "left", "right", "straight"
7. Meets Dumbledore who says two spirits took over castle
    - Shows spell book
    - Search through spell book with "grep"
        - I know "tab complete" will be useful, search for `tab complete`!
8. Go through main door / back gate

Main door (`rotate`, `grep`, `say`):
    - Note that says, "Un-rotate and say these words:"
    - Go back to the spell book for `rotate`
    - Spell is `say "I banish thee"`
    - Once say this, monster dead

Back gate (`rm`, `pwd`):
    - File `rock` "just a normal rock, promise there's nothing hiding under here"
    - Hidden folder
    - Morse code with hidden clue of where to go
    - Paper in CS office that says secret in your house
        - `pwd` to remember where you are
        - `cd ~`
    - Go to house, with special note
        - `rm` removes stuff
    - Go back
    - Monster shows up
    - Use `rm` to remove monster

9. Go back to Dumbledore
    - He asks a few questions
    - Gives you a program to get to a lock box
        - e.g., `Turn 90 degrees left, Walk 100 feet`
        - Go find lock box
        - Has secret spell to summon candy: Instant message teacher "we won"
        - Teacher comes over and gives candy

Missing:
- `cp`
- `mv`
- `mkdir`
- `python` -> Slytherin joke ("something like ask your snakes what this means")
- Environment variables set with `docker run` to choose between different Dewey numbers
- Use `curl` so can dynamically change stuff (e.g., dewey decimal numbers)
