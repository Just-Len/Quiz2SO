disk_size = 200

def scan(trackNumbers, headPosition, direction, printText=True):
    seek_count = 0
    distance, cur_track = 0, 0
    seek_sequence = []

    left = [track for track in trackNumbers if track < headPosition]
    right = [track for track in trackNumbers if track >= headPosition]

    left.sort(reverse=True)
    right.sort()


    if direction == "left":
        tracks = left + [0] + right
    elif direction == "right":
        tracks = right + [disk_size - 1] + left

    for track in tracks:
        seek_sequence.append(track)
        distance = abs(track - headPosition)
        seek_count += distance
        headPosition = track

    if printText:
        print("Total number of seek operations =", seek_count)
        print("Seek Sequence is")
        for track in seek_sequence:
            print(track)

    return seek_count
