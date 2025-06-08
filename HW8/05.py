def count_chars(s):
    result = {}
    for huruf in s:
        if huruf in result:
            result[huruf] += 1
        else:
            result[huruf] = 1
        return result
print(count_chars("Deven Abisha"))
