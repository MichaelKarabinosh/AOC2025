with open('../Inputs/InputFile5', 'r') as file:
    lines = file.readlines()
newlines = []
for line in lines:
    line = line.strip('\n')
    newlines.append(line)


def fresh(intervals, num):
    for i in range(len(intervals)):
        if int(intervals[i][0]) <= num <= int(intervals[i][1]): # for each number after the intervals, check if number is < upperbound and > lowerbound for any of the intervals
            return True
    return False

def part_one():
    total = 0
    intervals = []
    for r in range(len(newlines)):
        if newlines[r] != '':
            pair = newlines[r].split('-')
            intervals.append(pair) # create a list of all the intervals
        else:
           for q in range(r+1, len(newlines)):
               if fresh(intervals, int(newlines[q])):
                   total += 1
           break
    return total

def part_two():
    interval = [] # still creating a list of all the intervals
    total = 0

    for r in range(len(newlines)):
        if newlines[r] != '':
            pair = newlines[r].split('-')
            interval.append([int(pair[0]),int(pair[1])])
            # print(interval)
        else:
            interval.sort()
            merged_intervals = merge(interval)
            break
    for merged_interval in merged_intervals:
        # print(merged_interval)
        difference = merged_interval[1] - merged_interval[0] + 1 # then just count the difference between end of interval and start of interval for each interval (+ 1 b/c inclusive)
        total += difference
    return total


def merge(interval):
    start = interval[0] # since we sorted the list we can start at interval 0
    merged_intervals = []
    for r in range(1, len(interval)):
        if interval[r][0] <= start[1] + 1: # for each interval after the first, check if the first number is less than or equal to the last number of your current interval + 1 (edge case where 4,5 6,7 works because it makes 4,7)
            if interval[r][1] > start[1]: # another edge case where if you have 4,10 and 2,3 you don't want the end of the second interval to override the larger end of the first interval
                start[1] = interval[r][1]
        else:
            merged_intervals.append(start) # otherwise add to the list of merged intervals and set start to the interval that failed to merge: start process again
            start = interval[r]
    merged_intervals.append(start)
    return merged_intervals



print('Part One:', part_one())
print('Part Two:', part_two())

