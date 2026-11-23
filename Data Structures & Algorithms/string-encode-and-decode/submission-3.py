class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for i in strs:
            n = len(i)
            encoded_str += str(n) + '#' + i  # Fixed: used += instead of =
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []  # Renamed for clarity
        i = 0 

        while i < len(s):  # Fixed: changed strs to s
            j = i 
            while s[j] != '#':  # Fixed: changed strs to s
                j += 1
            length = int(s[i:j])  # Fixed: changed strs to s
            decoded_list.append(s[j+1 : j+1+length])  # Fixed: changed strs to s
            i = j + 1 + length 
            
        return decoded_list  # Fixed: added return
