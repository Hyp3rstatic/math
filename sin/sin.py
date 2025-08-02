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

#just giving vals in the range rn
def sin(rad):
  return (rad - (power(rad, 3)/THREE_FACTORIAL) + (power(rad, 5)/FIVE_FACTORIAL) - (power(rad, 7)/SEVEN_FACTORIAL))

print(sin(3.14/2))
