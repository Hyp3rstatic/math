from sin import PI, sin

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

#for testing
from trig_utils import *

def test_num_cos(num):
  test_num_trig(math.cos, cos, num)

#COS TESTING
if __name__ == "__main__":
  test_key_angs_trig(math.cos, cos, "TESTING KEY COS ANGLES:")
  
  test_trig_func(math.cos, "TESTING MATH.COS TIME...")

  #time for DIY cos is even worse because of how it's built on sin
  test_trig_func(cos, "TESTING DIY COS TIME...")

  test_trig_func(test_num_cos, "TESTING DIY COS ACCURACY COMPARED TO MATH.COS...")
