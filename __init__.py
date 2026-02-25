from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # solving the edge case where either strings are null
        if not s or not t:
            return ""
        
        # improve runtime by simply returning null when t is bigger than s
        if len(t) > len(s):
            return ""
        
        # create the hashmap using counter for t and needs is the total number of characters that we need
        # to match including its duplicates
        target = Counter(t)
        needs = len(target)
        have = 0
        win_len = float('inf')

        # set the left and right pointers to 0
        # initialize the window hash map to 0 and we use it to check if our have is equal to needs
        # using Counter object here to easily track count of each alphabet
        window = Counter()
        lp =  0
        res = [0,0]

        # the stopping case is when the right pointer reaches the end of the string
        for rp in range(len(s)):
            # increment the count for the window by iterating over the right pointer
            c = s[rp]
            window[c] += 1
            print("window",window)

            # if we have a match for the character and it matches the required number
            # of repetitions for the character we increase our have by 1 as we fulfilled it
            if c in target and target[c] == window[c]:
                have += 1
            
            # if the have matches needs, we intend to find a smaller subs by decrementing from the left if possible
            # we do this by using a variable called win_len, which track the minimum possible substring length
            while (have == needs):
                if(rp-lp+1<win_len):
                    win_len = rp - lp + 1
                    res = [lp,rp]
                c = s[lp]
                # after this let's pop from the left and see if we could find a smaller substring
                window[c] -= 1
                # if the character we popped from left is in target, we decrease our haves
                if c in target and window[c] < target[c]:
                    have -= 1
                lp += 1

        lp,rp = res

        print("win_len", win_len)
        if win_len != float('inf'):
            return s[lp: rp]  # return the correct substring using lp and rp
        else:
            return ""


solution = Solution()
s = "ABCCCCC"
t = "BC"
print(solution.minWindow(s, t))
