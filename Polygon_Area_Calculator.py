from numpy import rec


class Rectangle:

    def __init__(self, width, height):
        """Make Instances for class Rectangle."""
        self.height = height
        self.width = width

    def __str__(self):
        strng = f"Rectangle(width={self.width}, height={self.height})"
        return strng

    def set_width(self, width):
        """This function will set the new width for rectangle."""
        self.width = width
        return self.width
    
    def set_height(self, height):
        """This function will set the new width for rectangle."""
        self.height = height
        return self.height

    def get_area(self):
        """This Function will return the area of Rectangle."""
        area = (self.height * self.width)
        return area

    def get_perimeter(self):
        """This Function will return the perimeter of Rectangle."""
        perimeter = (self.height * 2) + (self.width * 2)
        return perimeter

    def get_diagonal(self):
        """This Function will return the diagnals of Rectangle."""
        diagonal = ((self.height ** 2) + (self.width ** 2)) ** .5
        return diagonal

    def get_picture(self):
        """
        This function will return string representing the
        shape of Rectangle.
        """
        strng = ""
        return_strng = "Too big for picture."
        if self.height > 50 or self.width > 50:
            return return_strng
        else:
            for i in range(self.height):
                strng += ('*' * self.width) + '\n'
        return strng

    def get_amount_inside(self, shape):
        """"""
        shape_area = shape.height * shape.width
        class_area = self.height * self.width
        is_fit = class_area // shape_area
        return is_fit

class Square(Rectangle):
    """This is a subclass of Rectangle."""
    def __init__(self, side):
        """Make instances for subclass Square."""
        self.height = side
        self.width = side

    def __str__(self):
        strng = f"Square(side={self.width})"
        return strng
    
    def set_side(self, side):
        """Set the new side for square."""
        self.height = side
        self.width = side
        return self.width or self.height

rect = Rectangle(3, 6)
sq = Square(5)
# print(issubclass(Square, Rectangle))  # OK.
# print(Square is not Rectangle)  # OK.
# print(isinstance(sq, Square) and isinstance(rect, Rectangle))  # OK.
# print(rect.str())  # OK.
# print(sq.str())  # OK.
# print(rect.get_area())  # OK.
# print(sq.get_area())  # OK.
# print(rect.get_perimeter())  # OK.
# print(sq.get_perimeter())  # OK.
# print(rect.get_diagonal())  # OK.
# print(sq.get_diagonal())  # OK.
# rect.set_width(7)  # OK.
# rect.set_height(8)  # OK.
# sq.set_side(2)  # OK.
# print(rect.str())  # OK.
# print(sq.str())  # OK.
# sq.set_width(4)  # OK.
# print(sq.str())  # OK.
# rect.set_width(7)  # OK.
# rect.set_height(3)  # OK.
# print(rect.get_picture())  # OK.
# sq.set_side(2)  # OK.
# print(sq.get_picture())  # OK.
# rect.set_width(51)  # OK.
# rect.set_height(3)  # OK.
# print(rect.get_picture())  # OK.
# rect.set_height(10)  # OK.
# rect.set_width(15)  # OK.
# print(rect.get_amount_inside(sq))  # OK.
# rect2 = Rectangle(4, 8)  # OK.
# print(rect2.get_amount_inside(rect))  # OK.
# rect2 = Rectangle(2, 3)
# print(rect2.get_amount_inside(rect))  # OK.
# print(str(sq))  # OK.