disk_size = 200

def CLOOK(trackNumbers, headPosition, printText = True):
	seek_count = 0
	distance = 0
	current_track = 0
	size = len(trackNumbers)

	left = []
	right = []
	seek_sequence = []

	for i in range(size):
		if (trackNumbers[i] < headPosition):
			left.append(trackNumbers[i])
		if (trackNumbers[i] > headPosition):
			right.append(trackNumbers[i])

	left.sort()
	right.sort()

	for i in range(len(right)):
		current_track = right[i]
		
		seek_sequence.append(current_track)
		distance = abs(current_track - headPosition)
		seek_count += distance
		headPosition = current_track

	seek_count += abs(headPosition - left[0])
	headPosition = left[0]

	for i in range(len(left)):
		current_track = left[i]
		seek_sequence.append(current_track)
		distance = abs(current_track - headPosition)
		seek_count += distance
		headPosition = current_track

	if printText:
		print("Total number of seek operations = ", seek_count)
		print("Seek Sequence is")

		for i in range(len(seek_sequence)):
			print(seek_sequence[i])

	return seek_count