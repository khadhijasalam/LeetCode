class Solution:
    def reverseWords(self, s: str) -> str:
        st=(s.strip()).split()
        st=[word for word in st if word!=" "]
        print(st)
        left=0
        right=len(st)-1
        while left<=right:
            st[left],st[right]=st[right],st[left]
            left+=1
            right-=1
        print(st)
        k=" ".join(st)
        print(k)
        return k
