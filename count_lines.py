"""Counts the number of lines in a file"""
with open("story.txt", "r") as FH:
    for line in FH:
        print("the lines are::", line)
    