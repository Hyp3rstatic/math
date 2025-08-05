from sin import sin, PI
from cos import cos

#TAN WIP - MORE ADJUSTMENTS NECESSARY

def tan(rad):
  #calculate cos_val ahead of time to prevent divide by 0
  cos_val = cos(rad)

  if(cos_val == 0):
    return

  #calculate tan
  tan_val = sin(rad)/cos_val

  #account for negatives in 2nd and 4th quadrants
  rad = rad % (2*PI)
  if (rad > PI/2 and rad < PI) or rad > (3*PI)/2:
    tan_val = -1 * abs(tan_val)
  else:
    tan_val = abs(tan_val)
  
  return tan_val

#for testing
from trig_utils import *

def test_num_tan(num):
  test_num_trig(math.tan, tan, num)

#COS TESTING
if __name__ == "__main__":
  #999 on math.tan is eq to None for testing purposes
  test_key_angs_trig(math.tan, tan, "TESTING KEY TAN ANGLES:")

  test_trig_func(math.tan, "TESTING MATH.TAN TIME...")

  #time for DIY cos is even worse because of how it's built on sin
  test_trig_func(tan, "TESTING DIY TAN TIME...")

  test_trig_func(test_num_tan, "TESTING DIY TAN ACCURACY COMPARED TO MATH.TAN...")
