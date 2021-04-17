function is_palindrome(n::Int)
    s = string(n)
    parity = length(s) % 2
    if s[1:end÷2] == s[end:-1:end÷2+1+parity]
        return true
    else
        return false
    end
end

function p004(n::Int)
    largest = 1
    for (i, j) in Iterators.product(1:n-1, 1:n-1)
        if is_palindrome(i * j) && i * j > largest
            largest = i * j
        end
    end
    return largest
end

println(p004(1000))
