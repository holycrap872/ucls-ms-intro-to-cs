## Essential Questions:

- How do computers store information?
- How do computers represent different types of information?

## Learning Objective:

- Understand how bits can represent color
- Be able to encode and decode simple bitmaps

## Lesson Plan

### Setup

- Supplies for activity
    - 4 grids from `blank_grid.docx` (2 papers front/back) per student
        - **Print on "flip horizontal"**
    - Pencils
- YouTube videos loaded up:
    - Morse code race: https://www.youtube.com/watch?v=pRuRE-Bwk1U
    - Dial up internet: https://www.youtube.com/watch?v=gsNaR6FRuO0
    - Paintball GPU: https://youtu.be/fKK933KK6Gg?si=jQGR5mB67w9hWcOW&t=68
- `Homework: Binary Information` Schoology assessment posted
    - See `assessment.md`
    - Allowed to take assessment up to two times

### Actual Lesson

- Reflection
    - How do computers store information?
    - What types of information do computers store?
        - Numbers, text, sound, pictures, video
    - How do 1's and 0's become letters and numbers?
    - Morse code race
        - https://www.youtube.com/watch?v=pRuRE-Bwk1U
        - Listen for dots and dashes
        - Can be very fast
    - Dial up internet
        - https://www.youtube.com/watch?v=gsNaR6FRuO0
        - How similar to Morse code?
            - "You can almost hear the dots and dashes as the text of a webpages is downloaded"
- Today going to talk about pictures
    - What do people know about how pictures are stored on a computer?
- Only thing computers understand: 1's and 0's
- Each picture broken down into things called pixels
    - Show in preview
    - Zoom in
    - Just a bunch of small rectangles stuck together
    - Pixel: "picture element"
- Start easy
    - How represent black and white?
        - 0 represents black (turn lights off)
        - 1 represents white (turn lights on)
- Teacup picture
    - Ask them if they can see what it is
    - First row would be encoded 1,1,1, ...
    - How would next row be encoded?
        - Next row is 1, 0, 0, ...
    - Missing row is encoded 1, seven 0's, 1, 1, 0, 1
- House Picture
    - Have student come up
    - Decode the following for me
        - Missing rows are:
            - two 1's, nine 0's, one 1
            - three 1's, seven 0's, two 1's
- Encode a 4x4 checkerboard as a class
- Now going to make our own art
    - Going to make your own black and white design on this paper
    - Encode it
    - Send it over the "internet" (teacher passing it to someone else)
    - Decode it
    - See if you came up with the right thing
- After that, bring everyone back together
- What did we learn?
    - How could you use the Morse code flashers to send picture?
- Common mistakes
    - Negative images (mixing up 1 -> white and 0 -> black)
    - Dropped bits
- Pixels can be anything
    - What are some examples?
        - Legos
        - Paintball GPU
            - https://youtu.be/fKK933KK6Gg?si=jQGR5mB67w9hWcOW&t=68
- What is difference between what we did and real pictures?

### Homework

- Schoology assessment: `Homework: Binary Information`

### Potential Extensions

- As a class, encode a BitEmoji encoder with just black and white pixels in scratch
