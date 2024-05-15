def c_scan(trackNumbers, headPosition, printText=True):
    disk_size = 200
    seek_count = 0
    cur_track = 0
    seek_sequence = []

    left = [track for track in trackNumbers if track < headPosition]
    right = [track for track in trackNumbers if track >= headPosition]

    left.sort()
    right.sort()

    for track in right:
        seek_sequence.append(track)
        seek_count += abs(track - headPosition)
        headPosition = track

    seek_count += (disk_size - 1) - headPosition
    headPosition = 0

    for track in left:
        seek_sequence.append(track)
        seek_count += abs(track - headPosition)
        headPosition = track

    if printText:
        print("Total number of seek operations =", seek_count)
        print("Seek Sequence is")
        print(*seek_sequence, sep="\n")

    return seek_count
