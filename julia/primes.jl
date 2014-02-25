module Primes

export primes, next_prime, is_prime, eratos

primes = Set(2,3)

# returns next prime using trial division and adds it to primes
function next_prime()
    i = maximum(primes)+2
    while true
        is_prime = true
        for p in primes
            if i%p == 0
                is_prime = false
                i += 2
                break
            end
        end
        if is_prime
            push!(primes,i)
            return i
        end
    end
end

# returns if n is prime.
function is_prime(n::Int)
    i = maximum(primes)
    while i < n
        i = next_prime()
    end
    return n in primes
end

# computes all primes up to n using sieve of eratosthenes.
# returns number of primes found.
function eratos(n::Int)
    sieve = falses(n)
    for i = 2:int(sqrt(n))
        if !sieve[i]
            for j = 2*i:i:n
                sieve[j] = true
            end
        end
    end
    cnt = 0
    for i = 2:n
        if !sieve[i]
            push!(primes,i)
            cnt+=1
        end
    end
    cnt
end

end
