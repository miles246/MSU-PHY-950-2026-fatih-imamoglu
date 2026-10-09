#!/usr/bin/env python3
"""
PHY950 Homework 2 - Master Script
Runs all solutions in sequence
"""

import subprocess
import sys
from pathlib import Path

def run_script(script_name):
    """Run a Python script and report results"""
    print(f"\n{'='*70}")
    print(f"Running {script_name}...")
    print('='*70)
    
    result = subprocess.run(
        [sys.executable, script_name],
        cwd=Path(__file__).parent,
        capture_output=False
    )
    
    if result.returncode == 0:
        print(f"✓ {script_name} completed successfully")
    else:
        print(f"✗ {script_name} failed with exit code {result.returncode}")
    
    return result.returncode == 0

def main():
    """Run all homework solutions"""
    print("\n" + "="*70)
    print("PHY950 Homework 2 - All Solutions")
    print("="*70)
    
    scripts = [
        "problem2.py",
        "problem3.py", 
        "problem4.py",
        "problem5.py",
        "problem6.py"
    ]
    
    results = {}
    for script in scripts:
        results[script] = run_script(script)
    
    # Summary
    print("\n" + "="*70)
    print("Summary")
    print("="*70)
    
    for script, success in results.items():
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"  {status}: {script}")
    
    all_passed = all(results.values())
    print("\n" + "="*70)
    if all_passed:
        print("✓ All problems completed successfully!")
    else:
        print("✗ Some problems failed. Check output above.")
    print("="*70 + "\n")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
