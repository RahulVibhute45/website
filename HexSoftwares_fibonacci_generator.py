#project name fibbonacci series
def fib(n):
 i=1
 Ft=0
 St=1
 print(f"first term is:{Ft} \nsecond term is:{St} ")
 while i<=n-2 :
  Tt=Ft+St
  print(f"third term is:{Tt}")
  Ft=St
  St=Tt
  i+=1
n=int(input("enter number of terms:"))
fib=fib(n)
