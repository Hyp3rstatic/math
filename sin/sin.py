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

def sin(radian):
  return  
