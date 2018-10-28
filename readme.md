## SixPillars

**SixPillars** is a program that speeds up your habit of doing the sentence completion exercises in the book Six Pillars of Self Esteem by Nathaniel Branden. 

Instead of searching for which stems you should work on this week, and searching for evening or morning stems depending on when you're doing the exercise and others, **SixPillars** allows you to use a simple python script where you only input

- how long in weeks you've been doing sentence completions
- is it morning or evening
- which pillars you would like to work on

After you input this, the program will generate a file for you, that contains all the stems that dr. Branden directly recommends to you. No more need to look them up yourself in the book! This is done using the ```sixcreate.py``` script.

The ```sixgather.py``` script is used to accumulate all that you have written in the previous week, and output a file with this information that is easy to read and is structured. This way it'll be easier for you to review what you've done this week and answer the final question of the week: "If any of what I've written this week is true, then I should ..."

### Dependencies

To run this program you need ```python3```. Download and install it from python's official page.

### Usage

You should always run these programs from the root directory of this repository.

##### Sixcreate

Sixcreate is used to generate the file containing the questions that you want.

###### Dictionary of pillars
- 1: Practice of living consciously
- 2: Practice of self-acceptance
- 3: Practice of self-responsibility
- 4: Practice of self-assertiveness
- 5: Practice of living purposefully
- 6: Practice of personal integrity

```python sixcreate.py <list of pillars you want to use> --week <week> --morning <1 if morning 0 if evening>```

- examples:

```python sixcreate.py 1 --week 2 --morning 1``` - Will generate a file with questions for the first pillar, 2nd week and for they will be morning questions.

```python sixcreate.py 1 2 3 4 --week 3 --morning 0``` - Will generate evening stems for the first 4 pillars for the 3rd week.

##### Sixgather

Sixgather is used to accumulate all that you have written for this week, and output a well formated file, so it will be easy for you to read what you've done in the previous week and answer the final question: "If any of what I've written this week is true, then I should ...".

### Usage

```python sixgather.py```
