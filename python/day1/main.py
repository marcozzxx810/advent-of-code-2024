
from collections import Counter


num_set1 = []
num_set2 = []

def calculate_distance(set1, set2):
    sorted_set1 = sorted(set1)
    sorted_set2 = sorted(set2)

    total_distance = 0
    for num1, num2 in zip(sorted_set1, sorted_set2):
        d = abs(int(num2)-int(num1))
        total_distance += d

    return total_distance

def calculate_similarity(set1, set2):
    mapping_set2 = Counter(set2)

    score = 0
    for num1 in set1:
        score += int(num1) * mapping_set2[num1]

    return score


with open("input.txt", "r") as f:
    for line in f:
        tmp = line.rstrip().split("   ")
        assert len(tmp) == 2
        num_set1.append(tmp[0])
        num_set2.append(tmp[1])

print(calculate_distance(num_set1, num_set2))
print(calculate_similarity(num_set1, num_set2))
