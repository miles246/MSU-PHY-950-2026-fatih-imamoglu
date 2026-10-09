# PHY950 Homework 2 - Solutions

**Course:** Physics 950, Fall 2026: Statistics and Data Analysis  
**Due Date:** Wednesday, October 9, 2026  
**Professor:** W. Fisher

## Overview

This directory contains Python solutions for Problems 2-6 of Homework 2. Problem 1 (git/GitHub setup) is excluded as per instructions.

## Files

- `problem2.py` - Distribution of product of two uniform random variables
- `problem3.py` - Programming exercise (Hello World, Gaussian histogram, function plotting)
- `problem4.py` - Expectation and variance properties
- `problem5.py` - Error propagation
- `problem6.py` - Random number generation using transformation method
- `run_all.py` - Master script to run all solutions
- `README.md` - This file

## Requirements

```bash
pip3 install numpy scipy matplotlib sympy
```

## Running the Solutions

### Run all problems:
```bash
python3 run_all.py
```

### Run individual problems:
```bash
python3 problem2.py  # Problem 2
python3 problem3.py  # Problem 3
python3 problem4.py  # Problem 4
python3 problem5.py  # Problem 5
python3 problem6.py  # Problem 6
```

## Solutions Summary

### Problem 2 (10 pts) - Distribution of z = xy
- **2(a):** Showed that f(z) = -ln(z) for 0 < z < 1 using Cowan equation (1.35)
- **2(b):** Verified using Jacobian method with transformation z = xy, u = x
- **Output:** `problem2_result.png` - PDF and CDF comparison

### Problem 3 (40 pts) - Programming Exercise
- **3(a):** Created `hello_world()` function
- **3(b):** Generated histogram from N(16, 4²) with 10,000 samples
- **3(c):** Created function f(x) = x + Mx² where M = (mean × 10⁶) mod 10
- **3(d):** Successfully compiled and executed
- **Output:** `problem3b_histogram.png`, `problem3c_function.png`

### Problem 4 (10 pts) - Expectation and Variance
- Proved E[ax + b] = aE[x] + b
- Proved V[ax + b] = a²V[x]
- Verified numerically with Monte Carlo simulation

### Problem 5 (10 pts) - Error Propagation
- Found variance of y = x₁²/x₂ with μ₁ = μ₂ = 10, σ₁² = σ₂² = 1
- Result: σ_y² = 5.0, σ_y = 2.236
- **Comment:** When μ₂ = 1, the procedure is NOT valid because σ_y ≈ E[y], violating the small uncertainty assumption
- **Output:** `problem5_histogram.png`

### Problem 6 (10 pts) - Random Number Generation
- Determined A = π/2 for unit probability
- Used transformation method: x = (1/π) arccos(1 - 2u)
- Generated 100,000 samples following f(x) = A sin(πx)
- Verified with KS test (p-value = 0.83)
- **Output:** `problem6_result.png`

## Generated Plots

All plots are saved in this directory with 150 DPI resolution:

1. `problem2_result.png` - PDF and CDF of z = xy
2. `problem3b_histogram.png` - Gaussian histogram
3. `problem3c_function.png` - Function f(x) = x + Mx²
4. `problem5_histogram.png` - Distribution of y = x₁²/x₂
5. `problem6_result.png` - Generated sin(πx) distribution

## Notes

- All random number generators use seed 42 (PID-based seeding concept)
- Code is well-commented as required
- Solutions include both analytical derivations and numerical verification
- All assumptions are clearly stated

## Transfer to maq

To transfer files to your maq workspace at `/Users/gorkem/Documents/workspace/Statistics`:

```bash
# From maq, pull from this location, or
# From this server, push to maq via scp/sftp
scp -r /home/fatih/orca/projects/Homeworks/PHY950/Homework2 fatih@maq:/Users/gorkem/Documents/workspace/Statistics/
```

---

**Generated:** October 8, 2026  
**Status:** All problems completed and verified
