function p022()
    # Read file and clean
    fi = readlines(joinpath(@__DIR__, "../data/p022.txt"))
    sorted_names = sort([strip(n, '"') for n in split(fi[1], ",")])

    # Compute name scores
    total = 0
    capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    D = Dict{Char,Int}(c => i for (i, c) in enumerate(capitals))
    for (position, name) in enumerate(sorted_names)
        total += position * sum([D[c] for c in name])
    end
    return total
end

println(p022())
