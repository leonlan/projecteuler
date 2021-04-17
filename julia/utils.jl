using Primes

"""
σ(n::Int, x::Int)

Computes the divisor function of `n` with `x`-th powers.

For more info: https://en.wikipedia.org/wiki/Divisor_function

# Examples
```julia repl
julia> σ(12, 0)
6

julia> σ(42, 1)
96
"""
function σ(n::Int, x::Int)
    total = 1

    for (p, α) in Primes.factor(n)
        if x == 0
            total *= α + 1
        else
            total *= (p ^ ((α+1) * x) - 1) ÷ (p ^ x - 1)
        end
    end

    return total
end
