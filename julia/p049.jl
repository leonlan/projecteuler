using Primes

function is_permutation(p, q)
    return sort(collect(string(p))) == sort(collect(string(q)))
end

function p049()
    primes = Primes.primes(1000, 9999)
    for p in primes
        if p != 1487
            for q in primes
                if p < q && is_permutation(p, q)
                    diff = q-p
                    r = q + diff
                    if isprime(r) && is_permutation(r, q)
                        return string(p) * string(q) * string(r)
                    end
                end
            end
        end
    end
end

println(p049())
