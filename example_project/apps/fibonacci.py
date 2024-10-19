# -*- coding: utf-8 -*-

import sys

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence[:n]

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        n = int(f.read().strip())
    
    fib_sequence = fibonacci(n)
    
    with open(output_file, 'w') as f:
        f.write(', '.join(map(str, fib_sequence)))
        f.write('\n')

if __name__ == "__main__":
    main()
