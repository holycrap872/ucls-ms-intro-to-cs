0. What is the definition of a function:
    - Something that takes input(s) and produces an output
    - Something that takes a single input and produces multiple outputs
    - Something that produces a constant output unrelated to input(s)
    - Something that takes a set of input(s) and combines them
0. For the inputs (3, 4) the function above would say _ and for the inputs (8, 8) the function would say _
    ```
    if num_1 > num_2: "First!"
    elif num_1 < num_2: "Second!"
    else: "Same!"
    ```
0. The program below will say the numbers:
    ```
    def do_something(num_1, num_2):
        say(num_1 + num_2)

    do_something(7, 4)
    do_something(9, 0)
    do_something(6, 6)
    ```
    - 11, 9, 12
    - 74, 90, 66
    - 3, 10, 36
    - 11, 9
    - 3, 10, 14, 11
0. When run, the program below will first say the number_ and then say the number _.
    ```
    def do_something(num_1, num_2):
        say(num_1 * num_2)

    set x to 2
    set y to 5
    do_something(x, y)
    change x by -1
    change y by 4
    do_something(x, y)
    ```
0. When run, the program below will first say the number_, then the number _, and then the number _.
    ```
    def do_something(num_1):
        say(10 - num_1)

    set x to 5
    repeat 3:
        do_something(x)
        change x by -1
    ```
0. Why are functions so powerful (select the **three** that apply)?
    - They let you reuse code without copying and pasting
    - They make programs more general by using variables
    - They help organize code into logical pieces
    - They hide complicated details behind simple names
