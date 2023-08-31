#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0  # Class attribute to keep track of instances
    print_symbol = '#'  # Default print symbol
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property        
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
           raise ValueError("height must be >= 0")
        self.__height = value
        
    def area(self):
        a = self.__width *self.__height
        return a
    def perimeter(self):
        if self.__width==0 or self.__height == 0:
            p = 0
        else:
            p=2*(self.__height + self.__width)
        return p
    
    
    def __str__(self):
        return self.rect()
    def __repr__(self):
        return f"Rectangle({self.__height}, {self.__width})"        
        
    def rect(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        
        result = ""
        for _ in range(self.__height):
            if isinstance(self.print_symbol, list):
                # If print_symbol is a list, join its elements into a string
                symbol = "".join(map(str, self.print_symbol))
            else:
                symbol = self.print_symbol
            
            result += symbol * self.__width + "\n"
        return result
        
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -=1
    @staticmethod    
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.width * rect_1.height
        area_2 = rect_2.width * rect_2.height
        if area_1 >= area_2:
            return area_1
        else:
            return area_2
    @classmethod
    def square(cls, size=0):
        return cls(size, size)             



my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
