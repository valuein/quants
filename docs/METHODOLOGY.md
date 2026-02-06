# 📐 Data Methodology & Standardization

Transparency is the core of the Valuein FDE product. This document details how we process raw SEC XBRL data into standardized financial time series.

## 1. Data Sourcing & Lineage


1.  **Ingestion:** We pull raw XBRL instances directly from the SEC EDGAR RSS feed.
2.  **Validation:** We verify the `adsh` (Accession Number) against the CI/CII registry.
3.  **Parsing:** We extract facts using the US-GAAP Taxonomy (2020-2025).

## 2. Point-in-Time (PIT) Architecture
To prevent look-ahead bias in quantitative backtesting, we strictly preserve the timeline of information availability.

* **`report_date` (The "As-Of" Date):** The end of the fiscal period (e.g., Dec 31, 2024).
* **`filing_date` (The "Knowledge" Date):** The date the file was actually published to the SEC (e.g., Feb 14, 2025).
* **`ingested_at` (The "System" Date):** The timestamp the row entered our database.

**⚠️ Quant Note:** When backtesting, always filter by `filing_date <= trade_date` to ensure you are not trading on information the market did not have yet.

## 3. Restatement Handling
We utilize an **Append-Only** strategy for restatements. We never overwrite historical rows.

If a company restates their 2023 Q3 earnings:
1.  The original row remains valid but is marked `is_restated = TRUE` (virtual logic).
2.  A *new* row is inserted with the new `value` and the newer `filing_date`.

This allows you to reconstruct the "Point-in-Time" reality of the market on any given past date.

## 4. Standardization Logic
We map over 15,000 raw XBRL tags into ~150 standardized metrics using a "Waterfall" approach.

### Example: `Operating Income`
We attempt to resolve this metric in the following order:
1.  **Direct Tag:** `us-gaap:OperatingIncomeLoss`
2.  **Calculation:** `GrossProfit - OperatingExpenses`
3.  **Calculation:** `Revenues - CostOfRevenue - OperatingExpenses`

If all methods fail, the value is recorded as `NULL` rather than imputed (zero-filled), to maintain statistical integrity.

## 5. Fiscal Year Alignment
Companies have differing fiscal year-ends (e.g., Apple ends in September).
* **Fiscal Period:** As reported by the company (e.g., FY2024 Q1).
* **Calendar Period:** We normalize all data to the standard Calendar Year (CY) to allow for peer comparison.
    * *Example:* A fiscal quarter ending Jan 31, 2024 is mapped to `CY2023 Q4`.
