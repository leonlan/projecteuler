function p008(k)
    fp = joinpath(@__DIR__, "../data/p008.txt")
    s = [parse(Int, x) for x in join(readlines(fp))]
    largest = 0
    for i in 1:length(s)-(k-1)
        prod = reduce(*, s[i:i+(k-1)])
        largest = prod > largest ? prod : largest
    end
    return largest
end

println(p008(13))
