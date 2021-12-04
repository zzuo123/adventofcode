def read_file():
	with open('12.txt', 'r') as file:
		lines = [[line[:1], int(line[1:])] for line in file]
	return lines


data = read_file()


def walk1():
	x_pos = 0
	y_pos = 0
	facing = 90  # starts off facing east
	for line in data:
		if line[0] == 'N':
			y_pos += line[1]
		elif line[0] == 'S':
			y_pos -= line[1]
		elif line[0] == 'E':
			x_pos += line[1]
		elif line[0] == 'W':
			x_pos -= line[1]
		elif line[0] == 'L':
			facing = (facing - line[1]) % 360
		elif line[0] == 'R':
			facing = (facing + line[1]) % 360
		elif line[0] == 'F':
			if facing == 0:  # north
				y_pos += line[1]
			elif facing == 90:  # east
				x_pos += line[1]
			elif facing == 180:  # south
				y_pos -= line[1]
			elif facing == 270: # west
				x_pos -= line[1]
	return abs(x_pos)+abs(y_pos)


def walk2():
	x_pos = 0
	y_pos = 0
	x_way = 10
	y_way = 1
	for line in data:
		if line[0] == 'N':
			y_way += line[1]
		elif line[0] == 'S':
			y_way -= line[1]
		elif line[0] == 'E':
			x_way += line[1]
		elif line[0] == 'W':
			x_way -= line[1]
		elif line[0] == 'L':  # clockwise -1*line[1]%360/90 times
			for i in range(int(-1*line[1]%360/90)):
				temp = x_way
				x_way = y_way
				y_way = -temp
		elif line[0] == 'R':  # clockwise line[1]%360/90 times
			for i in range(int(line[1]%360/90)):
				temp = x_way
				x_way = y_way
				y_way = -temp
		elif line[0] == 'F':
			x_pos += (line[1]*x_way)
			y_pos += (line[1]*y_way)
	return abs(x_pos)+abs(y_pos)

print(walk1())
print(walk2())