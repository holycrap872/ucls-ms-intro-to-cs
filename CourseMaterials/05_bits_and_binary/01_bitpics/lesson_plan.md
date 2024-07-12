## Essential Questions:
- Understand how computers store and represent certain types of information

## Learning Objective:

- Understand how bits can represent color
- Be able to encode and decode simple bitmaps

## Lesson Plan

### Setup

- 4 grids from `blank_grid.docx` (2 papers front/back) per student
    - Print on "flip horizontal"
- Pencils
- Youtube videos loaded up:
    - https://www.youtube.com/watch?v=pRuRE-Bwk1U
    - https://youtu.be/fKK933KK6Gg?si=jQGR5mB67w9hWcOW&t=68

### Actual Lesson

- Reflection
    - How do computers store information?
    - What types of information do computers store?
        - numbers, text, sound, pictures, video
    - How does that become letters and numbers?
    - https://www.youtube.com/watch?v=pRuRE-Bwk1U
- Today going to talk about pictures
    - What do people know about how pictures are stored on a computer?
- Only thing computers understand: 1's and 0's
- Each picture broken down into things called pixels
    - Show in preview
    - Zoom in
    - Just a bunch of small rectangles stuck together
    - Pixel: "Picture element"
- Start easy
    - How represent black and white?
        - 0 represent black (turn lights off)
        - 1 represent white (turn lights on)
- Teacup Picture
    - Ask them if they can see what it is
    - First row would be encoded 1,1,1, ...
    - How would next row be encoded?
        - Next row is 1, 0, 0, ...
    - Missing row is encoded 1, seven 0's, 1, 1, 0, 1
- House Picture
    - Have student come up
    - decode the following for me
        - Missing rows are:
            - two 1's, one 0, seven 1's, one 0, one 1
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
- Pixels can be anything
    - What are some examples?
        - Legos
        - Paintball GPU
            - https://youtu.be/fKK933KK6Gg?si=jQGR5mB67w9hWcOW&t=68
- What is different between what we did and real pictures?

#### Homework

- Schoology assessment on BitPics
- Questions:
    1. Where does the word "pixel" come from?
        - It's a combination of the words "picture" and "element"
        - It's based on the fact that you're picking different colors
        - It's a Greek word that translates to "part of the eye"
        - It's from a patent filed in 1904 for teaching pigs to identify edible foods
    2. How many total pixels are there in an image that is 9 pixels wide and 8 pixels high?
        - 72 pixels
        - 17 pixels
        - 98 pixels
        - 103 pixels
    3. What color pixel is represented by the number 0?
        - Black
        - White
        - Orange
        - Green
    4. What color pixel is represented by the number 1?
        - White
        - Black
        - Orange
        - Blue
    5. The following list of bits ends a 6x6 picture where each pixel is represented
       by a single bit. What is it a picture of? 000000010010000000100001011110000000
        - A smile
        - A dog
        - A hockey stick
        - A cup

### Potential Extensions

- As a class, encode a BitEmoji encoder with just black and white pixels in scratch
