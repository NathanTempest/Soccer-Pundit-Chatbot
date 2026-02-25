def bitonic_sequence(seq, key):
    #Given a bitonic sequence, to find if an element exists or not.
    #First find the pivot - the point where the increasing sequence ends and decreasing sequence begins
    pivot = 0
    l = 0
    r = len(seq) - 1
    while l <= r:
        mid = (l + r)//2
        #do a spot check if this matches the key
        if seq[mid] == key:
            return True
        #check that the two elements on either side of mid are in bounds
        if mid > 0 and mid < len(seq) - 1:
            if seq[mid] > seq[mid - 1] and seq[mid] > seq[mid + 1]:
                #this is the pivot condition
                pivot =  mid
                break
            if seq[mid] > seq[mid - 1] and seq[mid] < seq[mid + 1]:
                #we are in an increasing sequence
                l = mid + 1
            if seq[mid] < seq[mid - 1] and seq[mid] > seq[mid + 1]:
                #we are in a decreasing sequence
                r = mid - 1
    #if the key is greater than the pivot, then both the sequences cannot contain the key, return False
    if key > seq[pivot]:
        return False
    def find_incr(seq, key, pivot):
        l = 0
        r = pivot
        while l <= r:
            mid = (l + r)//2
            if seq[mid] == key:
                return True
            if seq[mid] < key:
                #key might be in 2nd half
                l = mid + 1
            elif seq[mid] > key:
                #key might be in 1st half
                r = mid - 1
         #failed to find the key in the increasing sequence
        return False
    def find_decr(seq, key, pivot):
        l = pivot
        r = len(seq) - 1
        while l <= r:
            mid = (l + r)//2
            if seq[mid] == key:
                return True
            if seq[mid] < key:
                #key might be in 1st half
                r = mid - 1
            elif seq[mid] > key:
                #key might be in 2nd half
                l = mid + 1
         #failed to find the key in the increasing sequence
        return False
    #if the key is in either half, return True, else False
    return find_incr(seq, key, pivot) or find_decr(seq, key, pivot)

seq = [1,2,3,4,5,4,3,2,1]
key = 4
print("Should return True", bitonic_sequence(seq, key))
key = 16
print("Should return False", bitonic_sequence(seq, key))
