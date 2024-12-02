f = open("input.txt", "r")

input_list = []
for line in f:
    input_list.append(line.split())

#helper funcs
def isSafeFunc(report):
    trend = None
    isSafe = True
    report_size = len(report)

    for i in range(report_size - 1):
    
        curr = int(report[i])
        nxt = int(report[i + 1])
        diff = curr - nxt

        if diff < 0 and abs(diff) < 4: 
            if trend is not None and trend != True:
                    isSafe = False
                    break 
            trend = True
            
        elif diff > 0 and abs(diff) > 0 and abs(diff) < 4: 
            if trend is not None and trend != False:
                    isSafe = False
                    break
            trend = False
        else:
            isSafe = False
            break

    return isSafe

## part 1 ##
total_1 = 0
for report in input_list:
    if isSafeFunc(report) == True:
        total_1 += 1

print("The answer for part 1 is: " + str(total_1))

## part 2 ##
total_2 = 0

for report in input_list:
    if isSafeFunc(report):
        total_2 += 1
        continue

    isSafe = False
    for i in range(len(report)):
        reportMod = report[:i] + report[i+1:]
        if isSafeFunc(reportMod):
            isSafe = True
            break
    if isSafe:
        total_2 += 1

print("The answer for part 1 is: " + str(total_2))


    
     