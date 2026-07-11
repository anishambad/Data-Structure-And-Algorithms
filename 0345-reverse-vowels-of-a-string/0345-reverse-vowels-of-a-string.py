class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")

        s_list = list(s)
        n = len(s_list)

        i = 0 
        j = n-1

        while i < j :
            if s_list[i] not in vowels :
                i +=1
                continue
            
            if s_list[j] not in vowels :
                j -=1
                continue

            
            s_list[i] , s_list[j] = s_list[j] , s_list[i]
            i+=1
            j-=1


        return "".join(s_list)
         
