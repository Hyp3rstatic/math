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

def cos(rad):
  #get sin val with phase shift
  cos_val = sin( rad + (PI/2) )

  #account for negatives on x-axis
  rad = rad % (2*PI)
  if rad > PI/2 and rad < (3*PI)/2:
    cos_val = -1 * abs(cos_val)
  if rad < PI/2 or rad > (3*PI)/2:
    cos_val = abs(cos_val)
  
  return cos_val

import math

def test_num_trig(cmprfunc, testfunc, num):
  cmpr_val = cmprfunc(num)
  diy_val = testfunc(num)
  if not cmpr_val-0.01 <= diy_val <= cmpr_val+0.01:
    print("cmpr_val: " + str(cmpr_val) + " | diy_val: " + str(diy_val))

#for use in test_trig tests
def test_num_sin(num):
  test_num_trig(math.sin, sin, num)

def test_num_cos(num):
  test_num_trig(math.cos, cos, num)

#test the accuracy of the 16 key angles for a visual unit test
def test_key_angs_trig(cmprfunc, testfunc, msg):
  print(msg)
  next_ang = 30
  for x in range(16):
    ang = PI/180 * next_ang
    #subtract from the ang for math.sin is done to avoid out of scope issues stemming from PI
    print(str(next_ang) + " | " + str(cmprfunc(ang-0.001)) + ": " + str(testfunc(ang)))
    #going to next key angle
    if (x+1) % 4 == 0 or (x+2) % 4 == 0:
      next_ang += 30
    else:
      next_ang += 15
  print('')

import time

def test_trig_func(func, msg):
  print(msg)
  start = time.time()
  for x in range(360*10000):
    x *= PI/180
    func(x)
  print("TEST COMPLETE")
  end = time.time()
  print("time: " + str(end - start) + '\n')

#SIN TESTING

#note: running math.sin and diy sin in a function speeds up code compared to running it in main
#python function optimizations at work - applies to cos too

test_key_angs_trig(math.sin, sin, "CALCULATING KEY SIN ANGLES:")

test_trig_func(math.sin, "TESTING MATH.SIN TIME...")

#time for DIY is way worse, sin in python math lib points to a compiled c bin
test_trig_func(sin, "TESTING DIY SIN TIME...")

test_trig_func(test_num_sin, "TESTING DIY SIN ACCURACY COMPARED TO MATH.SIN...")

#COS TESTING

test_key_angs_trig(math.cos, cos, "TESTING KEY COS ANGLES:")

test_trig_func(math.cos, "TESTING MATH.COS TIME...")

#time for DIY cos is even worse because of how it's built on sin
test_trig_func(cos, "TESTING DIY COS TIME...")

test_trig_func(test_num_cos, "TESTING DIY COS ACCURACY COMPARED TO MATH.COS...")
