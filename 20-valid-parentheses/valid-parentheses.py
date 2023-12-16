class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        inp = "({["
        oup = "]})"
        for i in s:
            if i in inp:
                st.append(i)
            if i in oup:
                if len(st)==0 or i=="]" and st[-1] != "["  or i == "}" and st[-1]!="{" or i==")" and st[-1] != "(": return False
                st.pop()
        return True if len(st) == 0 else False