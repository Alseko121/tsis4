def even(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input())

even_nums = even(n)
print(",".join(str(num) for num in even_nums))
#even numbers
