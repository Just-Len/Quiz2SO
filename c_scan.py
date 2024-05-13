disk_size = 200

def c_scan(trackNumbers, headPosition, printText = True):
	seek_count = 0
	distance = 0
	cur_track = 0
	left = []
	right = []
	seek_sequence = []
	size = len(trackNumbers)

	left.append(0)
	right.append(disk_size - 1)

	for i in range(size):
		if (trackNumbers[i] < headPosition):
			left.append(trackNumbers[i])
		if (trackNumbers[i] > headPosition):
			right.append(trackNumbers[i])

	left.sort()
	right.sort()

	for i in range(len(right)):
		cur_track = right[i]

		seek_sequence.append(cur_track)

		distance = abs(cur_track - headPosition)

		seek_count += distance

		headPosition = cur_track

	headPosition = 0

	seek_count += (disk_size - 1)

	for i in range(len(left)):
		cur_track = left[i]

		seek_sequence.append(cur_track)

		distance = abs(cur_track - headPosition)

		seek_count += distance

		headPosition = cur_track

	if printText:
		print("Total number of seek operations =", seek_count)
		print("Seek Sequence is")
		print(*seek_sequence, sep="\n")

	return seek_count