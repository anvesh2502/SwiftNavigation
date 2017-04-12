def is_prime(v) :
  
  i=2
  
  while (i*i)<=v :
    if (v%i)==0 : return False
    i+=1
  
  return True  

def print_fibonacci(n) :
  
  if n==0 : return 
  
  if n==1 : 
    print 0
    return
  
  if n==2 :
    print 0
    print 1
    return

    
  
  fib=[0]*(n+1)
  fib[0]=0
  fib[1]=1
  
  print 0 
  print 1
  
  i=2
  while i<=n :
    fib[i]=fib[i-1]+fib[i-2]
    val=fib[i]
    
    otherFlag=True
    
    if is_prime(val) :
      print 'BuzzFizz'
      otherFlag=False
    
    if val%15==0 :
      print 'FizzBuzz'
      otherFlag=False
    
    if val%5==0 :
      print 'Fizz'
      otherFlag=False
    
    if val%3==0 :
      print 'Buzz'
      otherFlag=False
      
    if  otherFlag :
      print val
    
    i+=1 


print_fibonacci(10)    
    
  