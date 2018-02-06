passage_characters= "This is a paragraph from the book"
print(len(passage_characters))

#calculate the area of a triangle

def triangle_area(base, height):
    area= (1.0/2)*base*height
    return area

print(triangle_area(7,4))

#square function
def square(value):
    new_value=value**2
    print(new_value)

square(7)

square(float(input("Enter a value to be squared:")))
#rectangle area
def rectangle_area(length, width):
    area= length*width
    return area
print(rectangle_area(8,2))
