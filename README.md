# Classroom Timetable Generator

A Python 3 console program that builds a weekly class timetable from the number of days, periods per day, and the weekly periods of each subject.

PS No.: 77 | University: Rungta International Skills University | Course: B.Tech CSE

## Problem Statement
Generate a weekly timetable where the total periods equal days x periods per day. A subject can appear at most 2 times in one day. Each slot is filled with the subject that has the most periods left (if tied, the subject entered first is chosen).

## Rules
| Rule | Detail |
|------|--------|
| Days | 1 to 6 (Mon, Tue, Wed, Thu, Fri, Sat) |
| Total periods | Sum of all subject periods = days x periods per day |
| Daily limit | One subject: maximum 2 periods per day |
| Slot choice | Subject with the most periods left; tie goes to the first entered |
| Input | Only positive whole numbers |

## Concepts Used
- **Dictionary:** `subjects = {name: periods_left}` tracks remaining periods of each subject.
- **List:** `timetable` stores one list of subjects for every day.
- **Loops:** nested `for` loops (day, then slot, then subject) and a `while` loop for re-asking invalid input.
- **Function:** `get_positive_int()` validates input using `try/except`.
- **Constraints:** total check, 2-per-day limit, and a greedy choice for every slot.

## How the Program Works
1. Read days and periods per day (validated).
2. Read each subject name and its weekly periods into a dictionary.
3. Check total periods = total slots, and no subject exceeds 2 x days.
4. For every day and every slot, pick the subject with the most periods left (skip subjects already used twice that day).
5. Print the timetable day by day.

## How to Run
Requires Python 3 (no external libraries).
```
py timetable.py
```
Enter days, periods per day, number of subjects, then each subject name and its periods.

## Sample Run (Test Case 1)
```
days:3
periods:3
Number of subjects: 4
Subject name: Maths
Periods for Maths: 3
Subject name: Physics
Periods for Physics: 2
Subject name: Programming
Periods for Programming: 3
Subject name: English
Periods for English: 1
Mon: Maths, Programming, Maths
Tue: Physics, Programming, Maths
Wed: Physics, Programming, English
```

## Test Cases
| # | Scenario | Input | Expected Output | Result |
|---|----------|-------|-----------------|--------|
| 1 | Normal input | Days 3, Periods 3, Maths 3, Physics 2, Programming 3, English 1 | Mon: Maths, Programming, Maths / Tue: Physics, Programming, Maths / Wed: Physics, Programming, English | Pass |
| 2 | Boundary / minimum | Days 1, Periods 2, Maths 2 | Mon: Maths, Maths | Pass |
| 3a | Invalid: total mismatch | Days 3, Periods 3, Maths 3, Physics 2, Programming 3 | Error: Total weekly periods (8) must equal available slots (9). | Pass |
| 3b | Invalid: daily limit | Days 1, Periods 3, Maths 3 | Timetable cannot be generated: Maths needs 3 periods in 1 day, but the limit is 2 per day. | Pass |
| 4 | Different valid scenario | Days 2, Periods 2, Programming 2, English 2 | Mon: Programming, English / Tue: Programming, English | Pass |

## Input Validation
- Zero, negative numbers, text (`abc`) and decimals (`2.5`) are rejected, and the program asks again.
- Total periods and per-subject limits are checked before the timetable is built.

## Project Structure
```
class-time-table-project/
├── timetable.py   # main program
└── README.md      # documentation
```

## Possible Improvements
- Save the timetable to a text file.
- Show a table with period numbers (P1, P2, P3).
- Add teacher names for every subject.

## Author
Shivansh Tamboli | ERP No = RU-26-01061
