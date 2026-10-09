#!/usr/bin/env python3
"""
PDF Math Extractor - System for extracting and understanding math from PDFs
Usage: python3 pdf_math_extractor.py <pdf_file> [--latex] [--explain]
"""

import subprocess
import sys
import argparse
from pathlib import Path

def extract_text_with_layout(pdf_path):
    """Extract text preserving layout using pdftotext"""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', str(pdf_path), '-'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting text: {e}", file=sys.stderr)
        return None

def extract_images(pdf_path, output_dir):
    """Extract images from PDF using pdfimages"""
    try:
        subprocess.run(
            ['pdfimages', '-all', str(pdf_path), str(output_dir / 'image')],
            check=True
        )
        return list(output_dir.glob('image-*'))
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("pdfimages not available or failed", file=sys.stderr)
        return []

def check_latex_available():
    """Check if LaTeX tools are available"""
    tools = ['pdflatex', 'xelatex', 'lualatex']
    available = []
    for tool in tools:
        try:
            subprocess.run(['which', tool], capture_output=True, check=True)
            available.append(tool)
        except subprocess.CalledProcessError:
            pass
    return available

def render_latex(latex_code, output_format='png'):
    """Render LaTeX code to an image"""
    # This is a placeholder - would need full LaTeX setup
    print("LaTeX rendering requires full TeX installation")
    print("Install: sudo apt-get install texlive-latex-base texlive-latex-extra")
    return None

def analyze_math_content(text):
    """Analyze text for mathematical content"""
    import re
    
    # Patterns for common math notation
    patterns = {
        'equations': r'[\$\\]([^\\$\\]+)[\$\\]',  # $...$ or \(...\)
        'fractions': r'\\frac\{([^}]+)\}\{([^}]+)\}',
        'integrals': r'\\int(?:_\{([^}]+)\})?(?:^\{([^}]+)\})?',
        'sums': r'\\sum(?:_\{([^}]+)\})?(?:^\{([^}]+)\})?',
        'greek': r'\\([a-zA-Z]+)',
        'superscripts': r'\^(\{[^}]+\}|.)',
        'subscripts': r'_(\{[^}]+\}|.)'
    }
    
    analysis = {}
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        analysis[name] = len(matches)
    
    return analysis

def main():
    parser = argparse.ArgumentParser(description='Extract and analyze math from PDFs')
    parser.add_argument('pdf_file', type=Path, help='PDF file to process')
    parser.add_argument('--latex', action='store_true', help='Check LaTeX availability')
    parser.add_argument('--explain', action='store_true', help='Explain math content')
    parser.add_argument('--output-dir', type=Path, default=Path('.'), help='Output directory')
    
    args = parser.parse_args()
    
    if not args.pdf_file.exists():
        print(f"File not found: {args.pdf_file}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Processing: {args.pdf_file}")
    print("="*60)
    
    # Extract text
    text = extract_text_with_layout(args.pdf_file)
    if text:
        print(f"\nExtracted {len(text)} characters")
        print("\n--- Content Preview ---")
        print(text[:2000] + "..." if len(text) > 2000 else text)
        
        # Analyze math content
        if args.explain:
            print("\n--- Math Content Analysis ---")
            analysis = analyze_math_content(text)
            for key, value in analysis.items():
                print(f"  {key}: {value} occurrences")
    
    # Check LaTeX
    if args.latex:
        print("\n--- LaTeX Availability ---")
        latex_tools = check_latex_available()
        if latex_tools:
            print(f"Available: {', '.join(latex_tools)}")
        else:
            print("No LaTeX engines found")
            print("Install with: sudo apt-get install texlive-latex-base texlive-latex-extra")
    
    # Extract images
    print("\n--- Extracting Images/Graphs ---")
    images = extract_images(args.pdf_file, args.output_dir)
    if images:
        print(f"Extracted {len(images)} images")
    else:
        print("No images extracted or pdfimages not available")
    
    print("\n" + "="*60)
    print("✓ Processing complete")

if __name__ == "__main__":
    main()
