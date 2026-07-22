import statistics
import numpy as np

def main():
    # 20 survey responses
    responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]
    
    # Determine and display the frequency of each rating
    print("Rating Frequencies:")
    for rating in range(1, 6):
        frequency = responses.count(rating)
        print(f"{rating}: {frequency}")
        
    print()
    
    # Calculate response statistics using built-in, statistics, and NumPy functions
    minimum = np.min(responses)          # NumPy function
    maximum = np.max(responses)          # NumPy function
    stat_range = maximum - minimum       # Range calculation
    mean = statistics.mean(responses)    # Statistics module function
    median = statistics.median(responses)# Statistics module function
    mode = statistics.mode(responses)    # Statistics module function
    
    # Section 5.17.2 uses sample variance/std (ddof=1)
    variance = np.var(responses, ddof=1) # NumPy variance with degrees of freedom
    std_dev = np.std(responses, ddof=1)  # NumPy standard deviation with degrees of freedom
    
    # Display the results
    print("Response Statistics:")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range: {stat_range}")
    print(f"Mean: {mean}")
    print(f"Median: {float(median)}")
    print(f"Mode: {mode}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_dev}")

if __name__ == '__main__':
    main()
