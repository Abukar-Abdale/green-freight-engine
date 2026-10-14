
# 🚚 Green Freight Engine — Scope 3 Emissions Engine

A Python-based logistics data pipeline for calculating freight transport carbon emissions (**GHG Protocol Scope 3 Category 4 & Category 9**), fully aligned with the **ISO 14083** standard and the **GLEC Framework**.

---

## 📌 Features

- **Standardized Calculations**: Converts shipment weight (tonnes) and distance (km) into **tonne-kilometers (tkm)** and **\\(\text{CO}_2\text{e}\\) emissions (kg/tonnes)**.
- **Multi-Modal Support**: Pre-loaded Well-to-Wheel (WTW) emission factors for Heavy Diesel Trucks, Electric Trucks, Rail Freight, Ocean Cargo, and Air Freight.
- **Batch CSV Processing**: Automatically ingests raw shipment datasets via `pandas` and computes carbon footprints per route and company-wide totals.
- **Windows & Cross-Platform Safe**: Clean CLI output formatted for all terminal environments.

---

## 🛠️ Project Structure

```text
green-freight-engine/
│
├── core/
│   ├── __init__.py          # Package initializer
│   └── emissions.py         # ISO 14083 emission factors & math logic
│
├── data/
│   └── sample_shipments.csv # Raw shipment test dataset
│
├── main.py                  # Pipeline execution script
└── README.md                # Project documentation
```

---

## 🧮 Methodology & Formulas

The engine uses standard Well-to-Wheel (WTW) carbon intensity factors:

\\[\text{Transport Work (tkm)} = \text{Weight (tonnes)} \times \text{Distance (km)}\\]

\\[\text{CO}_2\text{e (kg)} = \frac{\text{Transport Work (tkm)} \times \text{Emission Factor (g }\text{CO}_2\text{e / tkm)}}{1,000}\\]

### Default Emission Factors (g \\(\text{CO}_2\text{e}\\) / tkm)
| Transport Mode | Mode Key | Emission Factor |
| :--- | :--- | :--- |
| **Heavy Diesel Truck (33t HGV)** | `road_diesel_heavy` | 85.0 g / tkm |
| **Electric Truck (EU Grid)** | `road_electric` | 18.0 g / tkm |
| **Rail Freight** | `rail_freight` | 24.0 g / tkm |
| **Ocean Container Ship** | `ocean_container` | 12.0 g / tkm |
| **Air Freight Cargo** | `air_freight_cargo` | 602.0 g / tkm |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- `pandas` library

### Installation & Execution

1. **Clone or navigate to the repository directory**:
   ```bash
   cd green-freight-engine
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas
   ```

3. **Run the engine**:
   ```bash
   python main.py
   ```

---

## 📊 Sample Output

```text
============================================================
 GREEN FREIGHT ENGINE - SCOPE 3 EMISSION REPORT
============================================================
  shipment_id     origin destination               mode   co2e_kg
0       SH001  Gothenburg  Jönköping  road_diesel_heavy    154.06
1       SH002     Hamburg  Jönköping  road_diesel_heavy   1326.00
2       SH003    Shanghai Gothenburg    ocean_container   3996.00
3       SH004   Frankfurt  Stockholm  air_freight_cargo   3612.00
4       SH005       Malmö  Sundsvall  road_diesel_heavy   1083.75
------------------------------------------------------------
 TOTAL FREIGHT CO2e: 10,171.81 kg (10.1718 tonnes)
============================================================
```

---

## 📜 Roadmap & Future Enhancements

- [x] **Block 1**: Raw CSV Data Pipeline & Ingestion
- [x] **Block 2**: Core Scope 3 Engine & ISO 14083 Emission Logic
- [ ] **Step 4**: Modal Shift Optimization (Road $\rightarrow$ Rail / Ocean reduction metrics)
- [ ] **Step 5**: Automated CSRD Report Exporter (CSV / PDF)
- [ ] **Step 6**: PostgreSQL Database Persistence & Power BI Control Tower Integration
```

---

🌱 **Next Step:** Now that your core setup and documentation are complete, would you like to build **Step 4: The Modal Shift Evaluator** (to calculate how much \\(\text{CO}_2\\) and money clients save by switching from Road/Air to Rail)?
