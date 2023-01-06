# Style assignment

We now get to work on cultivating a pythonic style. Much of this assignment (and coding style in general)
is arbitrary, but, as we discussed in class consistency with community guidelines is important! As you work through this assignment be sure to apply the principles we discussed in class, mainly following
the spirit of pep8. Don't let dogma mask larger issues or even lead to making code less
readable or consistent. As always, apply your best judgement and add explanation if you think it is merited.


# Task 1: Stylize (10 points)

Examine the python file task_1.py. There are several style issues. Create a pull request were you 
suggest improvements to this file. To create a pull request first clone the repo 
then create a new branch. Once you are done making changes, and have committed them, push your branch back
to origin and open a PR through the github interface.

Hint: running a linter is a good first step (e.g., [shed](https://pypi.org/project/shed/)) but also look
for more than just the cosmetic issues a program can easily detect/fix.


# Task 2: The Zen (5 points)

Create a new file called "zen.md" in this repo. Pick two of the zen of python tenants (`import this`).
For each one you picked, create a subsection and add some explanation of the principle and a good and
bad code example. Use [github-flavored markdown](https://github.github.com/gfm/) to nicely format the
document, including the examples.

If [this so post](https://stackoverflow.com/a/4568759/3645626) was an answer to this task,
it would look like this:

````markdown
# Complex is Better than Complicated

Although complex and complicated sound alike, they do not mean the same in this context.
The Zen therefore says: It is okay to build very complex applications, as long as the need for it is reasonable.

To give an example:

```python
counter = 0
while counter < 5:
   print counter
   counter += 1
```
The code is very easy to understand. It is not complex. However, it is complicated because 
you do not need to manually perform most of the steps above.

This code is complex (range actaully does quite a lot) but it's not complicated because
`range`'s interface is intuitive and well documented.  
```
for i in range(5):
   print(i)
```
````


# Task 3: Personal Style (10 points)

Look for a relatively simple python script (you can also convert a notebook to a script) you used
for your research, a class assignment, or anything really. Try to find ways to improve the script
to be more pythonic. Run a linter on it. Add the original and improved version of the script to 
this repo with clear names indicating which is which.
