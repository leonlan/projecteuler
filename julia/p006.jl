function p006(n::Int)
    ssq = sum([i^2 for i in 1:n])
    sqs = (n*(n+1)÷2)^2
    diff = abs(sqs-ssq)
    return diff
end

println(p006(100))
