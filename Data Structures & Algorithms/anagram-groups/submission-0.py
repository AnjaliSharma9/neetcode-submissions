
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        res = defaultdict(list)

        # 2. Start looping through every word in the input list
        for s in strs:
            # 3. Sort the characters and join them back into a string
            sorted_s = "".join(sorted(s))
            
            # 4. Use that sorted string as a key and add the original word to its list
            res[sorted_s].append(s)
        
        # 5. Extract all the groups from the dictionary
        return list(res.values())