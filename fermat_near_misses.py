#############################################
# Title: Fermat's Last Theorem Near Misses Finder
# File Name: fermat_near_misses.py
# External Files Needed: None
# External Files Created: near_miss_log.txt (log file containing detailed calculation logs)
# Programmers: Jahnavi Bollu, Abhinav Reddy Kommareddy
# Course: Software Engineering
# Date Submitted: 15-06
#
# Program Description:
# This program searches for "near misses" to Fermat's Last Theorem
# for user-specified values of n and k.
# It systematically tests combinations of x and y within the range [10, k]
# and calculates the relative miss for each pair.
# The program outputs any new smallest relative miss found during execution
# and logs all computations to a log file.
#
# Resources Used:
# - Python official documentation
# - StackOverflow for logging configuration and debugging advice
#############################################

import math
import logging

# Setup logging configuration
logging.basicConfig(filename='near_miss_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_near_misses(n, k):
    smallest_miss = None
    best_combination = None
    
    # Iterate over all combinations of x and y within the specified range
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            sum_powers = x ** n + y ** n
            
            # Find z such that z^n <= x^n + y^n < (z+1)^n
            z = math.floor(sum_powers ** (1 / n))
            z_power = z ** n
            z1_power = (z + 1) ** n
            
            # Calculate the miss for both z and z+1
            miss1 = sum_powers - z_power
            miss2 = z1_power - sum_powers
            miss = min(miss1, miss2)
            
            # Calculate relative miss
            relative_miss = miss / sum_powers
            
            # Log current calculations for debugging purposes
            logging.info(f"x={x}, y={y}, z={z}, miss1={miss1}, miss2={miss2}, relative_miss={relative_miss}")
            
            # Update the smallest miss if found
            if smallest_miss is None or relative_miss < smallest_miss:
                smallest_miss = relative_miss
                best_combination = (x, y, z, miss, relative_miss)
                
                # Print current best combination
                print(f"New smallest miss found: x={x}, y={y}, z={z}, "
                      f"miss={miss}, relative miss={relative_miss:.8f}")
    
    # Final result
    if best_combination:
        print("\nSmallest miss found:")
        print(f"x={best_combination[0]}, y={best_combination[1]}, z={best_combination[2]}, "
              f"miss={best_combination[3]}, relative miss={best_combination[4]:.8f}")

def main():
    print("Welcome to the Near Miss Finder for Fermat's Last Theorem.")
    n = int(input("Enter the value of n (3 <= n < 12): "))
    while not (3 <= n < 12):
        print("Invalid value. Please enter n in the range 3 <= n < 12.")
        n = int(input("Enter the value of n (3 <= n < 12): "))

    k = int(input("Enter the value of k (k > 10): "))
    while k <= 10:
        print("Invalid value. Please enter k > 10.")
        k = int(input("Enter the value of k (k > 10): "))

    calculate_near_misses(n, k)
    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
