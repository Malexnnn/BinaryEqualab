import React, { useState, useCallback } from 'react';
import { Plus, Minus, RotateCcw, Copy } from 'lucide-react';
import MathDisplay from './MathDisplay';
import apiService from '../services/apiService';

interface MatrixState {
    rows: number;
    cols: number;
    values: string[][];
}

const createEmptyMatrix = (rows: number, cols: number): string[][] => {
    return Array(rows).fill(null).map(() => Array(cols).fill('0'));
};

const MatrixMode: React.FC = () => {
    const [matrixA, setMatrixA] = useState<MatrixState>({
        rows: 3,
        cols: 3,
        values: [['4', '-2', '1'], ['0', '5', '-1'], ['3', '8', '2']]
    });

    const [matrixB, setMatrixB] = useState<MatrixState>({
        rows: 3,
        cols: 1,
        values: [['1'], ['0'], ['-5']]
    });

    const [results, setResults] = useState<Array<{ command: string; result: string }>>([]);
    const [loading, setLoading] = useState(false);

    const matrixToString = (m: MatrixState): string => {
        return `Matrix([${m.values.map(row => `[${row.join(',')}]`).join(',')}])`;
    };

    const updateMatrixValue = (
        matrix: 'A' | 'B',
        row: number,
        col: number,
        value: string
    ) => {
        const setter = matrix === 'A' ? setMatrixA : setMatrixB;
        const current = matrix === 'A' ? matrixA : matrixB;

        const newValues = [...current.values];
        newValues[row] = [...newValues[row]];
        newValues[row][col] = value;

        setter({ ...current, values: newValues });
    };

    const resizeMatrix = (matrix: 'A' | 'B', newRows: number, newCols: number) => {
        const setter = matrix === 'A' ? setMatrixA : setMatrixB;
        const current = matrix === 'A' ? matrixA : matrixB;

        const newValues = createEmptyMatrix(newRows, newCols);
        for (let r = 0; r < Math.min(current.rows, newRows); r++) {
            for (let c = 0; c < Math.min(current.cols, newCols); c++) {
                newValues[r][c] = current.values[r]?.[c] || '0';
            }
        }

        setter({ rows: newRows, cols: newCols, values: newValues });
    };

    const executeOperation = async (operation: string) => {
        setLoading(true);
        try {
            let expr = '';
            let displayCmd = operation;

            switch (operation) {
                case 'det(A)':
                    expr = `${matrixToString(matrixA)}.det()`;
                    break;
                case 'inv(A)':
                    expr = `${matrixToString(matrixA)}.inv()`;
                    break;
                case 'transpose(A)':
                    expr = `${matrixToString(matrixA)}.T`;
                    break;
                case 'eigenvals(A)':
                    expr = `${matrixToString(matrixA)}.eigenvals()`;
                    break;
                case 'A × B':
                    expr = `${matrixToString(matrixA)} * ${matrixToString(matrixB)}`;
                    displayCmd = 'A * B';
                    break;
                case 'rref(A)':
                    expr = `${matrixToString(matrixA)}.rref()`;
                    break;
                default:
                    expr = operation;
            }

            const response = await apiService.simplify(expr);
            setResults(prev => [...prev, { command: displayCmd, result: response.result || response.latex || 'Error' }]);
        } catch (error: any) {
            setResults(prev => [...prev, { command: operation, result: `Error: ${error.message}` }]);
        } finally {
            setLoading(false);
        }
    };

    const clearResults = () => setResults([]);

    const MatrixEditor = ({
        label,
        matrix,
        matrixKey
    }: {
        label: string;
        matrix: MatrixState;
        matrixKey: 'A' | 'B'
    }) => (
        <div className="bg-background-light rounded-xl border border-aurora-border overflow-hidden flex flex-col">
            <div className="px-4 py-3 border-b border-aurora-border bg-background-dark flex justify-between items-center">
                <div className="flex items-center gap-3">
                    <div className={`size-8 rounded ${matrixKey === 'A' ? 'bg-primary/20 text-primary' : 'bg-white/10 text-white'} flex items-center justify-center font-bold font-mono`}>
                        {label}
                    </div>
                    <span className="font-bold text-white">Matrix {label}</span>
                </div>
                <div className="flex items-center gap-2">
                    <button
                        onClick={() => resizeMatrix(matrixKey, Math.max(1, matrix.rows - 1), matrix.cols)}
                        className="p-1 hover:bg-white/10 rounded text-aurora-muted"
                        title="Remove row"
                    >
                        <Minus size={14} />
                    </button>
                    <span className="text-xs text-aurora-muted font-mono">{matrix.rows} × {matrix.cols}</span>
                    <button
                        onClick={() => resizeMatrix(matrixKey, matrix.rows + 1, matrix.cols)}
                        className="p-1 hover:bg-white/10 rounded text-aurora-muted"
                        title="Add row"
                    >
                        <Plus size={14} />
                    </button>
                </div>
            </div>
            <div className="p-6 flex items-center justify-center bg-background min-h-[200px]">
                <div className="flex relative before:absolute before:inset-y-0 before:-left-3 before:w-3 before:border-2 before:border-r-0 before:border-white/20 before:rounded-l-lg after:absolute after:inset-y-0 after:-right-3 after:w-3 after:border-2 after:border-l-0 after:border-white/20 after:rounded-r-lg">
                    <div
                        className="grid gap-2"
                        style={{ gridTemplateColumns: `repeat(${matrix.cols}, minmax(0, 1fr))` }}
                    >
                        {matrix.values.flatMap((row, r) =>
                            row.map((val, c) => (
                                <input
                                    key={`${r}-${c}`}
                                    type="text"
                                    value={val}
                                    onChange={(e) => updateMatrixValue(matrixKey, r, c, e.target.value)}
                                    className="w-14 h-12 bg-background-dark border border-aurora-border rounded text-center text-white font-mono focus:border-primary focus:ring-1 focus:ring-primary transition-all"
                                />
                            ))
                        )}
                    </div>
                </div>
            </div>
            <div className="px-4 py-2 border-t border-aurora-border bg-background-dark flex justify-end gap-2">
                <button
                    onClick={() => resizeMatrix(matrixKey, matrix.rows, Math.max(1, matrix.cols - 1))}
                    className="text-xs text-aurora-muted hover:text-white"
                >
                    - Col
                </button>
                <button
                    onClick={() => resizeMatrix(matrixKey, matrix.rows, matrix.cols + 1)}
                    className="text-xs text-aurora-muted hover:text-white"
                >
                    + Col
                </button>
            </div>
        </div>
    );

    return (
        <div className="flex flex-col h-full bg-background p-6 lg:p-10 overflow-y-auto">
            <div className="max-w-6xl mx-auto w-full flex flex-col gap-6">
                <header className="flex justify-between items-center">
                    <div>
                        <h2 className="text-2xl font-bold text-white tracking-tight">Matrix Operations</h2>
                        <p className="text-aurora-muted mt-1">Linear Algebra Workspace</p>
                    </div>
                    <div className="flex gap-3">
                        <button
                            onClick={() => {
                                setMatrixA({ rows: 3, cols: 3, values: createEmptyMatrix(3, 3) });
                                setMatrixB({ rows: 3, cols: 1, values: createEmptyMatrix(3, 1) });
                            }}
                            className="px-4 py-2 bg-background-light border border-aurora-border rounded hover:bg-white/5 text-white text-sm flex items-center gap-2"
                        >
                            <RotateCcw size={16} />
                            Reset
                        </button>
                    </div>
                </header>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <MatrixEditor label="A" matrix={matrixA} matrixKey="A" />
                    <MatrixEditor label="B" matrix={matrixB} matrixKey="B" />
                </div>

                {/* Operations Toolbar */}
                <div className="flex justify-center">
                    <div className="bg-background-light border border-aurora-border rounded-full p-2 flex gap-2 flex-wrap justify-center shadow-xl">
                        {['det(A)', 'inv(A)', 'transpose(A)', 'eigenvals(A)', 'A × B', 'rref(A)'].map(op => (
                            <button
                                key={op}
                                onClick={() => executeOperation(op)}
                                disabled={loading}
                                className="px-4 py-2 rounded-full bg-background-dark hover:bg-primary hover:text-white text-aurora-muted text-sm font-mono transition-colors border border-transparent hover:border-primary/50 disabled:opacity-50"
                            >
                                {op}
                            </button>
                        ))}
                    </div>
                </div>

                {/* Results Console */}
                <div className="bg-background-dark rounded-xl border border-aurora-border overflow-hidden">
                    <div className="px-4 py-2 border-b border-aurora-border bg-background-light flex justify-between">
                        <span className="text-xs font-bold text-aurora-muted uppercase tracking-wider">Console Output</span>
                        <button onClick={clearResults} className="text-xs text-primary cursor-pointer hover:underline">
                            Clear
                        </button>
                    </div>
                    <div className="p-4 font-mono text-sm space-y-3 h-48 overflow-y-auto">
                        {results.length === 0 ? (
                            <p className="text-aurora-muted text-center py-8">Click an operation to see results...</p>
                        ) : (
                            results.map((r, i) => (
                                <div key={i} className="border-b border-aurora-border/30 pb-2">
                                    <div className="flex gap-2 text-white/50">
                                        <span className="text-primary">&gt;</span>
                                        <span>{r.command}</span>
                                    </div>
                                    <div className="pl-4 text-primary font-bold mt-1">
                                        = <MathDisplay expression={r.result} inline />
                                    </div>
                                </div>
                            ))
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default MatrixMode;
