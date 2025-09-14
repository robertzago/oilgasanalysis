import country_converter as coco
import pandas as pd

def get_data_per_year(year: int):
    fiw_data = pd.read_excel("Aggregate_Category_and_Subcategory_Scores_FIW_2003-2024.xlsx", sheet_name="FIW06-24")
    oil_rent_data = pd.read_csv("API_NY.GDP.PETR.RT.ZS_DS2_en_csv_v2_6432.csv", encoding='utf-8-sig', skiprows=4)
    oil_prod_data = pd.read_csv("oil-prod-per-capita.csv")

    fiw_data = clean_up_countries(fiw_data, "Country/Territory")
    oil_rent_data = clean_up_countries(oil_rent_data, "Country Code")
    oil_prod_data = clean_up_countries(oil_prod_data, "Code")

    fiw_data16 = fiw_data[fiw_data["Edition"] == year].rename(columns={"Total": "FreedomInTheWorld"})
    oil_rent_data16 = oil_rent_data[["clean_codes", str(year)]].rename(columns={str(year): "OilRentPercentGDP"})
    oil_prod_data16 = oil_prod_data[oil_prod_data["Year"] == year].rename(columns={"Oil production per capita (kWh)": "OilProdPerCapita"})

    fiw_data16      = fiw_data16[fiw_data16["clean_codes"] != "not found"]
    oil_rent_data16 = oil_rent_data16[oil_rent_data16["clean_codes"] != "not found"]
    oil_prod_data16 = oil_prod_data16[oil_prod_data16["clean_codes"] != "not found"]

    fiw_data16 = fiw_data16[["clean_codes", "FreedomInTheWorld"]]

    oil_prod_data16 = oil_prod_data16[["clean_codes", "OilProdPerCapita"]]

    return fiw_data16, oil_rent_data16, oil_prod_data16


def clean_up_countries(data, row_name):
    cc = coco.CountryConverter()
    data["clean_codes"] = cc.pandas_convert(series=data[row_name], to="ISO3")
    return data


print("\n" + "="*70 + "\n")
fiw16, oilre16, oilpr16 = get_data_per_year(2016)

print(fiw16.head())
print(oilre16.head())
print(oilpr16.head())