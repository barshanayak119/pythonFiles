# Three sides of the triangle is a, b and c is entered by user  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  of triangle
s = (a + b + c) / 2  
  
# calculate the area  triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area) 
