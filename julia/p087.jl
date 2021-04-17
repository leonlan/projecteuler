using Primes

function p087(n::Int)
    # Initialize all elements
    primes = Primes.primes(2, floor(Int, sqrt(n)))
    squares = [p^2 for p in primes if p^2 < n]
    cubes = [p^3 for p in primes if p^3 < n]
    quads = [p^4 for p in primes if p^4 < n]

    counts = Set()
    for square in squares
        for cube in cubes
            if square + cube < n
                for quad in quads
                    m = square + cube + quad
                    if m < n
                        push!(counts, m)
                    end
                end
            end
        end
    end
    return length(counts)
end

println(p087(50*10^6))
