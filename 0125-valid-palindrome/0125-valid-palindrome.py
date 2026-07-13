class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lst = list(s)

        n = len(lst)
        
        i = 0
        j = n-1

        while i < j :

            while i < j and not lst[i].isalnum() :
                i+=1

            while i < j and not lst[j].isalnum() :
                j-=1

            if lst[i].lower() != lst[j].lower():
                return False
                
            i+=1
            j-=1
        
        return True

            