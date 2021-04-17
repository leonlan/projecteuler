using Primes

function p047(k::Int)
    count = 0
    n = 2
    while count < 4
        num_distinct_factors = length(keys(Primes.factor(n)))
        if num_distinct_factors == 4
            count += 1
        else
            count = 0
        end
        n += 1
    end
    return n-4
end

println(p047(4))
