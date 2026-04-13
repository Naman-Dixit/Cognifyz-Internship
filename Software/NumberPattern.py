n = int ( input("Enter a number: "))

# Upper Half
for i in range(1, n + 1):
    
    # Increasing numbers
    for num in range(1, i + 1):
        print(num, end=" ")
    
    # Decreasing numbers
    for num in range(i - 1, 0, -1):
        print(num, end=" ")
    
    print()

# Lower Half
for i in range(n - 1, 0, -1):
    
    # Increasing numbers
    for num in range(1, i + 1):
        print(num, end=" ")
    
    # Decreasing numbers
    for num in range(i - 1, 0, -1):
        print(num, end=" ")
    
    print()
