# class Shape:
#     def __init__(self, color):
#         self.color = color

#     def display_color(self):
#         print(f"Color: {self.color}")

#     @classmethod
#     def create_shape(cls, color, type):
#         if type == "circle":
#             return Circle(color)
#         elif type == "rectangle":
#             return Rectangle(color)

# class Circle(Shape):
#     def display_shape(self):
#         print("Type: Circle")

# class Rectangle(Shape):
#     def display_shape(self):
#         print("Type: Rectangle")

# circle = Shape.create_shape("red", "circle")
# circle.display_color()  # 输出：Color: red
# circle.display_shape()  # 输出：Type: Circle

# rectangle = Shape.create_shape("blue", "rectangle")
# rectangle.display_color()  # 输出：Color: blue
# rectangle.display_shape()  # 输出：Type: Rectangle

import inspect,os

frame = inspect.stack()[0]
# module = inspect.getmodule(frame[0])
# log_name = module.__name__ if module else "default_logger"

File_Name = os.path.basename(__file__).split(".")[0]


print(File_Name)