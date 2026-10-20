'''
2.1 Homework 1 + 2 Review

1. Git vs. GitHub
    Git is a local software tool and GitHub is the cloud website.
2. Terminal vs. Command Line
    Terminal is the window where you type and display the code, the command line is the line where you type stuff in on terminal.
3. Local vs. Remote Repository
    Local repository is stored on your own computer while a remote repository is on something like GitHub.
4. Version Control
    Tracking and managing changes made to python source code files over time.
5. Staging Area
    Where changes and files sit before you save them.
6. git add
    Prepares your changed files to be saved in the staging area.
7. git commit
    Saves the changes into the local repository. 
8. git push
    Uploads saved changes to GitHub.
9. git status
    Shows the current state of your files in a Git project.
10. git pull
    Dowloads the latest changes from a remote repository and updates local project files.
11. pwd
    Will display the absolute path of the directory you are currently in.
12. ls
    Lists the contents of the directory you are in.
13. cd
    Change directories, used for moving between directories.
14. nano
    Creates a text file and opens editor.
15. touch
    Touch just creates a file. 
16. mv
    Used to move files or directories or to rename them.
17. rm
    Removes/deletes files 
18. cat
    Concatenate; allows users to quickly stream the contents of a file to the screen or redirect it to another file.


2.2 A Directory Tree

1. pwd will tell you the current working directory.
2. ls will list all files in current working directory.
3. cd ../brianna_repo
   git pull
4. mv homework.py ../judy_decal/homework
5. cd ~/python_decal/brianna_repo
6. cat homework.py
7. There were some other changes that someone did to the remote repository. Judy needs to pull those changes first before pushing, so the fix would be to say git pull before saying git push.
8. cd ~/Recents

2.3 Draw Your Directory Tree
I dont want to do that
'''

# 3.1 Data Types

def checkDataType(i):
    print(type(i))
checkDataType(3.14)

# 3.2 Conditionals
def evenOrOdd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
evenOrOdd(124)

# 4 Loops

numbers = [1, 2, 3, 4, 5]
def sumWithLoop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sumWithLoop(numbers))

# 5.1 Lists

def duplicateList(ts_list):
    result = []
    for item in ts_list:
        result.append(item)
        result.append(item)
    return result
ts_list = ["verity", "lovity", "curiosity"]
print(duplicateList(ts_list))

# 5.2 Debugging

# original:
# def square(num)
    # return num * num

# the error is that there is no colon after defining the function, which is needed here. corrected version is below.

def square(num):
    return num * num
print(square(7))

# 6.2

more_variants = ["falsity", "cruelty", "squarity"]
print(duplicateList(more_variants))
