with open("Day01/Input.txt") as file:
    instruction = file.readline().strip()

floor = 0
for char in instruction:
    if char == '(':
        floor += 1
    else:
        floor -= 1


print(f'PArt 1 : The final floor is {floor}')

floor = 0
step = 0
for char in instruction:
    step += 1
    if char == '(':
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        break

print(f'Part 2 : the step that makes Santa go to the basement is {step}')