/ all primes up to x, calculated with sieve of eratosthenes
primes:{
 p:(x+1)#1b;
 {x>y*y}[x]{p[1_y*1+til floor x%y]:0b;y+1}[x]\2;
 where p=1}
