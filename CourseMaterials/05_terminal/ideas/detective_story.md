Because it's in a docker image, I can load up certain programs

```
apt-get update
apt-get install vim sudo
```

docker run -v ~/out_docker:/out_docker -it harry_potter /bin/zsh

docker run  -v ./kings_cross:/kings_cross -v ./diagon_alley:/diagon_alley -v ./hogsmeade:/hogsmeade -v ./hogwarts:/hogwarts -v ./harry_home:/home/harry1 -it harry_potter /bin/zsh


Pivot:
Going to use the murder mystery theme but tweak it

Half in real world and half in digital world

MURDER!!! Mr. Rizzi's been murdered, but he left clues all over the place

ASCII art clues


Murder Mystery
- You have your trusty flash light (light shine)
- You have your trusty cat (named cat)
- A map to the crime scene

1. Get to the crime scene
- Given a map, navigate through left, right, center to get to the middle
- Once you get there, use your trusty cat to read the clue

2. Something hidden in the first turn
- Use ` -al` to make your light shine brighter
    - Two files: clue and data file
- Go see board in CS dept -> `grep "CLUE" FILE` will help you find a file
- Clue tells you next clue shows it goes to the "very top"

3. Clue hiding in /
    - diff two big files to find next clue
    - Clue tells you to go to stairwell

4. Clue in stairwell tells you about mv
  Go back into maze and `mv` a piece of the wall

3. 

Ascii Art that you have to get to the right width

10. Say "I'm done" and collect your prize


Detective going to work to solve disappearence of Mr. Rizzi
