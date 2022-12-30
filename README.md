# Style assignment

We now get to work on cultivating a pythonic style. Much of this assignment (and coding style in general)
is subjective. However, be sure to apply the principles we discussed in class, mainly following
the spirit of pep8, but don't let dogma get in the way of larger issues or even lead to making code less
readable. As always, apply your best judgement and add explanation if you think it is merited.


# Task 1: Stylize (15 points)

Examine the python file codes/task_1.py. There are several style issues. Create a pull request were you 
suggest improvements to this file. To create a pull request apply your git skills! First clone the repo 
then create a new branch. Once you are done making changes, and have commited them, push your branch back
to origin and open a PR.

hint: running a linter is a good first step (e.g., [shed](https://pypi.org/project/shed/)) but also look
for more than just cosmetic issues.


# Task 2: Modify, push (5 points)

Add your name as a markdown link with a target to your personal github page to the file "students_who_win.md".
It should look like this:

```
[Derrick Chambers](github.com/d-chambers)
```

Add the changes then commit. Make the commit message read "completed Task 1". Push the changes back 
to your fork. 

Next, paste the commit hash for the commit you just made under task 2 of answers.md. Here is an example commit hash:

b0650b0f1fe6f2b831feb162879ce50da75784be

Hint: remember git log

# Task 3: Git diff (5 points)

First, use `git branch` to see the current *local* branches. Now look at the remote branches with `git branch -a`.
The `-a` tells git to look at all branches, not just the local ones. 

Next, checkout branch_2. This will create a local copy of branch_2. Run `git branch` to verify a new local branch
named branch_2 appears in the list.

Now, use the git diff command to find the differences in *only* the file "myscript.py" between main and branch_2.
Paste the output of the command under task 3 in answers.md. What is the difference in this file? Do you suspect
merging branch_2 and main will cause a conflict? 


# Task 3: Conflict resolution (5 points) 

Next, checkout the main branch again and merge branch_2 into it. Resolve the conflict and commit. Make the commit
message read "merge branch_2 into main" and push the new commit back to your fork. Paste the commit hash in answers.md
under task_4.

# Task 4: Rebase and squash (5 points)

Next, checkout branch_1 and rebase it to main. Push the changes from branch_1 to your fork.

Hints:
 - Read the output of git rebase *carefully*, it will tell you what to do.
 - When pushing, use the force.
 - [More on rebasing](https://stackoverflow.com/a/11566503/3645626)

Now, squash all commits on branch_1 into a single commit, and push again. Paste the hash of the commit in 
the fourth task of answers.md

# Task 5: Archeology (bonus, 5 points)

A file called "secret.py" once existed in this repo. Use your git foo to find the commit hash it was created,
deleted, and the comments of the file. Post your answers in Task 5 of answers.md

# Submit PR

Finish editing answers.md. Ping the instructors with a comment that includes @instructors to let them know
you are ready for feedback. Wait. 

# More hints

If things get hopelessly mangled: ![](https://xkcd.com/1597/)
[Local and remote branches](https://stackoverflow.com/a/72156/3645626)
