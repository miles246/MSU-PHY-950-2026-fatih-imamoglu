#!/usr/bin/env python3
"""
PHY950 Homework 2 - Solutions
Problem 4: Expectation and Variance Properties
"""

import sympy as sp

def problem4_theoretical():
    """
    Problem 4: Show that E[ax + b] = aE[x] + b and V[ax + b] = a²V[x]
    """
    print("=" * 60)
    print("Problem 4: Properties of Expectation and Variance")
    print("=" * 60)
    
    # Define symbols
    x = sp.Symbol('x')
    a, b = sp.symbols('a b', real=True)
    pdf = sp.Function('f(x)')  # PDF of x
    
    print("\n--- Part 1: E[ax + b] = aE[x] + b ---")
    print("\nDefinition: E[g(x)] = ∫ g(x) f(x) dx")
    print("\nE[ax + b] = ∫ (ax + b) f(x) dx")
    print("           = ∫ (ax) f(x) dx + ∫ b f(x) dx")
    print("           = a ∫ x f(x) dx + b ∫ f(x) dx")
    print("           = a E[x] + b × 1")
    print("           = a E[x] + b ✓")
    
    print("\n--- Part 2: V[ax + b] = a²V[x] ---")
    print("\nDefinition: V[X] = E[(X - E[X])²] = E[X²] - (E[X])²")
    
    print("\nLet Y = ax + b")
    print("E[Y] = aE[x] + b (from Part 1)")
    
    print("\nV[ax + b] = E[(ax + b - E[ax + b])²]")
    print("           = E[(ax + b - (aE[x] + b))²]")
    print("           = E[(ax - aE[x])²]")
    print("           = E[a²(x - E[x])²]")
    print("           = a² E[(x - E[x])²]")
    print("           = a² V[x] ✓")
    
    print("\nAlternative proof using V[X] = E[X²] - (E[X])²:")
    print("\nV[ax + b] = E[(ax + b)²] - (E[ax + b])²")
    print("           = E[a²x² + 2abx + b²] - (aE[x] + b)²")
    print("           = a²E[x²] + 2abE[x] + b² - (a²(E[x])² + 2abE[x] + b²)")
    print("           = a²E[x²] + 2abE[x] + b² - a²(E[x])² - 2abE[x] - b²")
    print("           = a²(E[x²] - (E[x])²)")
    print("           = a² V[x] ✓")
    
    return True

def problem4_numeric_verification():
    """
    Numeric verification using Monte Carlo simulation
    """
    import numpy as np
    
    print("\n" + "=" * 60)
    print("Problem 4: Numeric Verification")
    print("=" * 60)
    
    np.random.seed(42)
    n_samples = 100000
    
    # Generate random x from some distribution (e.g., normal)
    x = np.random.normal(5, 2, n_samples)
    
    # Constants
    a = 3
    b = -2
    
    # Calculate expectations and variances
    E_x = np.mean(x)
    V_x = np.var(x)
    
    y = a * x + b
    E_y = np.mean(y)
    V_y = np.var(y)
    
    print(f"\nSample: n = {n_samples:,}")
    print(f"Distribution: x ~ N(5, 2²)")
    print(f"Constants: a = {a}, b = {b}")
    
    print(f"\n--- Expectation ---")
    print(f"E[x] = {E_x:.6f}")
    print(f"E[ax + b] = E[{a}x + {b}] = {E_y:.6f}")
    print(f"aE[x] + b = {a}*{E_x:.6f} + {b} = {a*E_x + b:.6f}")
    print(f"Difference: {abs(E_y - (a*E_x + b)):.2e}")
    
    print(f"\n--- Variance ---")
    print(f"V[x] = {V_x:.6f}")
    print(f"V[ax + b] = V[{a}x + {b}] = {V_y:.6f}")
    print(f"a²V[x] = {a}²*{V_x:.6f} = {a**2 * V_x:.6f}")
    print(f"Difference: {abs(V_y - (a**2 * V_x)):.2e}")
    
    print("\n✓ Numeric verification successful!")
    
    return True

if __name__ == "__main__":
    problem4_theoretical()
    problem4_numeric_verification()
    print("\n✓ Problem 4 completed successfully!")
