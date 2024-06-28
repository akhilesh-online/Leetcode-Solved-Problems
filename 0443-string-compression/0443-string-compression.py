class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n == 0:
            return 0
        
        # Initialize pointers for reading and writing
        read = 0
        write = 0
        
        while read < n:
            char = chars[read]
            count = 0
            
            # Count the occurances of char
            while read < n and chars[read] == char:
                count += 1
                read += 1
                
            # Write the character
            chars[write] = char
            write += 1
            
            # Write the count if it is more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        # Return the new length of the array
        return write
            