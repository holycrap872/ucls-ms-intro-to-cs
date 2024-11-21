## Essential Questions

- Why is plaintext information bad?
- Why is hashing necessary?

## Lesson Plan

### Setup

### Actual Lesson

- When try to create a new user with Robozzle get a warning
    - Why?
- Show how sent in plain text via the network capture
    - Why is plaintext username bad?
    - What is going on with the password?
- Called a hash
    - One way function
    - Navigate to code by looking at the event attached to the form
- Look at actual code
    - http://www.robozzle.com/beta/robozzle.js:2115
    - What is going on?
    - What's the lesson
        - Never put in useful data
        - Never put in a password you use elsewhere
- SHA cracker
    - https://crackstation.net/
    - ChangeMe -> 13d8c9009647abffee45341993ab3952f57c361d 
- Wireshark
