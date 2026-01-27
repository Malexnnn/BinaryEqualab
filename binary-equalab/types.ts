export enum AppMode {
  CONSOLE = 'CONSOLE',
  GRAPHING = 'GRAPHING',
  MATRIX = 'MATRIX',
  ACCOUNTING = 'ACCOUNTING'
}

export interface HistoryItem {
  id: string;
  expression: string;
  result: string;
  timestamp: Date;
}

export interface Transaction {
  id: string;
  date: string;
  description: string;
  amount: number;
  type: 'income' | 'expense';
  category: string;
}
