def calculate_difference(queue, headPosition, difference):
    for i in range(len(difference)):
        difference[i][0] = abs(queue[i] - headPosition) 

def find_min(difference): 
    index = -1
    minimum = 999999999
 
    for i in range(len(difference)):
        if (not difference[i][1] & minimum > difference[i][0]):
            minimum = difference[i][0]
            index = i
    return index 
     
def shortest_seek_time_first(request, headPosition, printText = True):
        if (len(request) == 0): 
            return
         
        l = len(request) 
        difference = [0] * l
         
        for i in range(l):
            difference[i] = [0, 0]
         
        seek_count = 0
         
        seek_sequence = [0] * (l + 1) 
         
        for i in range(l): 
            seek_sequence[i] = headPosition 
            calculate_difference(request, headPosition, difference) 
            index = find_min(difference) 
             
            difference[index][1] = True
             
            seek_count += difference[index][0] 
             
            headPosition = request[index] 
     
        seek_sequence[len(seek_sequence) - 1] = headPosition 
         
        if printText:
            print("Total number of seek operations =", seek_count)
            print("Seek Sequence is")

        for i in range(l + 1):
            if printText:
                print(seek_sequence[i])

        return seek_count
