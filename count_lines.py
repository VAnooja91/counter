def count_lines(f_name, skip_empty=False):
    """Counts the number of lines in a file"""
    counter = 0
    with open(f_name, "r") as FH:
        for line in FH:
            if line != "\n":
                counter += 1
            elif skip_empty == False and line == "\n":
                counter += 1
            #print(counter ,repr(line))
    return counter



print("total count of lines:", count_lines("story.txt"))
print("total count of lines:", count_lines("story.txt", skip_empty=True))
