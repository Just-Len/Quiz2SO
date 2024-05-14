def first_come_first_served(requestedTracks, initialHeadPosition, printText = True):
	seek_count = 0
	distance, cur_track = 0, 0
	size = len(requestedTracks)

	for i in range(size):
		cur_track = requestedTracks[i]

		distance = abs(cur_track - initialHeadPosition)

		seek_count += distance

		initialHeadPosition = cur_track
	
		if printText:
			print("Total number of seek operations = ", seek_count)
			print("Seek Sequence is")

			for i in range(size):
				print(requestedTracks[i])

	return seek_count