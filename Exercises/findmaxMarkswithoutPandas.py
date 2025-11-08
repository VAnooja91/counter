data = {}
with open("marks.csv", 'r') as FH:
    headers = next(FH)
    for line in FH:
        fields =  line.strip().split(',')
        #print(fields)
        if fields[0] in data:
            data[fields[0]].append(fields[1])
        else:
            data[fields[0]] = [fields[1]]
    
    #print(*data.items(), sep="\n")
    
for key in data:
    print(key, max(data[key]))

