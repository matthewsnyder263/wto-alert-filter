# WTO Animal Product Notification Filter

This script filters WTO notification Excel files for keywords related to **animal health** and **animal products** (e.g., "beef", "avian", "pork").

It expedites the manual process of reviewing each WTO notification and flags those relevant to USDA's Foreign Agricultural Service (FAS) Animal Division.

---

## What It Does

- Automates keyword filtering for USDA's Foreign Agricultural Service (FAS) Animal Division  
- Reads a `Notifications.xlsx` export from the ePing WTO Alerts site  
- Scans **Title**, **Description**, and **Products covered** columns for animal-related keywords  
- Outputs a `filtered_notifications.csv` with only the relevant rows  
- Accelerates communication to Trade Policy Officers and International Trade Specialists based on commodity relevance

---

## Requirements

- Python 3.10+  
- `pandas`  
- `openpyxl`

Install dependencies with:

```bash
pip install pandas openpyxl
```

---


## Input
Export a `.xlsx` file directly from [ePing WTO Alerts](https://www.epingalert.org/en/Search/Index?domainIds=2) using the **Export Search Results** button (top right).  
Save the file as `Notifications.xlsx` in the same directory as this script.

---

## How to Use
1. Ensure `Notifications.xlsx` is in the same folder as the script.  
2. Run the script:

   ```bash
   python filtered_notifications.py
   ```

3. Check the generated filtered_notifications.csv file

---

## Why It Matters
WTO notifications can affect global trade policy, market access, and regulatory compliance.

This tool streamlines how FAS analysts discover actionable alerts, reducing manual workload and helping teams focus on what’s critical.

---

## Contributing
Contributions are welcome! If you’d like to improve the keyword set, add PostGIS support, or turn this into a GUI tool, feel free to fork the repo and submit a pull request.

