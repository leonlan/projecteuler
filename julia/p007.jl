# Little bit of a cheat, but I dont feel like writing a sieve.
using Primes

function p007(n::Int)
    return Primes.nextprime(2, n)
end

println(p007(10001))
