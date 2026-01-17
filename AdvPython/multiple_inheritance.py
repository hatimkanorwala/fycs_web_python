class abc:
    def __init__(self):
        print("Constructor called of class ABC")
        super().__init__()
class defg:
    def __init__(self):
        print("Constructor called of class DEFG")
class ghi(abc,defg):
    def __init__(self):
        print("Constructor called of class GHI")
        super().__init__()

obj = ghi()
