# TAMU Analytics 2018

This is a repo for the TAMU Analytics class of 2018 to collaborate on Python and/or R projects...or anything else you bring to the table: Scala, Java, F#, etc.

Admin contact: jbonfardeci@tamu.edu

Anacondas Python 2.7 environment: https://repo.continuum.io/archive/Anaconda2-4.3.1-Windows-x86_64.exe

Anacondas Python 3.6 environment: https://repo.continuum.io/archive/Anaconda3-4.3.1-Windows-x86_64.exe

Note: Anacondas creates an "environment" for a Python install, so you can install multiple versions side by side. This means Python and whatever 3rd-party packages you install runs in an isolated bubble. Most Python code for data science is written in 2.7 code but computer scientists use the latest 3.6 version. For whatever reasons, they did not build in backwards-compatibility like you'd expect in languages such as C# or Java.

You do not need to install multiple versions of Anacondas, just create a new environment from the Environments tab in Anaconda Navigator. 

1. Install GitHub: https://desktop.github.com

If you have a GitHub account (or need to set one up), send me your user name and I’ll make you a collaborator on the repo. 

2. Clone: Once Git is installed, you can “clone” the repo to your computer in the Git shell: 
a. Default folder should be "Documents\GitHub"
```
git clone https://github.com/jbonfardeci/tamu-analytics.git
cd tamu*
```

3. Branching: When you make changes, be sure to make a branch of the master. After you have the branch debugged working, you may merge your changes back into the master branch. 
```
git branch name_of_branch

git checkout branch_name

# make your changes, then:

git checkout master

git merge name_of_branch

git commit -m “comments”

git push (pushes changes to server)
```

For a GitHub cheat sheet: 
https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf
more hacks: https://github.com/tiimgreen/github-cheat-sheet

