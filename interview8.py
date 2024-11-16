# print 1 to 100 without loop 
def print_numbers(n=1):
    if n > 100:
        return
    print(n)
    print_numbers(n + 1)

print_numbers()