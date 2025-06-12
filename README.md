# WTO Animal Health Notification Filter

This Python script filters WTO notification Excel exports for keywords related to animal health and products (e.g., beef, pork, cattle, poultry). It's designed to support International Trade Specialists from USDA's Foreign Agriculture Service who monitor daily WTO SPS/TBT notifications and want a quick way to highlight relevant entries.

---

## What It Does

- Reads a WTO Excel export (e.g., `Notifications.xlsx`)
- Filters rows that contain any **animal-related keywords** in the:
  - `Title`
  - `Description`
  - `Products covered`
- Outputs a filtered Excel file: `Filtered_Notifications.xlsx`
- This expedites the manual process of having one person sort through each new heading, sometimes translating, and informing the corresponding analyst to any new WTO alerts on their commodities.
- Optionally opens the filtered file automatically

---

## Setup

### 1. Requirements

You’ll need Python 3.11+ and the following packages:

```bash
pip install pandas openpyxl
