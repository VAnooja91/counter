def count_lines(f_name):
    """Counts the number of lines in a file"""
    counter = 0
    with open(f_name, "r") as FH:
        for line in FH:
            counter += 1
    return counter


print("total count of lines:", count_lines("story.txt"))
