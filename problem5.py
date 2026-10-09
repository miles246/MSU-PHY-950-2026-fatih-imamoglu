#!/usr/bin/env python3
"""
PHY950 Homework 2 - Solutions
Problem 5: Error Propagation
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, simplify

def problem5_analytical():
    """
    Problem 5: Error propagation for y = x₁²/x₂
    Given: μ₁ = μ₂ = 10, σ₁² = σ₂² = 1
    
    Error propagation formula:
    σ_y² = (∂y/∂x₁)² σ₁² + (∂y/∂x₂)² σ₂²
    """
    print("=" * 60)
    print("Problem 5: Error Propagation")
    print("=" * 60)
    
    # Define symbols
    x1, x2 = symbols('x1 x2')
    
    # Function y = x₁²/x₂
    y = x1**2 / x2
    
    print(f"\nFunction: y = x₁²/x₂ = {y}")
    
    # Calculate partial derivatives
    dy_dx1 = diff(y, x1)
    dy_dx2 = diff(y, x2)
    
    print(f"\nPartial derivatives:")
    print(f"  ∂y/∂x₁ = {dy_dx1}")
    print(f"  ∂y/∂x₂ = {dy_dx2}")
    
    # Given parameters
    mu1 = 10
    mu2 = 10
    sigma1_sq = 1
    sigma2_sq = 1
    
    print(f"\nGiven parameters:")
    print(f"  μ₁ = {mu1}, μ₂ = {mu2}")
    print(f"  σ₁² = {sigma1_sq}, σ₂² = {sigma2_sq}")
    
    # Evaluate derivatives at the mean
    dy_dx1_val = float(dy_dx1.subs({x1: mu1, x2: mu2}))
    dy_dx2_val = float(dy_dx2.subs({x1: mu1, x2: mu2}))
    
    print(f"\nDerivatives evaluated at (μ₁, μ₂):")
    print(f"  ∂y/∂x₁|_(μ₁,μ₂) = {dy_dx1_val}")
    print(f"  ∂y/∂x₂|_(μ₁,μ₂) = {dy_dx2_val}")
    
    # Error propagation
    sigma_y_sq = (dy_dx1_val**2) * sigma1_sq + (dy_dx2_val**2) * sigma2_sq
    sigma_y = np.sqrt(sigma_y_sq)
    
    print(f"\nError propagation:")
    print(f"  σ_y² = (∂y/∂x₁)² σ₁² + (∂y/∂x₂)² σ₂²")
    print(f"       = ({dy_dx1_val})² × {sigma1_sq} + ({dy_dx2_val})² × {sigma2_sq}")
    print(f"       = {dy_dx1_val**2 * sigma1_sq} + {dy_dx2_val**2 * sigma2_sq}")
    print(f"       = {sigma_y_sq}")
    print(f"\n  σ_y = √{sigma_y_sq} = {sigma_y:.6f}")
    
    # Expected value of y
    mu_y = mu1**2 / mu2
    print(f"\nExpected value:")
    print(f"  E[y] = μ₁²/μ₂ = {mu1}²/{mu2} = {mu_y}")
    
    print(f"\nResult: y = {mu_y} ± {sigma_y:.6f}")
    
    return sigma_y_sq

def problem5_mu2_equals_1():
    """
    Comment on validity when μ₂ = 1
    """
    print("\n" + "=" * 60)
    print("Problem 5: Validity when μ₂ = 1")
    print("=" * 60)
    
    mu1 = 10
    mu2_new = 1
    sigma1_sq = 1
    sigma2_sq = 1
    
    print(f"\nNew parameters: μ₁ = {mu1}, μ₂ = {mu2_new}")
    
    # Partial derivatives at new means
    dy_dx1_val = 2 * mu1 / mu2_new  # = 20
    dy_dx2_val = -mu1**2 / mu2_new**2  # = -100
    
    print(f"\nPartial derivatives at (μ₁, μ₂):")
    print(f"  ∂y/∂x₁ = 2x₁/x₂ = {dy_dx1_val}")
    print(f"  ∂y/∂x₂ = -x₁²/x₂² = {dy_dx2_val}")
    
    # Error propagation
    sigma_y_sq_new = (dy_dx1_val**2) * sigma1_sq + (dy_dx2_val**2) * sigma2_sq
    
    print(f"\nVariance:")
    print(f"  σ_y² = ({dy_dx1_val})² × 1 + ({dy_dx2_val})² × 1")
    print(f"       = {dy_dx1_val**2} + {dy_dx2_val**2}")
    print(f"       = {sigma_y_sq_new}")
    print(f"  σ_y = {np.sqrt(sigma_y_sq_new):.2f}")
    
    print(f"\nExpected value: E[y] = {mu1}²/{mu2_new} = {mu1**2/mu2_new}")
    
    print("\n" + "-" * 60)
    print("Comment on validity:")
    print("-" * 60)
    print("""
The error propagation formula assumes:
1. Small uncertainties (σ << μ)
2. Linear approximation is valid
3. Variables are independent

When μ₂ = 1:
- The derivative ∂y/∂x₂ = -100 is very large
- σ_y ≈ 100, which is comparable to E[y] = 100
- This violates the "small uncertainty" assumption
- The linear approximation breaks down
- Higher-order terms become significant
- The actual distribution of y will be highly skewed
- Error propagation formula gives unreliable results

Conclusion: The procedure is NOT valid when μ₂ = 1 because
the relative uncertainty is too large, and the linear
approximation underlying error propagation fails.
""")
    
    return sigma_y_sq_new

def problem5_monte_carlo():
    """
    Monte Carlo verification
    """
    print("\n" + "=" * 60)
    print("Problem 5: Monte Carlo Verification (μ₂ = 10)")
    print("=" * 60)
    
    np.random.seed(42)
    n_samples = 100000
    
    # Generate samples
    x1 = np.random.normal(10, 1, n_samples)
    x2 = np.random.normal(10, 1, n_samples)
    y = x1**2 / x2
    
    # Statistics
    mean_y = np.mean(y)
    var_y = np.var(y)
    std_y = np.std(y)
    
    print(f"\nMonte Carlo results (n = {n_samples:,}):")
    print(f"  E[y] ≈ {mean_y:.6f} (analytical: 10)")
    print(f"  V[y] ≈ {var_y:.6f} (analytical: 4.25)")
    print(f"  σ_y ≈ {std_y:.6f}")
    
    # Compare with analytical
    analytical_var = 4.25
    print(f"\nComparison:")
    print(f"  Variance difference: {abs(var_y - analytical_var):.6f}")
    print(f"  Relative error: {abs(var_y - analytical_var)/analytical_var*100:.2f}%")
    
    # Plot histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(y, bins=100, density=True, alpha=0.7, color='green', edgecolor='black')
    ax.axvline(mean_y, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_y:.2f}')
    ax.axvline(10, color='blue', linestyle=':', linewidth=2, label='Analytical Mean = 10')
    ax.set_xlabel('y', fontsize=12)
    ax.set_ylabel('PDF', fontsize=12)
    ax.set_title('Problem 5: Distribution of y = x₁²/x₂', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/fatih/orca/projects/Homeworks/PHY950/Homework2/problem5_histogram.png', dpi=150)
    print(f"\nPlot saved to: problem5_histogram.png")
    
    return var_y

if __name__ == "__main__":
    var1 = problem5_analytical()
    var2 = problem5_mu2_equals_1()
    var_mc = problem5_monte_carlo()
    print("\n✓ Problem 5 completed successfully!")
