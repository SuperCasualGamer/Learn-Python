class Burmese:
    def __init__(self, val: int = 0, tail: "Burmese" = None):
        self.val = val
        self.tail = tail
    
    def hiss() -> str:
        return "Hiss"

if __name__ == '__main__':
    Samke = Burmese(1, Burmese(2, Burmese(3)))
    Cloen = Samke
    while Cloen is not None:
        print(Cloen.val)
        Cloen = Cloen.tail