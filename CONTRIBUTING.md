# Contributing to Valuein Financial Data Essentials

First off, thank you for considering contributing to Valuein! It's people like you that make this community the standard for professional financial data.

## 🛑 Scope of Contributions
This repository hosts the **public SDK, documentation, and usage examples** for the Valuein Financial Data Essentials feed.

* **Allowed:** New Python examples, formula corrections, documentation improvements, SDK bug fixes.
* **Not Allowed:** Changes to the underlying data pipeline, database schema, or API infrastructure (these are proprietary).

## 🐛 Found a Bug?
If you find a bug in the source code or a mistake in the documentation, you can help us by [submitting an issue](https://github.com/valuein/quants/issues) to our GitHub Repository. Even better, you can submit a Pull Request with a fix.

**Note:** If you find a **Data Quality Issue** (e.g., wrong EBITDA for Apple), do not open a PR. Please use the [Data Quality Ticket](https://github.com/valuein/quants/issues/new?template=01_data_quality_report.md) instead.

## 💡 Submitting a Pull Request (PR)

### 1. Adding a New Financial Model or Example
We love new examples! If you have a great way to calculate a SaaS metric or a new backtesting strategy:
1.  Place your script in the appropriate `examples/` directory (e.g., `examples/02_quantitative/`).
2.  Ensure it uses the `financial_sdk` client.
3.  Include comments explaining the financial logic.

### 2. Style Guide
We adhere to strict standards to ensure this repo remains production-ready for our institutional clients.
* **Python:** We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/).
* **Docstrings:** All functions must have Google-style docstrings.
* **Type Hinting:** All new functions must have Python type hints.

**Example:**
```python
def calculate_roic(nopat: float, invested_capital: float) -> float:
    """
    Calculates Return on Invested Capital (ROIC).
    
    Args:
        nopat (float): Net Operating Profit After Tax.
        invested_capital (float): Total equity + total debt - cash.
        
    Returns:
        float: The ROIC ratio.
    """
    if invested_capital == 0:
        return 0.0
    return nopat / invested_capital
```

### 3. Commit Messages
* Use the present tense ("Add feature" not "Added feature").
* Reference issues if applicable ("Fixes #42").

## 📄 License
By contributing, you agree that your contributions will be licensed under the same License that covers the project.
