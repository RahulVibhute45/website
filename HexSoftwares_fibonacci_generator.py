#project name fibbonacci series
def fib(n):
 i=1
 Ft=0#first term
 St=1#second term
 print(f"first term is:{Ft} \nsecond term is:{St} ")
 while i<=n-2 :
  Tt=Ft+St#third term
  print(f"third term is:{Tt}")
  Ft=St#updating values second term --->first term
  St=Tt#updating value third term --->second term
  i+=1#increment value of i by 1
n=int(input("enter number of terms:"))#taking user input outside function
fib=fib(n)#calling function
