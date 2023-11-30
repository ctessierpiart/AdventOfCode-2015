with open("Day03/Input.txt") as file:
    directions = file.read().strip()

x, y = 0, 0
houses_delivered = [[x, y]]
for direction in directions:
    if direction == '>':
        x += 1
    elif direction == '^':
        y += 1
    elif direction == '<':
        x -= 1
    elif direction == 'v':
        y -= 1
    
    if [x, y] not in houses_delivered:
        houses_delivered.append([x, y])


print(f'Part 1 : Number of lucky houses is {len(houses_delivered)}')

santa_x, santa_y = 0, 0
robot_x, robot_y = 0, 0
houses_delivered = [[0,0]]
isSanta = True
for direction in directions:
    if isSanta:
        if direction == '>':
            santa_x += 1
        elif direction == '^':
            santa_y += 1
        elif direction == '<':
            santa_x -= 1
        elif direction == 'v':
            santa_y -= 1
        
        if [santa_x, santa_y] not in houses_delivered:
            houses_delivered.append([santa_x, santa_y])
    else:
        if direction == '>':
            robot_x += 1
        elif direction == '^':
            robot_y += 1
        elif direction == '<':
            robot_x -= 1
        elif direction == 'v':
            robot_y -= 1
        
        if [robot_x, robot_y] not in houses_delivered:
            houses_delivered.append([robot_x, robot_y])
    
    isSanta = not isSanta

print(f'Part 2 : Number of lucky houses is {len(houses_delivered)}')
