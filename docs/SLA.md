# 🛡️ Service Level Agreement (SLA)

**Effective Date:** February 1, 2026

This Service Level Agreement ("SLA") outlines the performance commitments for the Valuein Financial Data Essentials (FDE) feed.

## 1. System Availability
We guarantee that the Data API and Database Access will be available **99.9%** of the time during any monthly billing cycle.

| Status | Definition |
| :--- | :--- |
| **Operational** | API responds with 200 OK; Database accepts connections. |
| **Degraded** | API latency > 2s; Database connection pool > 90% utilization. |
| **Outage** | Total inability to access data endpoints. |

## 2. Data Freshness & Latency
We commit to the following "Time-to-Database" latencies from the moment a filing is accepted by the SEC EDGAR system:

| Filing Type | Processing Target | Guarantee      |
| :--- |:------------------|:---------------|
| **8-K (Events)** | < 5 minutes       | 24 hours       |
| **10-Q (Quarterly)** | < 5 minutes       | 24 hours       |
| **10-K (Annual)** | < 5 minutes       | 24 hours       |

## 3. Support Response Times
Tickets submitted via the [Support Portal](../.github/ISSUE_TEMPLATE) are prioritized as follows:

| Severity | Definition | Response Time |
| :--- | :--- | :--- |
| **Critical** | Complete service outage; Production blocker. | < 2 Hours (24/7) |
| **High** | Significant data error (e.g., wrong ticker mapping). | < 1 Business Day |
| **Normal** | Question about methodology; Feature request. | < 3 Business Days |

## 4. Maintenance Windows
* **Scheduled Maintenance:** Occurs Sundays between 04:00 UTC and 06:00 UTC.
* **Emergency Maintenance:** We reserve the right to patch critical security vulnerabilities immediately, with notification sent via email within 30 minutes.

---
*For credit requests regarding SLA breaches, please contact billing@valuein.biz with your incident ticket number.*

