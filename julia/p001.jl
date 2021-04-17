function p001(N)
    total = 0
    for i in 0:3:N-1
        if i % 5 > 0
            total += i
        end
    end
    for i in 0:5:N-1
        total += i
    end
    return total
end

println(p001(1000))
