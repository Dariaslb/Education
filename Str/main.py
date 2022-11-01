class String:
    def __init__(self, st):
        if not isinstance(st, str):
            raise TypeError
        self.string = st

    def __call__(self, new_st = None):
        self.string = new_st
        return self.string

    def __add__(self, other):
        List = []
        if isinstance(other, str):
            obj = String(other)
            List.append(self.string)
            List.append(obj.string)
        else:
            List.append(self.string)
            List.append(other.string)
        return ''.join(List)



'''ob = String("")
print(ob.string)
ob("01")
print(ob.string)
ob_2 = String("22")
print(ob + ob_2)
print(ob + "333")'''

