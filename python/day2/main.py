reports = []

def check_report_safe(report):
    first = 0
    second = 1
    direction = 0
    while second < len(report):
        first_num = int(report[first])
        second_num = int(report[second])
        if first == 0:
            direction = second_num > first_num
        
        diff = abs(second_num - first_num)

        if diff <= 0 or diff > 3:
            break

        if direction == 1 and second_num < first_num:
            break

        if direction == 0 and second_num > first_num:
            break

        first += 1
        second += 1

    if second == len(report):
        return True

    return False

def check_reports_safe(reports):
    ans = 0
    for report in reports:
        if check_report_safe(report):
            ans+= 1
    
    return ans

def check_reports_safe_part_2(reports):
    ans = 0
    for report in reports:
        for i in range(len(reports)):
            new_reports = report[:i] + report[i+1:]
            if check_report_safe(new_reports):
                ans+=1
                break

    
    return ans

with open("input.txt", "r") as f:
    for line in f:
        report = line.rstrip().split(" ")
        reports.append(report)

print(check_reports_safe(reports))
print(check_reports_safe_part_2(reports))