function p002(N)
    a, b = 1, 1
    total = 0
    while b <= N
        a, b = b, a+b
        if a % 2 == 0
            total += a
        end
    end
    return total
end

println(p002(4e6))
