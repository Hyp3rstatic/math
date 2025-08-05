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

  #the var that will be used for calculating sin
  rad_quart = rad

  #second quad and fourth quad flipping logic
  if (rad > PI/2 and rad < PI) or (rad > (3*PI/2)):
    #correct overflip
    if rad%(PI/2) > (PI/4):
      rad_quart -= 2 * ( (rad%(PI/2)) - (PI/4) )
    #correct underflip
    if rad%(PI/2) < (PI/4):
      rad_quart += 2 * ( (PI/4) - (rad%(PI/2)) )

  #put the radian value in terms of pi/2 (effective range)
  #PI/2 and 3PI/2 have to distinguished because of PI/2 being the clock base
  if rad == PI/2 or rad == (PI*3)/2:
    rad_quart = PI/2
  else:
    rad_quart %= (PI/2) 
    #print("rad: " + str(rad)) #debug

  sin_val = (rad_quart - (power(rad_quart, 3)/THREE_FACTORIAL) + (power(rad_quart, 5)/FIVE_FACTORIAL) - (power(rad_quart, 7)/SEVEN_FACTORIAL))

  #anything over pi rad is negative (2pi is 0 with mod)
  if rad > PI:
    sin_val *= -1

  return sin_val

#libs for testing
from trig_utils import *

#SIN TESTING
if __name__ == "__main__":
  #for use in test_trig tests
  def test_num_sin(num):
    test_num_trig(math.sin, sin, num)

  #note: running math.sin and diy sin in a function speeds up code compared to running it in main
  #python function optimizations at work - applies to cos too

  test_key_angs_trig(math.sin, sin, "CALCULATING KEY SIN ANGLES:")

  test_trig_func(math.sin, "TESTING MATH.SIN TIME...")

  #time for DIY is way worse, sin in python math lib points to a compiled c bin
  test_trig_func(sin, "TESTING DIY SIN TIME...")

  test_trig_func(test_num_sin, "TESTING DIY SIN ACCURACY COMPARED TO MATH.SIN...")
