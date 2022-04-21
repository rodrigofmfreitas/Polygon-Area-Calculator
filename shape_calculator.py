class Rectangle:

    def __init__(self, width, height):
        self.height = height
        self.width = width
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        s = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            for j in range(self.width):
                s += "*"
            s += "\n"
        return s

    def get_amount_inside(self, shape):
        amount_h = int(self.height/shape.height)
        amount_w = int(self.width/shape.width)
        return amount_h * amount_w



class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.height = side
        self.width = side