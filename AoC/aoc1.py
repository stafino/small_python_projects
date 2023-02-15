

with open('aoc1.txt') as f:
    data = [row.strip() for row in f.readlines()]

calories = [sum(map(int, row.split(" "))) for row in " ".join(data).split("  ")]
print(max(calories))
print(sum(sorted(calories, reverse=True)[:3]))
