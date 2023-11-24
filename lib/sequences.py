def print_fibonacci(length):
    # Handle the case where length is 0 separately
    if length == 0:
        print("Fibonacci Sequence up to length 0 : []")
        return
    # Handle the case where length is 1 separately
    elif length == 1:
        print("Fibonacci Sequence up to length 1 : [0]")
        return

    # Initialize the first two numbers in the Fibonacci sequence
    fibonacci_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    # Print the generated Fibonacci sequence in the required format
    sequence_str = ', '.join(map(str, fibonacci_sequence))
    print(f"Fibonacci Sequence up to length {length} : [{sequence_str}]")
