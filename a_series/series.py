def fibonacci(n):
 if n ==0 or n==1:
  return n
 elif n>1:
  return fibonacci(n-1)+fibonacci(n-2)

def lucas(n):
 if n==0:
  return 2
 elif n==1:
  return 1
 else:
  return lucas(n-1)+lucas(n-2)
 


def sum_series(n,first=0,second=1):
  if first==0 and second==1:
    return fibonacci(n)
  elif first ==2 and second==1:
   return lucas(n)
  else:
   if n ==first:
    return first
   if n==second:
    return second
   else:
    return sum_series(n-1,first,second)+sum_series(n-2,first,second)
