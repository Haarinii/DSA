class Solution:
    def compress(self, chars: List[str]) -> int:
         count = 1
         read = 0
         write = 0

         for i in range(1, len(chars) + 1):
             if i < len(chars) and chars[i] == chars[read]:
                count += 1
             else:
                 chars[write] = chars[read]
                 write += 1

                 if count > 1:
                     for c in str(count):
                        chars[write] = c
                        write += 1

                 read = i
                 count = 1

         return write
        

        


        