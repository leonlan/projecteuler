using Primes

"""
The smallest multiple can be computed as the smallest
necessary prime multiplicities for each of the divisors.
"""
function p005(n::Int)
    multiplicity = Dict{Integer,Integer}(1=>1)
    for i in 2:n
        factors = Primes.factor(i)
        for (k, v) in factors
            old = get(multiplicity, k, 0)
            # Update multiplicity if not enough
            multiplicity[k] = v > old ? v : old
        end
    end
    smallest_multiple = Primes.prodfactors(multiplicity)
    return smallest_multiple
end


println(p005(20))
