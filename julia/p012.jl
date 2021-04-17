using Primes
include("utils.jl")


function p012(d::Int)
    triangle = 1
    i = 2
    while σ(triangle, 0) < d
        triangle += i
        i += 1
    end
    return triangle
end

println(p012(500))
