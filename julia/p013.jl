function p013()
    fp = joinpath(@__DIR__, "../data/p013.txt")
    nums = [parse(Int128, x[1:13]) for x in readlines(fp)]
    total = sum(nums)
    return string(total)[1:10]
end

println(p013())
