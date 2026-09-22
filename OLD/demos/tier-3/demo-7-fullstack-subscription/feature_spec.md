# Feature Spec: Ingram Micro Cloud Marketplace - Subscription Seat Tier Upgrades & Prorated Billing

## Context
When an MSP or Reseller Partner changes the quantity or license tier of an active subscription (e.g., Microsoft 365 or Adobe Creative Cloud) mid-cycle, the system must:
1. Validate seat changes against vendor minimums.
2. Calculate the exact unbilled/prorated days remaining in the current billing cycle (typically 30-day cycle).
3. Compute credit for unused days of the previous tier and debit for remaining days of the upgraded tier.
4. Record an immutable transaction ledger entry.
5. Provide a responsive UI summary badge for partner approval.

## Existing Schema
- `Subscription`: id, partner_id, customer_id, sku, current_tier, seat_count, unit_price, billing_cycle_start, billing_cycle_end, status.
- `UpgradeRequest`: subscription_id, new_tier, new_seat_count, effective_date.
- `LedgerEntry`: id, subscription_id, transaction_type, prorated_amount, currency, created_at.

## Business Calculation Example
- Total cycle: 30 days.
- Change occurs on Day 10 (20 days remaining).
- Old price: $20.00/seat x 10 seats = $200.00/month. Unused credit = (20/30) * $200.00 = $133.33 credit.
- New price: $30.00/seat x 15 seats = $450.00/month. New charge = (20/30) * $450.00 = $300.00 debit.
- Net Due Now = $300.00 - $133.33 = $166.67.
