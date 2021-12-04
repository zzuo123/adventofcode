with open('13.txt', 'r') as file:
	min_timestamp = int(file.readline())
	bus_timestamp = file.readline().split(',')
processed_timestamp = []
diff = []
count = 1
for i in range(len(bus_timestamp)):
	if bus_timestamp[i] != 'x':
		bus_timestamp[i] = int(bus_timestamp[i])
		processed_timestamp.append(bus_timestamp[i])
		diff.append(count)
		count = 1
	else:
		bus_timestamp[i] = 0
		count += 1
del diff[0]
bus_timestamp = processed_timestamp
# Part 1
time_list = []
for i in range(len(bus_timestamp)):
	timestamp = 0
	while timestamp < min_timestamp:
		timestamp += bus_timestamp[i]
	time_list.append(timestamp)
print((min(time_list) - min_timestamp) * bus_timestamp[time_list.index(min(time_list))])
# Part 2
'''
bus_timestamp[i] + diff[i] = bus_timestamp[i+1]
len(bus_timestamp) = len(diff) + 1
'''
final_timestamp = bus_timestamp.copy()


# make final_timestamp ascend
def routine():
	for i in range(1, len(final_timestamp)):
		while final_timestamp[i] < final_timestamp[i-1]:
			final_timestamp[i] += bus_timestamp[i]


def finder(index):
	if index == len(final_timestamp)-1:
		return final_timestamp[0]
	if final_timestamp[index] + diff[index] == final_timestamp[index+1]:
		return finder(index+1)
	else:
		final_timestamp[0] += bus_timestamp[0]
		routine()
		return finder(0)


print(finder(0))