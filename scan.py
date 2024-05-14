disk_size = 200

def scan(trackNumbers, headPosition, direction, printText = True):
	seek_count = 0
	distance, cur_track = 0, 0
	left = []
	right = []
	seek_sequence = []
	size = len(trackNumbers)

	if (direction == "left"):
		left.append(0)
	elif (direction == "right"):
		right.append(disk_size - 1)

	for i in range(size):
		if (trackNumbers[i] < headPosition):
			left.append(trackNumbers[i])
		if (trackNumbers[i] > headPosition):
			right.append(trackNumbers[i])

	left.sort()
	right.sort()

	run = 2
	while (run != 0):
		if (direction == "left"):
			for i in range(len(left) - 1, -1, -1):
				cur_track = left[i]

				seek_sequence.append(cur_track)

				distance = abs(cur_track - headPosition)

				seek_count += distance

				headPosition = cur_track
			
			direction = "right"
	
		elif (direction == "right"):
			for i in range(len(right)):
				cur_track = right[i]
				
				seek_sequence.append(cur_track)

				distance = abs(cur_track - headPosition)

				seek_count += distance

				headPosition = cur_track
			
			direction = "left"
		
		run -= 1

	if printText:
		print("Total number of seek operations =", seek_count)
		print("Seek Sequence is")

		for i in range(len(seek_sequence)):
			print(seek_sequence[i])

	return seek_count
