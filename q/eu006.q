/ The sum of the squares of the first ten natural numbers is:
/    1^(2) + 2^(2) + ... + 10^(2) = 385
sumsq:{(+/)x*x}
385=sumsq 1+til 10
/ The square of the sum of the first ten natural numbers is:
/     (1 + 2 + ... + 10)^(2) = 55^(2) = 3025
sqsum:{a:(+/)x;a*a}
3025=sqsum 1+til 10
/ Find the difference between the sum of the squares of the first one
/ hundred natural numbers and the square of the sum.
ns:1+til 100
sqsum[ns]-sumsq[ns]
