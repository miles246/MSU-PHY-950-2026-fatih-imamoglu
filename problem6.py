#!/usr/bin/env python3
"""
PHY950 Homework 2 - Solutions
Problem 6: Random Number Generation using Transformation Method
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def problem6():
    """
    Problem 6: Generate random numbers according to f(x) = A sin(πx) for x ∈ [0,1]
    
    Step 1: Determine A for unit probability
    ∫₀¹ A sin(πx) dx = 1
    A [-cos(πx)/π]₀¹ = 1
    A [-cos(π)/π + cos(0)/π] = 1
    A [1/π + 1/π] = 1
    A (2/π) = 1
    A = π/2
    
    Step 2: Transformation method (Cowan Section 3.2)
    CDF: F(x) = ∫₀ˣ (π/2) sin(πt) dt = (π/2) [-cos(πt)/π]₀ˣ = (1/2)(1 - cos(πx))
    
    Set F(x) = u where u ~ Uniform(0,1):
    (1/2)(1 - cos(πx)) = u
    1 - cos(πx) = 2u
    cos(πx) = 1 - 2u
    πx = arccos(1 - 2u)
    x = (1/π) arccos(1 - 2u)
    """
    print("=" * 60)
    print("Problem 6: Random Number Generation")
    print("=" * 60)
    
    # Analytical constants
    A = np.pi / 2
    print(f"\nStep 1: Normalization constant")
    print(f"  ∫₀¹ A sin(πx) dx = 1")
    print(f"  A = π/2 = {A:.6f}")
    
    print(f"\nStep 2: Transformation method")
    print(f"  PDF: f(x) = {A:.4f} sin(πx)")
    print(f"  CDF: F(x) = (1/2)(1 - cos(πx))")
    print(f"  Inverse CDF: x = (1/π) arccos(1 - 2u)")
    
    # Generate random numbers
    np.random.seed(42)
    n_samples = 100000
    
    # Generate uniform random numbers
    u = np.random.uniform(0, 1, n_samples)
    
    # Apply transformation
    x = (1/np.pi) * np.arccos(1 - 2*u)
    
    print(f"\nStep 3: Generated {n_samples:,} samples")
    print(f"  Range: [{x.min():.6f}, {x.max():.6f}]")
    
    # Create histogram
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Histogram
    bins = np.linspace(0, 1, 50)
    hist, edges = np.histogram(x, bins=bins, density=True)
    bin_centers = 0.5 * (edges[:-1] + edges[1:])
    
    ax1.hist(x, bins=bins, density=True, alpha=0.7, color='purple', 
             edgecolor='black', label='Generated samples')
    
    # Overlay theoretical PDF
    x_theory = np.linspace(0, 1, 500)
    pdf_theory = A * np.sin(np.pi * x_theory)
    ax1.plot(x_theory, pdf_theory, 'r-', linewidth=2, label=f'f(x) = {A:.4f} sin(πx)')
    
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('PDF', fontsize=12)
    ax1.set_title('Problem 6: Generated Distribution', fontsize=14)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # CDF comparison
    sorted_x = np.sort(x)
    empirical_cdf = np.arange(1, len(sorted_x) + 1) / len(sorted_x)
    analytical_cdf = 0.5 * (1 - np.cos(np.pi * sorted_x))
    
    ax2.plot(sorted_x, empirical_cdf, 'b-', alpha=0.7, label='Empirical CDF')
    ax2.plot(sorted_x, analytical_cdf, 'r--', linewidth=2, label='Analytical CDF')
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('CDF', fontsize=12)
    ax2.set_title('CDF Comparison', fontsize=14)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/fatih/orca/projects/Homeworks/PHY950/Homework2/problem6_result.png', dpi=150)
    print(f"\nPlot saved to: problem6_result.png")
    
    # Statistics
    print(f"\nStatistics:")
    print(f"  Sample mean: {np.mean(x):.6f} (analytical: 0.5)")
    print(f"  Sample std: {np.std(x):.6f}")
    
    # Verify normalization
    # ∫ f(x) dx ≈ sum of histogram * bin_width
    bin_width = bins[1] - bins[0]
    integral = np.sum(hist) * bin_width
    print(f"\nNumerical integral of PDF: {integral:.6f} (should be 1.0)")
    
    # KS test
    from scipy.stats import kstest
    
    # Custom CDF for KS test
    def custom_cdf(x):
        return 0.5 * (1 - np.cos(np.pi * x))
    
    ks_stat, p_value = kstest(x, custom_cdf)
    print(f"\nKolmogorov-Smirnov test:")
    print(f"  KS statistic: {ks_stat:.6f}")
    print(f"  p-value: {p_value:.6f}")
    print(f"  (p > 0.05 indicates good agreement)")
    
    return x

if __name__ == "__main__":
    problem6()
    print("\n✓ Problem 6 completed successfully!")
