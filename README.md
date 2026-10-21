# python-from-scratch

I use AI a lot, but I realised I could not write code from a blank file by myself. So I am relearning programming from zero, typing every line by hand.

This repo is my daily proof of that. Every lesson, exercise and project here was typed by me, with tests, and committed as I went.

## The rules

1. Type everything myself. No copy-paste and no AI writing code.
2. Retype yesterday's work from memory for 10 minutes each day.
3. Get stuck for at least 20 minutes before asking for a hint.
4. Write a test for what I build and run it before every commit.
5. Commit every day and write two lines in `LOG.md`.

## Setup

```bash
git clone <this repo>
cd python-from-scratch
python3 -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install pytest
```

## Run things

```bash
python3 01-basics/lesson01_variables.py   # run one file
pytest                                    # run all tests
```

## Folder map

```text
01-basics/            variables, maths, strings, if, loops, functions
02-data-structures/   lists, dictionaries, sets, files, classes
03-projects/          small programs (guessing game, to-do list)
04-leetcode/          problem solving, one pattern per week
LOG.md                daily diary: what I built, what confused me
```

## Progress

### Part 1: fundamentals and problem solving (12 weeks)

- [x] Lesson 1: variables
- [x] Lesson 2: maths
- [ ] Lesson 3: strings
- [ ] Lesson 4: if
- [ ] Lesson 5: loops and FizzBuzz
- [ ] Lesson 6: functions and tests
- [ ] Lesson 7: lists
- [ ] Lesson 8: dictionaries
- [ ] Lesson 9: sets and tuples
- [ ] Lesson 10: files and errors
- [ ] Lesson 11: classes
- [ ] Project 1: guessing game
- [ ] Project 2: to-do list that saves to a file
- [ ] LeetCode: arrays and hashing, two pointers, stacks, binary search, linked lists, trees, graphs, dynamic programming

### Part 2: build real things (12 weeks)

- [ ] Python deeper, Git and Linux
- [ ] SQL with SQLite
- [ ] HTTP and a JSON API from scratch
- [ ] Login security by hand (password hashing and JWT)
- [ ] REST API with FastAPI and a database
- [ ] Docker and deploying
- [ ] Capstone: FightTrack Core API

## About me

I am Ayet, a software developer from Melaka, Malaysia.

- Portfolio: [ayet.me](https://ayet.me)
- GitHub: [izzxrith](https://github.com/izzxrith)
- LinkedIn: [muhammad-izzarith](https://linkedin.com/in/muhammad-izzarith)