print("Hey Dibyendu !!!")

# Print the diamond pattern
def print_diamond_pattern(n):
    # Upper half of the diamond
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
    # Lower half of the diamond
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Change 'n' to control the size of the diamond pattern
n = 10
print_diamond_pattern(n)

print("\n\n\n")
n = 20
print_diamond_pattern(n)
