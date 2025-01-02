def perform_bitwise_operation(num1, num2, operation):
    if operation == "AND":
        return num1 & num2
    elif operation == "OR":
        return num1 | num2
    elif operation == "NOT":
        return ~num1
    elif operation == "XOR":
        return num1 ^ num2
    return None

# User input
num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
operation = input("Select Operation (AND, OR, NOT, XOR): ")

# Perform the operation
result = perform_bitwise_operation(num1, num2, operation)

# Display the result
if result is not None:
    bin1 = f'{num1:04b}'
    bin2 = f'{num2:04b}'
    result_bin = f'{result:04b}' if operation != "NOT" else f'{result & 0xFF:04b}'

    print(f"Number 1: {num1} ({bin1})")
    print(f"Number 2: {num2} ({bin2})")
    print(f"Operation: {operation}")
    print(f"Result: {result} ({result_bin})")
else:
    print("Invalid operation.")
25
