def count_lines(f_name, skip_empty=False):
    """Counts the number of lines in a file"""
    counter = 0
    with open(f_name, "r") as FH:
        for line in FH:
            if line != "\n":
                counter += 1
            elif skip_empty == False and line == "\n":
                counter += 1
    return counter

def skip_empty_line():
    pass

def without_skip_empty_lines():
    pass

print("total count of lines:", count_lines("story.txt"))
print("total count of lines:", count_lines("story.txt", skip_empty=True))
