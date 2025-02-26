def isprime(n):
     if n<2:
        return False
     for i in range(2,n):
          if n%i==0:
            return False
     return True
primenumbers=[n for n in range(2,50) if isprime(n)]
print(primenumbers)