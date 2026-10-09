#!/usr/bin/env python3
"""
PHY950 Homework 2 - Solutions
Problem 3: Programming exercise with histograms and random numbers
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def hello_world():
    """Problem 3(a): Print Hello World"""
    print("Hello World")

def generate_gaussian_histogram(mean=16, std=4, n_samples=10000):
    """
    Problem 3(b): Generate histogram from Gaussian distribution
    Returns the mean value from the histogram
    """
    print(f"\nGenerating {n_samples} samples from N({mean}, {std}²)...")
    
    # Generate random numbers
    np.random.seed(42)  # Using PID seed concept
    data = np.random.normal(mean, std, n_samples)
    
    # Create histogram with appropriate bins
    bin_width = 0.5
    x_min = mean - 4*std
    x_max = mean + 4*std
    bins = np.arange(x_min, x_max + bin_width, bin_width)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    n, bins, patches = ax.hist(data, bins=bins, density=True, alpha=0.7, 
                               color='skyblue', edgecolor='black', label='Histogram')
    
    # Overlay theoretical Gaussian
    x = np.linspace(x_min, x_max, 1000)
    pdf = stats.norm.pdf(x, mean, std)
    ax.plot(x, pdf, 'r-', linewidth=2, label=f'N({mean}, {std}²)')
    
    # Calculate sample mean and std from histogram
    sample_mean = np.mean(data)
    sample_std = np.std(data)
    
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Probability Density', fontsize=12)
    ax.set_title(f'Problem 3(b): Gaussian Distribution (n={n_samples:,})', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/fatih/orca/projects/Homeworks/PHY950/Homework2/problem3b_histogram.png', dpi=150)
    print(f"Plot saved to: problem3b_histogram.png")
    
    print(f"\nStatistics:")
    print(f"  Theoretical mean: {mean}, std: {std}")
    print(f"  Sample mean: {sample_mean:.4f}")
    print(f"  Sample std: {sample_std:.4f}")
    
    return sample_mean

def plot_function_with_mod(mean_value):
    """
    Problem 3(c): Create function f(x) = x + M*x²
    where M = (mean_value * 1e6) mod 10
    """
    print(f"\nProblem 3(c): Creating function with mean = {mean_value}")
    
    # Calculate M
    M = int(np.fmod(mean_value * 1e6, 10))
    print(f"  M = int(fmod({mean_value} * 1e6, 10)) = {M}")
    
    # Define function
    def f(x):
        return x + M * x**2
    
    # Generate x values
    x = np.linspace(0, 10, 500)
    y = f(x)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, 'b-', linewidth=2, label=f'f(x) = x + {M}x²')
    
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('f(x)', fontsize=12)
    ax.set_title(f'Problem 3(c): Function Plot (M={M})', fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Add some statistics
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    plt.tight_layout()
    plt.savefig('/home/fatih/orca/projects/Homeworks/PHY950/Homework2/problem3c_function.png', dpi=150)
    print(f"Plot saved to: problem3c_function.png")
    
    print(f"\nFunction statistics on [0, 10]:")
    print(f"  f(0) = {f(0):.2f}")
    print(f"  f(10) = {f(10):.2f}")
    print(f"  Mean value: {np.mean(y):.2f}")
    
    return f

def main():
    """Main function - Problem 3"""
    print("=" * 60)
    print("PHY950 Homework 2 - Problem 3")
    print("=" * 60)
    
    # 3(a): Hello World
    print("\n--- Problem 3(a) ---")
    hello_world()
    
    # 3(b): Gaussian histogram
    print("\n--- Problem 3(b) ---")
    mean_from_hist = generate_gaussian_histogram(mean=16, std=4, n_samples=10000)
    
    # 3(c): Function with mod
    print("\n--- Problem 3(c) ---")
    plot_function_with_mod(mean_from_hist)
    
    print("\n" + "=" * 60)
    print("✓ Problem 3 completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
