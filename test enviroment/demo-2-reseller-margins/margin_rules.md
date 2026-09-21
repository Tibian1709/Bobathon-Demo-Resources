# Ingram Micro Reseller Discount & Tiering Model Rules

## Partner Tier Thresholds (Annual Gross Spend in USD)
- **Standard (Entry Tier)**: $0 – $99,999 annual spend.
  - Base Distributor Discount: 5.0% off MSRP.
  - Rebate Incentive: 0%
- **Silver Partner**: $100,000 – $499,999 annual spend.
  - Base Distributor Discount: 8.5% off MSRP.
  - Quarterly Rebate Incentive: 1.0% on incremental cloud services.
- **Gold Partner**: $500,000 – $1,999,999 annual spend.
  - Base Distributor Discount: 12.0% off MSRP.
  - Quarterly Rebate Incentive: 2.0% on incremental cloud services.
  - Free 24/7 Level-2 Partner Support Access.
- **Platinum Partner**: $2,000,000+ annual spend.
  - Base Distributor Discount: 16.5% off MSRP.
  - Quarterly Rebate Incentive: 3.5% on incremental cloud services.
  - Dedicated Solutions Architect & Custom API Throttling limits (5,000 req/min).

## Calculation Formulas
- `Ingram Buy Rate = MSRP * (1 - Ingram Base Discount Rate)`
- `Reseller Buy Price = MSRP * (1 - Partner Tier Discount Rate)`
- `Distributor Margin $ = Reseller Buy Price - Ingram Buy Rate`
- `Distributor Margin % = (Distributor Margin $ / Reseller Buy Price) * 100`
- `Reseller Gross Margin $ = MSRP - Reseller Buy Price`
- `Reseller Margin % = (Reseller Gross Margin $ / MSRP) * 100`

## Target Product SKUs for Demo Spreadsheet
1. Microsoft 365 Business Premium (SKU: M365-BP) - MSRP: $22.00 / user / month
2. Adobe Creative Cloud for Teams (SKU: ADB-CCT) - MSRP: $84.99 / user / month
3. Cisco Duo MFA Enterprise (SKU: CISCO-DUO) - MSRP: $6.00 / user / month
4. AWS Cloud Consumption Direct (SKU: AWS-CON) - MSRP: Variable ($10,000 base package)
5. Veeam Backup for Microsoft 365 (SKU: VEEAM-M365) - MSRP: $1.80 / user / month
