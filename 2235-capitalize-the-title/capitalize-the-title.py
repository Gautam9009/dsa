class Solution():
    def capitalizeTitle(self, title):
        a = title.split()
        b =[]
        for word in a:
            if len(word) ==1 or len(word) == 2:
                x = word.lower()
                b.append(x)
            elif len(word) > 2:
                y = word.title()
                b.append(y)
        jj = " ".join(b)
        return jj
                
            
            
