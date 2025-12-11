with open('../Inputs/InputFile11', 'r') as file:
    lines = file.readlines()
    newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)

# def domain_expansion(cur,dict,key):


dict = {}
for line in newlines:
    split = line.split(':')
    placeholder = split[1].split(' ')
    placeholder.pop(0)
    dict[split[0]] = placeholder



print(dict)