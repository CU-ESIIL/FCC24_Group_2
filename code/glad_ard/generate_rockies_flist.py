import geopandas as gpd
import pandas as pd
import numpy as np
import os

START_YEAR = 1997
END_YEAR = 2023
GLAD_FILE_PATERN = "https://glad.umd.edu/dataset/glad_ard2/{lat}/{tile}/{period}.tif"
OUTPUT_DIR = "."
ECO_REGION = "Southern Rockies"


def main():
    # read eco region and write to file
    eco_regions = gpd.read_file("zip://" + "us_eco_l3.zip")
    southern_rockies = eco_regions[eco_regions["US_L3NAME"] == ECO_REGION]
    southern_rockies = southern_rockies.to_crs("EPSG:4326")
    southern_rockies.to_file("/data-store/output/eco_region.geojson", driver="GeoJSON")

    # get ard tiles that intersect the ecoregion
    ard_tiles = gpd.read_file(
        "https://glad.umd.edu/users/Potapov/ARD/Global_ARD_tiles.zip"
    )
    relevant_ard_tiles = ard_tiles.clip(southern_rockies)
    tiles = relevant_ard_tiles["TILE"].unique()

    # use the ard time codes to general all codes for the year ranges
    start_codes = np.cumsum(np.repeat(23, END_YEAR - START_YEAR + 1)) + 392 - 23
    year_code_maps = {
        year: list(range(start, start + 23))
        for year, start in zip(range(START_YEAR, END_YEAR + 1), start_codes)
    }

    rows = []
    for tile in tiles:
        for year, year_codes in year_code_maps.items():
            for code in year_codes:
                rows.append(
                    (
                        tile,
                        year,
                        code,
                        GLAD_FILE_PATERN.format(
                            lat=tile.split("_")[1], tile=tile, period=code
                        ),
                    )
                )

    ard_assets = pd.DataFrame(rows, columns=["tile", "year", "16-day-code", "url"])
    print("saving to flist.txt")
    ard_assets.iloc[:100]["url"].to_csv("flist.txt", index=False, header=False)


if __name__ == "__main__":
    main()
