using Primes

function p010(n::Int)
    return sum(Primes.primes(2, n))
end

println(p010(2*10^6-1))
