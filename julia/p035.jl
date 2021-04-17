using Primes

function is_circular_prime(p::Int)
    s = string(p)
    l = length(s)
    if '0' in s
        return false
    elseif l == 1
        return true
    else
        for i in 2:l
            rotated = s[i:end] * s[1:i-1]
            if !Primes.isprime(parse(Int, rotated))
                return false
            end
        end
        return true
    end
end


function p035(n::Int)
    primes = Primes.primes(2, n-1)
    count = 0
    for p in primes
        if is_circular_prime(p)
            count += 1
        end
    end
    return count
end

println(p035(1000000))
