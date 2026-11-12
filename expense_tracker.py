"""
Expense Tracker (JPY)
---------------------
Practice project for my data-analysis skills. I track my own spending
in a small CSV while studying in Naha, and this script turns it into a
one-page summary: total, spend by category, daily average, biggest day.

Reads expenses.csv (date, category, amount_jpy, note) and prints:
  * Total spend and number of expenses
  * Spend by category, with share of the total
  * Average spend per day over the period
  * The single biggest expense

All amounts are in Japanese yen (JPY). Data is sample data for practice.

Built by Shivam Kaushik while learning Python.
Standard library only (csv, datetime).
"""

import csv
from datetime import date

EXPENSES_FILE = "expenses.csv"


def load_expenses(filename):
    rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows.append({
                "date": row["date"],
                "category": row["category"],
                "amount": float(row["amount_jpy"]),
                "note": row["note"],
            })
    return rows


def main():
    rows = load_expenses(EXPENSES_FILE)
    total = sum(r["amount"] for r in rows)
    first = date.fromisoformat(rows[0]["date"])
    last = date.fromisoformat(rows[-1]["date"])
    days = (last - first).days + 1

    print(f"Expense summary - {len(rows)} expenses")
    print(f"Period: {rows[0]['date']} to {rows[-1]['date']} ({days} days)")
    print("-" * 52)
    print(f"Total spend:         {total:,.0f} JPY")
    print(f"Average per day:     {total / days:,.0f} JPY")
    print(f"Average per expense: {total / len(rows):,.0f} JPY")

    by_cat = {}
    for r in rows:
        c = by_cat.setdefault(r["category"], {"count": 0, "total": 0.0})
        c["count"] += 1
        c["total"] += r["amount"]

    print("\nBy category:")
    print(f"{'Category':<12}{'Count':>7}{'Total':>14}{'Share':>9}")
    for name, c in sorted(by_cat.items(), key=lambda i: i[1]["total"], reverse=True):
        print(f"{name:<12}{c['count']:>7,}{c['total']:>14,.0f}{c['total'] / total:>9.1%}")

    biggest = max(rows, key=lambda r: r["amount"])
    print(f"\nBiggest expense: {biggest['amount']:,.0f} JPY on {biggest['date']} "
          f"({biggest['category']} - {biggest['note']})")


if __name__ == "__main__":
    main()
