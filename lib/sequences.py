# sequences.py

def print_fibonacci(length):
    '''Prints a list of the Fibonacci sequence up to the specified length.'''
    if length == 0:
        print([])  # If length is 0, print an empty list and return
        return
    fibonacci_sequence = [0]  # Initialize the sequence with the first Fibonacci number
    if length == 1:
        print(fibonacci_sequence)  # If length is 1, print [0] and return
        return
    fibonacci_sequence.append(1)  # Append the second Fibonacci number to the sequence
    while len(fibonacci_sequence) < length:  # Continue generating Fibonacci numbers until the sequence reaches the specified length
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Calculate the next Fibonacci number
        fibonacci_sequence.append(next_number)  # Append the next Fibonacci number to the sequence
    print(fibonacci_sequence)  # Print the generated Fibonacci sequence
