import re
corrupted_string = []



def process_string(corrupted_string):
    ans = 0
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, corrupted_string)
    for x, y in matches:
        ans += int(x)*int(y)
    
    return ans

def process_string_2(corrupted_string: str):
    pattern = r"don't\(\)(.*?)do\(\)"
    cleaned_string = re.sub(pattern, '', corrupted_string)

    return process_string(cleaned_string)


with open("input.txt", "r") as f:
    for line in f:
        corrupted_string .append(line.rstrip())

print(sum([process_string(line) for line in corrupted_string]))
print(sum([process_string_2("".join(corrupted_string)) ]))