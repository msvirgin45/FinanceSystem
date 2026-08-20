# Finance System

A personal command-line finance system built with Python and SQLite.

## Goals:

This project is planned to help users manage money by tracking their income/expenses, accounts, catergories, budgets, 
recurring transactions, and reports.

## Planned Features:

1. **Transaction management**
   - Add income
   - Add expenses
   - Edit transactions
   - Delete transactions
   - View all transactions
   - Search/filter/sort transactions


2. **Multiple accounts**
   - Example: Cash, Bank, Credit Card, Savings


3. **Categories**
   - Predefined categories
   - Custom user categories


4. **Budgets**
5. **Recurring transactions**
6. **Financial reports**
7. **Search system**
8. **Data validation**
9. **SQLite database**
10. **Import/Export**
11. **Configuration settings**
12. **Command-line interface**

## Tech Stack

- Python 3.10+
- SQLite3 (built into Python)
- Standard library first (can expand later)

## Project Structure

```text
FinanceSystem/
  src/
    main.py
    cli.py
    db/
      connection.py
      schema.sql
    utils/
      validators.py
```

## Getting Started

1. Clone repo
2. Make sure Python 3.10+ is installed
3. Run:

```bash
python src/main.py
```

## Current Status

Early foundation stage:
- CLI shell
- DB connection helper
- Starter schema
- Basic validators

## Next Build Targets

- Add account creation/listing commands
- Add category creation/listing commands
- Add transaction add/view commands
- Add filter/search support