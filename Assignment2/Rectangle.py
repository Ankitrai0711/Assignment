class Rectangle:
    def _init_(self, length: int, width: int):
        self.length = length
        self.width = width

    def _iter_(self):
        return iter([{'length': self.length}, {'width': self.width}])

if _name_ == "_main_":
    rectangle = Rectangle(12, 7)
    for i in rectangle:
        print(i)