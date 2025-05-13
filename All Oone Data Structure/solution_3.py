class AllOne:

    def __init__(self):
        self.d = {}
        self.aux = []

    def inc(self, key: str) -> None:
        if key in self.d.keys():
            self.d[key] += 1
            for i in range(len(self.d.keys())):
                if self.aux[i][0] == key:
                    self.aux[i][1] = self.d[key]
                    break
        else:
            self.d[key] = 1
            self.aux.append([key, 1])
        print(self.aux)
        print(self.d)

    def dec(self, key: str) -> None:
        self.d[key] -= 1
        for i in range(len(self.aux)):
            if self.aux[i][0] == key:
                self.aux[i][1] = self.d[key]

        if self.d[key] == 0:
            del self.d[key]
            for i in range(len(self.aux)):
                if self.aux[i][0] == key:
                    self.aux.pop(i)
                    break

    def getMaxKey(self) -> str:
        if not self.aux:
            return ''
        self.aux.sort(key = lambda x: x[1])
        print(self.aux)
        return self.aux[-1][0]

    def getMinKey(self) -> str:
        if not self.aux:
            return ''
        self.aux.sort(key = lambda x: x[1])
        print(self.aux)
        return self.aux[0][0]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()