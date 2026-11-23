class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            # We store: length + "#" + word
            # Example: "neet" becomes "4#neet"
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res, i = [], 0
        
        while i < len(s):
            # 1. Find the delimiter '#' to get the length
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. Extract the length and convert to integer
            length = int(s[i:j])
            
            # 3. Grab the word starting after '#'
            # The word starts at j + 1 and ends at j + 1 + length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # 4. Move the pointer to the start of the next length-prefix
            i = j + 1 + length
            
        return res