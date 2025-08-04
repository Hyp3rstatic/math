#An approximation for sin
#Uses Manclaurin Series
#Range will be a quarter circle for this implementation (Half circle is standard)

def factorial(num):
  num_fac = 1;

  #return on non positive integers (excluding 0)
  if num != int(num) or num <= 0:
    return;

  #factorialing
  for x in range(num):
    num_fac *= x+1
  
  return num_fac

#only for positive int powers rn
def power(num, deg):
  if deg != int(deg) or deg < 0:
    return

  raised_num = 1

  for x in range(deg):
    raised_num *= num

  return raised_num

#for good accuracy within the first quadrant the manclaurin series will include the first 8 terms
#simplified that is: x - (x^3/3!) + (x^5/5!) - (x^7/7!)
#to save computation time factorials of 3, 5, and 7 will be stored as constants

#use of the function is redunant here, but yolo
THREE_FACTORIAL = factorial(3) #6
FIVE_FACTORIAL = factorial(5) #120
SEVEN_FACTORIAL = factorial(7) #5040

#python math.pi approximation
PI = 3.141592653589793

def sin(rad):
  #put radian value in terms of one unit circle cycle
  rad = rad % (PI*2)

  #put the radian value in terms of pi/2 (effective range)
  #PI/2 and 3PI/2 have to distinguished because of PI/2 being the clock base
  if rad == PI/2 or rad == (PI*3)/2:
    rad_quart = PI/2
  else:
    rad_quart = rad % (PI/2) 
    #print("rad: " + str(rad)) #debug

  #handle flipping logic for rad_quart based on its quadrant

  sin_val = (rad_quart - (power(rad_quart, 3)/THREE_FACTORIAL) + (power(rad_quart, 5)/FIVE_FACTORIAL) - (power(rad_quart, 7)/SEVEN_FACTORIAL))

  return sin_val

print("1: " + str(sin( PI/2 ))) #1
print("0: " + str(sin( PI ))) #0
print("-1: " + str(sin( (3*PI)/2 ))) #-1
print("0: " + str(sin( 2*PI ))) #0

print('')

print("0.7: " + str(sin( PI/4 ))) #0.7
print("0.7: " + str(sin( (3*PI)/4 ))) #0.7
print("-0.7: " + str(sin( (5*PI)/4 ))) #-0.7
print("-0.7: " + str(sin( (7*PI)/4 ))) #-0.7

print('')

print("0.86: " + str(sin( PI/3 ))) #0.86
print("0.86: " + str(sin( (2*PI)/3 ))) #0.86
print("-0.86:" + str(sin( (4*PI)/3 ))) #-0.86
print("-0.86: " + str(sin( (5*PI)/3 ))) #-0.86

print('')

print("0.5: " + str(sin( PI/6 ) )) #0.5
print("0.5: " + str(sin( (5*PI)/6 ))) #0.5
print("-0.5: " + str(sin( (7*PI)/6 ))) #-0.5
print("-0.5: " + str(sin( (11*PI)/6 ))) #-0.5

