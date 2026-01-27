import React from 'react';
import { Transaction } from '../types';

const AccountingMode: React.FC = () => {
  const transactions: Transaction[] = [
    { id: '1', date: '2023-10-24', description: 'Consulting Services', amount: 1250.00, type: 'income', category: 'Sales' },
    { id: '2', date: '2023-10-25', description: 'Office Supplies', amount: -120.50, type: 'expense', category: 'Operations' },
    { id: '3', date: '2023-10-26', description: 'Software License', amount: -49.99, type: 'expense', category: 'Software' },
    { id: '4', date: '2023-10-27', description: 'Client Retainer', amount: 3000.00, type: 'income', category: 'Sales' },
  ];

  const totalBalance = transactions.reduce((acc, curr) => acc + curr.amount, 0);

  return (
    <div className="flex flex-col h-full bg-aurora-bg relative overflow-hidden">
        {/* Background glow */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[600px] h-[300px] bg-aurora-primary/10 blur-[100px] pointer-events-none"></div>

        <div className="relative z-10 flex flex-col h-full max-w-5xl mx-auto w-full p-4 lg:p-8">
            
            {/* Header / Big Counter */}
            <div className="flex flex-col items-center justify-center py-8 gap-4">
                <span className="text-aurora-muted uppercase tracking-widest text-xs font-bold">Current Balance</span>
                <div className="flex items-center gap-8">
                    <button className="size-12 rounded-full bg-red-600/20 text-red-500 hover:bg-red-600 hover:text-white transition-colors flex items-center justify-center border border-red-600/30">
                        <span className="material-symbols-outlined">remove</span>
                    </button>
                    <h1 className="text-5xl lg:text-7xl font-bold text-aurora-primary tracking-tight font-display drop-shadow-2xl">
                        $ {totalBalance.toLocaleString(undefined, { minimumFractionDigits: 2 })}
                    </h1>
                    <button className="size-12 rounded-full bg-emerald-600/20 text-emerald-500 hover:bg-emerald-600 hover:text-white transition-colors flex items-center justify-center border border-emerald-600/30">
                        <span className="material-symbols-outlined">add</span>
                    </button>
                </div>
            </div>

            {/* Quick Actions */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
                <div className="bg-aurora-surface border border-white/10 rounded-xl p-4 flex flex-col gap-2">
                    <label className="text-xs text-aurora-muted uppercase font-bold">Amount</label>
                    <div className="flex items-center gap-2">
                        <span className="text-xl text-aurora-muted">$</span>
                        <input type="number" className="bg-transparent border-none text-white text-2xl font-bold w-full focus:ring-0 p-0" placeholder="0.00" />
                    </div>
                </div>
                <div className="bg-aurora-surface border border-white/10 rounded-xl p-4 flex flex-col gap-2">
                    <label className="text-xs text-aurora-muted uppercase font-bold">Description</label>
                    <input type="text" className="bg-transparent border-none text-white text-lg w-full focus:ring-0 p-0" placeholder="Transaction note..." />
                </div>
            </div>

            {/* Ledger Table */}
            <div className="flex-1 bg-aurora-surface border border-white/10 rounded-xl overflow-hidden flex flex-col shadow-2xl">
                <div className="p-4 border-b border-white/10 bg-aurora-panel flex justify-between items-center">
                    <h3 className="font-bold text-white flex items-center gap-2">
                        <span className="material-symbols-outlined text-aurora-primary">history</span>
                        Transaction Ledger
                    </h3>
                    <button className="text-xs text-aurora-muted hover:text-white flex items-center gap-1">
                        <span className="material-symbols-outlined text-sm">download</span> Export CSV
                    </button>
                </div>
                <div className="overflow-auto flex-1">
                    <table className="w-full text-left">
                        <thead className="bg-aurora-bg text-xs text-aurora-muted uppercase font-bold sticky top-0">
                            <tr>
                                <th className="p-4">Date</th>
                                <th className="p-4">Description</th>
                                <th className="p-4">Category</th>
                                <th className="p-4 text-right">Amount</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-white/5 text-sm">
                            {transactions.map((t) => (
                                <tr key={t.id} className="hover:bg-white/5 transition-colors group">
                                    <td className="p-4 text-aurora-muted font-mono">{t.date}</td>
                                    <td className="p-4 text-white font-medium">{t.description}</td>
                                    <td className="p-4 text-aurora-muted">
                                        <span className="px-2 py-1 rounded bg-white/5 text-xs border border-white/10">{t.category}</span>
                                    </td>
                                    <td className={`p-4 text-right font-bold font-mono ${t.type === 'income' ? 'text-emerald-500' : 'text-red-500'}`}>
                                        {t.type === 'income' ? '+' : ''} $ {Math.abs(t.amount).toFixed(2)}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>

            <div className="mt-4 flex justify-end gap-3">
                 <button className="px-6 py-3 rounded-lg bg-aurora-surface border border-white/10 text-aurora-muted hover:text-white font-bold transition-colors">Reset</button>
                 <button className="px-6 py-3 rounded-lg bg-aurora-primary text-white font-bold shadow-lg hover:bg-aurora-accent transition-colors">Save Report</button>
            </div>

        </div>
    </div>
  );
};

export default AccountingMode;
