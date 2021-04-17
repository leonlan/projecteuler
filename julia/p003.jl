using Primes

function p003(N)
    p = 2
    remainder = N
    largest = 1
    while remainder != 1
        while remainder % p == 0
            remainder ÷= p
            largest = p
        end
        p = Primes.nextprime(p, 2)

        # Shortcut to termination
        if Primes.isprime(remainder)
            largest = remainder
            break
        end
    end
    return largest
end

println(p003(600851475143))
