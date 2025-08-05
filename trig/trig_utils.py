import time
import math

PI = 3.141592653589793

def test_num_trig(cmprfunc, testfunc, num):
  cmpr_val = cmprfunc(num)
  diy_val = testfunc(num)
  if not cmpr_val-0.01 <= diy_val <= cmpr_val+0.01:
    print("cmpr_val: " + str(cmpr_val) + " | diy_val: " + str(diy_val))

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

def test_trig_func(func, msg):
  print(msg)
  start = time.time()
  for x in range(360*10000):
    x *= PI/180
    func(x)
  print("TEST COMPLETE")
  end = time.time()
  print("time: " + str(end - start) + '\n')
