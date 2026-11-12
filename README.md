# Expense Tracker (JPY)

A small tracker for monthly spending in yen: totals, spend by category, daily average, and the biggest single expense.

## Why I built this

I live in Naha and track what I spend each month — rent, food, transport, study books, phone. I used to do this in a spreadsheet; this project is the same summary rebuilt in Python, so I can re-run it whenever I add new rows.

## What it does

Reads `expenses.csv` (date, category, amount_jpy, note — 18 sample expenses over Oct 2026) and prints:

- Total spend, average per day, and average per expense
- Spend by category, with each category's share of the total
- The single biggest expense

## How to run

```bash
cd expense-tracker-jpy
python expense_tracker.py
```

Point it at your own data by replacing `expenses.csv` (keep the same columns).

## Sample output

```
Expense summary - 18 expenses
Period: 2026-10-01 to 2026-10-31 (31 days)
----------------------------------------------------
Total spend:         65,580 JPY
Average per day:     2,115 JPY
Average per expense: 3,643 JPY

By category:
Category      Count         Total    Share
Rent              1        45,000    68.6%
Food              9         8,300    12.7%
Study             2         4,700     7.2%
Phone             1         2,980     4.5%
Transport         4         2,600     4.0%
Other             1         2,000     3.0%

Biggest expense: 45,000 JPY on 2026-10-01 (Rent - Monthly rent)
```

(Data is sample data created for practice.)

## Files

- `expense_tracker.py` — the program
- `expenses.csv` — sample expenses (18 rows, Oct 2026)

## Next steps

- Add a monthly comparison, so October vs November is one command
- Flag any category that goes over a budget I set
- Plot the daily spend trend once I start using matplotlib

*Standard library only for now. Built while learning Python.*
