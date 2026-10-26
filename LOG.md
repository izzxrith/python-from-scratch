01 - Basic

lesson 01 - variables
    - For this one i just imagine that variable is a box with a label. For instance, the box name holds the text 'Ayet'.
    - Text is called string and needs quote - whole numbers = integers while number with dot (3.5, 4.23 etc) are floats.
    - True and False = booleans, a yes or no answer
    - print makes the robot say something out loud or just print the output needed and line starting with # or """ """ is a comment. Robot ignore but its a note for a humans (us).

lesson 02 - maths 
    - maths is a calculator which means i just learn on the operator like +, -, *, / and etc
    - for this lesson i guess every operator needed to be jot down for me as i intended to learn on how to do leetcode for my improvement.

lesson 03 - strings
    - As for this, i learn on how to calc length(len), upper, lower, word[x] or use [x:y] the count not included y, split and replace.
    - I use f-string too which means anything inside {} is replaced by its value. I will use this everywhere
    - P/S : counting always starts at 0 and not 1. 

lesson 04 - if is a fork in the road
    - so for this lesson robot ask yes or no question. yes goes one way and no goes the other. only true branch runs
    - compare is == (equal), != (not equal), > , <, >=, <=
    - join question with and, or, not.
    - the colon (:) and the 4 space indent matter. indent means this line belongs inside the if.

lesson 05 - loops mean do it again
    - for repeats a know number of times
    - while repeats until the question turns to no. If it never turns to no then the loop runs forever and needed to stop with Ctrl + C
    - range (5) gives 0,1,2,3,4. It stops before 5.

    fizzbuz.py 
        - i need to check 15 first because number divisible by 15 is divisible by both 3 and 5. If i checked 3 first i would never reach FizzBuzz

lesson 06 - functions is a recipe with a name
    - i put something in (the parameter, like n). The function works
    - return hands the answer back. Write the recipe once and use it forever.
    - Tha last block (if __name__ = '__main__':) means: only run this when i run the file directly and not when another file imports it.
    - This lets tests import your functions safely.

    test_lesson06.py
        - Run pytest from the repo root. 
        - Green means your code works and red tells you exactly what broke.
        - a test is a robot that chekcs your robot.

02 - Data Structure

lesson 07 - lists are a train of boxes
    - this is where things get more complicated
    - a list keeps things in order
    - enumerate gives you the position and the value at once.
    - the list comprehension is a short way to say : make a new list from the number that pass my test.