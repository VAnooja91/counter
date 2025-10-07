def count_lines():
    """Counts the number of lines in a file"""
    counter = 0
    with open("story.txt", "r") as FH:
        for line in FH:
            counter += 1
    return counter


print("total count of lines:", count_lines())
