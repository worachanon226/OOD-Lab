class palindrome:
    def __init__(self,str):
        self.isPalin(str,0,len(str)-1)

    def isPalin(self,str,l,r):
        if l == r:
            self.s = f'\'{str}\' is palindrome'
            return 
        if str[l] != str[r]:
            self.s = f'\'{str}\' is not palindrome'
            return 
        if l < r+1:
            return self.isPalin(str,l+1,r-1)
        
        self.s = f'\'{str}\' is palindrome'
        return 
    def __str__(self):
        return self.s

inp = input("Enter Input : ")
p = palindrome(inp)
print(p)