# math.ceil() => Return the ceiling of x, the smallest integer grater than or equal to x. if x is not a float, delegates to x._ceil_(), which should return an integral value.
# it always return a integer  value naver a float value. 
# it rich the next value when we given a float value
import math
x=12.46
print(math.ceil(x))

# math.fabs() => it always return a positavie value
b=-23
print(math.fabs(b))

# math.factorial() => it is use show the factorial of value.
# Return c factorial as integer. Raises value error if x is not integral or is negative.
c=5
print(math.factorial(c))

# math.floor() => Return the floor of x, the largest integer less than or equal to x. if x is not a float, delegates to x._floor_(), which should return an integral value.
# it is use to show the without decimal (.) value
x= 11.5
print(math.floor(x)) # it print only 11.

# math.fsum() => return an accurate floating point sum of values in th eiterable.
# it show the sum of all list of tuple value
l=[23,65,65,34,23]
print(math.fsum(l))

# math.sqrt() => return the square root of x.
# it show the which is the square root of x. 
print(math.sqrt(34))
