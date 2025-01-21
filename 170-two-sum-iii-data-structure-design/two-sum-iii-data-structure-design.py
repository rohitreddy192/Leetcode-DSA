class TwoSum:

    def __init__(self):
        self.s = defaultdict(int)

    def add(self, number: int) -> None:
        self.s[number] += 1

    def find(self, value: int) -> bool:
        for i,j in self.s.items():
            if value-i in self.s:
                if value-i==i:
                    if self.s[i]>1: 
                        return True
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)