# 🏛️ Valuein Financial Data Essentials (FDE) - Public Resources

[![Data Quality](https://img.shields.io/badge/Data_Quality-99.9%25-green)]()
[![Update Frequency](https://img.shields.io/badge/Updates-Daily-blue)]()
[![Python](https://img.shields.io/badge/Python-3.12%2B-green)]()

**Professional-grade SEC financial data for financial analysts, quantitative researchers, data engineers, and investment teams.**

## 👋 Welcome

This repository serves as the official integration hub for Valuein Financial Data Essentials feed by hosting our documentation, features requests, issue tracker, and the official Python SDK, schema definitions, and usage patterns for production environments.


## 📚 Documentation
* [**Data Dictionary**](docs/DATA_DICTIONARY.md): The live, auto-updated definition of every metric and column.
* [**Connection Guide**](docs/CONNECTING.md): How to connect via Snowflake, Postgres, or API.
* [**Schema Guide**](docs/SCHEMAS.md): Entity-relationship diagrams and join logic.


## 🛡️ Data Governance & Methodology
We adhere to strict standards to ensure institutional-grade reliability.

* **Methodology**: How we map GAAP/IFRS tags to standardized metrics and handle restatements.
* **SLA Policy**: Our commitment to 99.9% uptime and <2min SEC filing latency.
* **Restatement Handling**: We preserve "as-reported" history to support true point-in-time backtesting.


## ⚡ Quick Start
Clone this repo and install dependencies:
```bash
git clone [https://github.com/valuein/quants.git](https://github.com/valuein/quants.git)
cd quants
pip install -r requirements.txt
```

## 🚀 Getting Started with Examples
We provide tailored examples for different roles:

| Role | Directory                                                      | Use Case |
| :--- |:---------------------------------------------------------------| :--- |
| **Data Engineers** | [`examples/01_engineering`](examples/01_engineering)           | Bulk ingestion, schema validation, incremental loading. |
| **Quants** | [`examples/02_quantitative`](examples/02_quantitative)         | Alpha factor creation, time-series alignment, backtesting. |
| **Analysts/PMs** | [`examples/03_fundamental`](examples/03_fundamental)  | DCF modeling inputs, peer comparison, ratio analysis. |

## 🆘 Support & Community
* **Found a data error?** [Open a Data Ticket](https://github.com/valuein/quants/issues/new?template=01_data_quality_report.md)
* **Need a new metric?** [Request a Feature](https://github.com/valuein/quants/issues/new?template=02_feature_request.md)
* **Service down?** [Service Outage](https://github.com/valuein/quants/issues/new?template=03_service_outage.md)
* **General Question?** [Start a Discussion](https://github.com/valuein/quants/discussions)


---
## License

This project is licensed under a Proprietary Software License. See the `LICENSE` file for more information.
