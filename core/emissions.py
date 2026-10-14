"""Core Scope 3 Freight Emission Engine (ISO 14083 / GLEC Framework compliant)."""

from typing import Dict

# Emission factors in grams of CO2e per tonne-kilometer (g CO2e / tkm)
EMISSION_FACTORS: Dict[str, float] = {
    "road_diesel_heavy": 85.0,  # Heavy Diesel Truck
    "road_electric": 18.0,  # Electric Truck (EU Grid)
    "rail_freight": 24.0,  # Electric/Diesel Freight Train
    "ocean_container": 12.0,  # Container Cargo Ship
    "air_freight_cargo": 602.0,  # Air Cargo Plane
}


def calculate_shipment_emissions(
    weight_tons: float,
    distance_km: float,
    mode: str,
) -> Dict[str, float]:
    """Calculates total CO2e emissions (kg) for a single shipment."""
    if mode not in EMISSION_FACTORS:
        raise ValueError(
            f"Unknown transport mode '{mode}'. Available: {list(EMISSION_FACTORS.keys())}"
        )

    # 1. Look up how dirty the vehicle is
    factor = EMISSION_FACTORS[mode]

    # 2. Calculate Tonne-Kilometers (Transport Work)
    tonne_km = weight_tons * distance_km

    # 3. Multiply by factor and divide by 1,000 to convert grams to kilograms
    co2e_kg = (tonne_km * factor) / 1000.0

    return {
        "tonne_km": round(tonne_km, 2),
        "co2e_kg": round(co2e_kg, 2),
        "co2e_tons": round(co2e_kg / 1000.0, 4),
    }
