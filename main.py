import os
import sys

# Ensures Python can locate the core module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
from core.emissions import calculate_shipment_emissions


def run_pipeline():
    print("=" * 60)
    print(" GREEN FREIGHT ENGINE - SCOPE 3 EMISSION REPORT")
    print("=" * 60)

    # 1. Load the raw shipments CSV file (Block 1)
    df = pd.read_csv("data/sample_shipments.csv")

    # 2. Pass each shipment row through our Math Engine (Block 2)
    results = df.apply(
        lambda row: calculate_shipment_emissions(
            weight_tons=row["weight_tons"],
            distance_km=row["distance_km"],
            mode=row["mode"],
        ),
        axis=1,
    )

    # 3. Combine the results back into the table
    results_df = pd.DataFrame(list(results))
    df = pd.concat([df, results_df], axis=1)

    # 4. Display the calculation table
    print(df[["shipment_id", "origin", "destination", "mode", "co2e_kg"]])

    # 5. Print total emissions summary
    total_kg = df["co2e_kg"].sum()
    total_tons = df["co2e_tons"].sum()
    print("-" * 60)
    print(f" TOTAL FREIGHT CO2e: {total_kg:,.2f} kg ({total_tons:.4f} tonnes)")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()