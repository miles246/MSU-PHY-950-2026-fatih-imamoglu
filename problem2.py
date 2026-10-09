#!/usr/bin/env python3
"""
PHY950 Homework 2 - Solutions
Problem 2: Distribution of product of two uniform random variables
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.integrate import quad

def problem2_analytical():
    """
    Problem 2(a): Show that for z = xy where x,y ~ Uniform(0,1),
    the PDF is f(z) = -ln(z) for 0 < z < 1
    
    Using Cowan equation (1.35): f(z) = ∫ g(x)h(z/x) * (1/|x|) dx
    """
    print("=" * 60)
    print("Problem 2: Distribution of z = xy where x,y ~ Uniform(0,1)")
    print("=" * 60)
    
    # The analytical PDF: f(z) = -ln(z) for 0 < z < 1
    def f_z(z):
        if 0 < z < 1:
            return -np.log(z)
        return 0
    
    # Verify it integrates to 1
    integral, error = quad(f_z, 0, 1)
    print(f"\nAnalytical PDF: f(z) = -ln(z) for 0 < z < 1")
    print(f"Integral from 0 to 1: {integral:.6f} (should be 1.0)")
    print(f"Integration error: {error:.2e}")
    
    # Generate Monte Carlo samples to verify
    np.random.seed(42)  # Using PID seed concept
    n_samples = 100000
    x = np.random.uniform(0, 1, n_samples)
    y = np.random.uniform(0, 1, n_samples)
    z = x * y
    
    # Plot histogram vs analytical
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
    
    # Histogram
    bins = np.linspace(0, 1, 50)
    hist, edges = np.histogram(z, bins=bins, density=True)
    bin_centers = 0.5 * (edges[:-1] + edges[1:])
    
    ax1.hist(z, bins=bins, density=True, alpha=0.7, label='Monte Carlo')
    z_analytical = np.linspace(0.001, 1, 100)
    ax1.plot(z_analytical, -np.log(z_analytical), 'r-', linewidth=2, label='f(z) = -ln(z)')
    ax1.set_xlabel('z')
    ax1.set_ylabel('PDF')
    ax1.set_title('Problem 2(a): PDF of z = xy')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # CDF comparison
    sorted_z = np.sort(z)
    empirical_cdf = np.arange(1, len(sorted_z) + 1) / len(sorted_z)
    analytical_cdf = lambda z: z * (1 - np.log(z)) if 0 < z < 1 else (0 if z <= 0 else 1)
    analytical_cdf_vals = [analytical_cdf(z) for z in sorted_z]
    
    ax2.plot(sorted_z, empirical_cdf, 'b-', alpha=0.7, label='Empirical CDF')
    ax2.plot(sorted_z, analytical_cdf_vals, 'r--', linewidth=2, label='Analytical CDF')
    ax2.set_xlabel('z')
    ax2.set_ylabel('CDF')
    ax2.set_title('CDF Comparison')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/fatih/orca/projects/Homeworks/PHY950/Homework2/problem2_result.png', dpi=150)
    print(f"\nPlot saved to: problem2_result.png")
    
    # Statistics
    print(f"\nMonte Carlo statistics:")
    print(f"  Mean: {np.mean(z):.6f} (analytical: 0.25)")
    print(f"  Variance: {np.var(z):.6f} (analytical: 1/18 ≈ 0.0556)")
    
    return f_z

def problem2_jacobian():
    """
    Problem 2(b): Alternative method using Jacobian
    Define z = xy, u = x
    Then x = u, y = z/u
    Jacobian: J = |∂(x,y)/∂(z,u)| = 1/u
    Joint PDF: f(z,u) = g(u)h(z/u) * (1/u) = 1 * 1 * (1/u) = 1/u
    Marginal PDF: f(z) = ∫ f(z,u) du = ∫_{z}^{1} (1/u) du = -ln(z)
    """
    print("\n" + "=" * 60)
    print("Problem 2(b): Jacobian Method")
    print("=" * 60)
    
    print("\nTransformation:")
    print("  z = xy, u = x")
    print("  Inverse: x = u, y = z/u")
    print("\nJacobian determinant:")
    print("  J = |∂(x,y)/∂(z,u)| = |det([[0, 1], [1/u, -z/u²]])| = 1/u")
    print("\nJoint PDF f(z,u):")
    print("  f(z,u) = g(u) * h(z/u) * |J| = 1 * 1 * (1/u) = 1/u")
    print("  Valid for: 0 < u < 1 and 0 < z/u < 1, i.e., z < u < 1")
    print("\nMarginal PDF f(z):")
    print("  f(z) = ∫_{z}^{1} (1/u) du = [ln(u)]_{z}^{1} = ln(1) - ln(z) = -ln(z)")
    
    return True

# Run Problem 2
if __name__ == "__main__":
    problem2_analytical()
    problem2_jacobian()
    print("\n✓ Problem 2 completed successfully!")
