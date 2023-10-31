class Math:
    @staticmethod
    def add(a, b):
        return a + b
    
    def add_num(self, a, b):
        return a + b
    
m = Math()
res = m.add_num(1,2)
print(res)

print(m.add(2,3))
print(Math.add(2,3))