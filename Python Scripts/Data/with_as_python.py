with open('abc.txt') as input_data:
    for line in input_data:
        tmpline = line.split()
        if tmpline!=[]:
            try:
                if float(tmpline[0])==13 or float(tmpline[0])==13.5 or float(tmpline[0])==14:
                    print [ float(x) for x in tmpline]
            except ValueError:
                continue
