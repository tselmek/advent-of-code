from statistics import median


lines = [line.rstrip("\n") for line in open("input.txt")]

CORRUPTED_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

AUTOCOMPLETE_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

CLOSING = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score = 0
corrupted_lines = []

for k, line in enumerate(lines):
    stack = []
    k = 0
    while k < len(line):
        if line[k] in "({[<":
            stack.append(line[k])
        else:
            if line[k] == CLOSING[stack[-1]]:
                stack.pop(-1)
            else:
                score += CORRUPTED_POINTS[line[k]]
                corrupted_lines.append(line)
                break 
        k += 1

print(score)

for line in corrupted_lines:
    lines.pop(lines.index(line))

scores = []

for incomplete_line in lines:
    stack = []
    k = 0
    while k < len(incomplete_line):
        if incomplete_line[k] in "({[<":
            stack.append(incomplete_line[k])
        else:
            if incomplete_line[k] == CLOSING[stack[-1]]:
                stack.pop(-1)
        k += 1
    score = 0
    while len(stack) > 0:
        score = score * 5 + AUTOCOMPLETE_POINTS[CLOSING[stack.pop(-1)]]
    scores.append(score)

print(median(scores))

