# 📈 Market Making Strategy – `demo_MarketMaking`

This repository demonstrates a simple **market making algorithm** using the AlgoAPI framework. The strategy is designed for educational and backtesting purposes, and operates on historical EURUSD data.

---

## 🧠 Strategy Overview

A **market making strategy** profits by capturing the **bid-ask spread**. The simplest form of this strategy places a **pair of limit orders** — one to buy at the bid and one to sell at the ask — and waits for both to be filled over time.

When the market remains within a **stable trading range**, this approach can be reasonably effective in earning small, consistent profits from the spread.

However, in a **trending or volatile market**, this strategy can fail:
- One side of the order may remain unfilled for too long.
- The market may drift away, leaving inventory unbalanced.

---

## 🔁 Strategy Logic

To address these weaknesses, this implementation includes **order resetting logic**:

- **Constantly monitor** open orders.
- If **no open orders**, submit a fresh pair of limit orders.
- If **only one side is filled**, **cancel the remaining order** and reset the pair.
- **Adjust bid/ask levels** or order quantity to help rebalance inventory over time.

The **key objective** is to:
- Keep the **net position close to zero**, and
- Maximize the number of completed order pairs.

---

## ⚙️ Implementation Notes

The core logic resides in the `on_marketdatafeed()` function, which runs once per day. It places:

- A **limit buy order** at `(bid - 0.00005)`
- A **limit sell order** at `(ask + 0.00005)`

The orders:
- Use a **fixed spread** of `0.0001` (5 points from bid/ask each side).
- Are **cancelled automatically every week** (via `timeinforce` setting).

---

## 🧪 Backtest Configuration

| Setting             | Value             |
|---------------------|-------------------|
| Strategy Name       | `demo_MarketMaking` |
| Backtest Period     | January 2017 – December 2017 |
| Data Interval       | 1 day             |
| Initial Capital     | USD 100,000       |
| Base Currency       | USD               |
| Leverage            | 50                |
| Transaction Cost    | 0                 |
| Allow Short Selling | Yes               |
| Instruments         | `['EURUSD']`      |

---

## 📁 File Structure

