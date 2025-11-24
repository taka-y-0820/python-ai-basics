def generate_fibonacci_sequence(count: int) -> list[int]:
    """
    Return a list containing the first 'count' number of Fibonacci numbers.
    Uses an iterative approach for efficiency.
    """
    if count < 0:
        raise ValueError("The number of elements (count) must be a non-negative integer.")

    # Return an empty list if the count is zero
    if count == 0:
        return []

    sequence = []
    a, b = 0, 1
    
    # Loop 'count' times to append the first 'a' element and update the sequence
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence

def generate_pyramid_lines(sequence: list[int], depth: int) -> list[str]:
    """
    Generates a list of strings representing the centered lines 
    of the Fibonacci pyramid up to the specified depth.
    """
    if depth < 1:
        return []

    lines = []
    index = 0
    
    for row in range(1, depth + 1):
        # Calculate the required number of elements for the current row
        end_index = index + row 
        
        # Check if sequence has enough elements (robustness)
        if end_index > len(sequence):
            break 
            
        line = ' '.join(map(str, sequence[index:end_index]))
        lines.append(line)
        index = end_index
        
    return lines

def display_pyramid(lines: list[str], depth: int):
    """
    Displays the pyramid lines centered based on the maximum line length.
    """
    if not lines:
        return
        
    max_len = max(len(line) for line in lines)
    print(f"\nThe Fibonacci pyramid up to depth {depth}:")
    for line in lines:
        print(line.center(max_len))

if __name__ == "__main__":
    import sys

    # --- 1. Input Validation and Argument Parsing ---
    if len(sys.argv) != 2:
        print("Usage: python fibonacci_efficient.py <depth>")
        sys.exit(1)

    try:
        d = int(sys.argv[1])
        if d < 1:
            raise ValueError("Depth should be a positive integer.")
            
        # --- 2. Data Generation ---
        # Calculate total elements needed for a pyramid of depth d
        total_elements_needed = d * (d + 1) // 2 
        
        # Generate the required sequence
        sequence = generate_fibonacci_sequence(total_elements_needed)
        
        # Generate the pyramid lines (Separated Logic)
        lines = generate_pyramid_lines(sequence, d)
        
        # --- 3. Output ---
        display_pyramid(lines, d)
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)