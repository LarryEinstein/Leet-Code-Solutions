from haversine import haversine, Unit
import numpy as np
import math
import requests
import pandas as pd

# 1. Load the data
worldcities_df = pd.read_csv("worldcities.csv", header=0)
print("First row of full dataset:")
print(worldcities_df.head(1), "\n")

# 2. Filter to primary capitals only
worldcities_df_capitals = worldcities_df[worldcities_df["capital"] == "primary"].reset_index(drop=True)
print("First 13 capital cities:")
print(worldcities_df_capitals.head(13), "\n")

# 3. Keep only what we need for distance calculations
worldcities_df_haversine = worldcities_df_capitals[["city", "lat", "lng"]].reset_index(drop=True)
print("Capitals used for haversine calculations:")
print(worldcities_df_haversine.head(), "\n")

# Example sanity check
tokyo_to_jakarta = haversine((35.687, 139.7495), (-6.175, 106.8275))
print("Tokyo to Jakarta distance (km):", tokyo_to_jakarta, "\n")

# 4. Prepare for pairwise distances between capitals
cities = worldcities_df_haversine["city"].to_numpy()
lats = worldcities_df_haversine["lat"].to_numpy()
lngs = worldcities_df_haversine["lng"].to_numpy()

num_cities = len(cities)
print(f"Number of capital cities: {num_cities}")

rows = []

# 5. Compute all unique pairs (i < j)
for i in range(num_cities):
    lat_i = lats[i]
    lng_i = lngs[i]
    city_i = cities[i]

    for j in range(i + 1, num_cities):
        lat_j = lats[j]
        lng_j = lngs[j]
        city_j = cities[j]

        distance = haversine((lat_i, lng_i), (lat_j, lng_j))

        rows.append(
            {
                "city_a": city_i,
                "city_b": city_j,
                "distance": distance,
            }
        )

# 6. Build the DataFrame once
city_a_city_b_distance_df = pd.DataFrame(rows)
print("\nSample of city-to-city distances:")
print(city_a_city_b_distance_df.head())

# 7. Top 10 most remote capital pairs (farthest distances)
top_10_remote = city_a_city_b_distance_df.sort_values("distance", ascending=False).head(10)

print("\nTop 10 most remote capital city pairs:")
print(top_10_remote)
