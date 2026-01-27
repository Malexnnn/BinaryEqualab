import React, { useEffect, useRef } from 'react';
import katex from 'katex';

interface MathDisplayProps {
  expression: string;
  isResult?: boolean;
  block?: boolean;
  inline?: boolean;
  className?: string;
}

// Helper to convert calculator syntax to LaTeX
export const asciiToLatex = (input: string): string => {
  if (!input) return '';
  let latex = input;

  // 1. Basic Symbols
  latex = latex.replace(/\bpi\b/g, '\\pi');
  latex = latex.replace(/\binf\b/g, '\\infty');
  latex = latex.replace(/\btheta\b/g, '\\theta');
  latex = latex.replace(/\*/g, ' \\cdot ');
  
  // 2. Functions (prepend backslash)
  // Matches sin, cos, tan, ln, log, lim, det, but avoids things already slashed
  latex = latex.replace(/(\\|[a-zA-Z])*(sin|cos|tan|csc|sec|cot|ln|log|det|lim)/g, (match, prefix, func) => {
    if (prefix && prefix.includes('\\')) return match;
    return (prefix || '') + '\\' + func;
  });

  // 3. Integrals: integrate(f, x, a, b) -> \int_{a}^{b} f dx
  // This is a specific rendering for the history items in the demo
  if (latex.includes('integrate')) {
    // Try 4 args: integrate(expr, var, lower, upper)
    // We use a simplified regex that might fail on nested parens, but works for the demo data
    const match4 = latex.match(/integrate\(([^,]+),\s*([^,]+),\s*([^,]+),\s*([^)]+)\)/);
    if (match4) {
      return `\\int_{${asciiToLatex(match4[3])}}^{${asciiToLatex(match4[4])}} ${asciiToLatex(match4[1])} \\, d${match4[2]}`;
    }
    // Try 2 args: integrate(expr, var)
    const match2 = latex.match(/integrate\(([^,]+),\s*([^)]+)\)/);
    if (match2) {
      return `\\int ${asciiToLatex(match2[1])} \\, d${match2[2]}`;
    }
  }

  // 4. Roots: sqrt(x)
  latex = latex.replace(/sqrt\(([^)]+)\)/g, '\\sqrt{$1}');
  
  // 5. Fractions: a / b
  // Simple heuristic: if we see " / ", treat surrounding words as num/den
  // latex = latex.replace(/(\w+|\([^)]+\))\s*\/\s*(\w+|\([^)]+\))/g, '\\frac{$1}{$2}');
  
  // 6. Powers: ^
  // x^2 is fine, but formatting e^x nice
  latex = latex.replace(/e\^/g, 'e^');

  return latex;
};

const MathDisplay: React.FC<MathDisplayProps> = ({ expression, isResult = false, block = false, inline = false, className = '' }) => {
  const containerRef = useRef<HTMLElement>(null);

  useEffect(() => {
    if (containerRef.current) {
      try {
        // Convert ASCII math to LaTeX if it doesn't look like LaTeX (starts with \)
        // This heuristic allows us to pass raw LaTeX if needed
        const isRawLatex = expression.trim().startsWith('\\') || expression.includes('{');
        const textToRender = isRawLatex ? expression : asciiToLatex(expression);

        katex.render(textToRender, containerRef.current, {
          throwOnError: false,
          displayMode: block,
          macros: {
            "\\e": "\\mathrm{e}",
            "\\i": "\\mathrm{i}"
          }
        });
      } catch (err) {
        console.error("KaTeX Error:", err);
        containerRef.current.innerText = expression;
      }
    }
  }, [expression, block]);

  const Tag = inline ? 'span' : 'div';

  return (
    <Tag 
      ref={containerRef as any} 
      className={`
        ${isResult ? 'text-aurora-primary text-xl font-bold' : 'text-aurora-text/90 text-lg'} 
        ${inline ? '' : 'overflow-x-auto overflow-y-hidden'}
        ${className}
      `} 
    />
  );
};

export default MathDisplay;