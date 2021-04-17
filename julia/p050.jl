using Primes


function p050(n::Int)
    primes = Primes.primes(2, n)
    maxprime = 0
    maxlen = 1
    N = length(primes)

    for i in 1:N
        subsum = primes[i]
        sublen = 1
        j = 1
        while subsum <= n
            # Check for new candidate
            if sublen > maxlen && subsum > maxprime && Primes.isprime(subsum)
                maxprime = subsum
                maxlen = sublen
            end

            # Update the subvalues
            if i + j <= N
                subsum += primes[i+j]
                sublen += 1
                j += 1
            else
                break
            end
        end
    end

    return maxprime
end

println(p050(1000000))
