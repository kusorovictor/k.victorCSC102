import pandas as pd

# Data for Cadbury Nigeria Plc
data = {
    "Segment": ["Refreshment Beverages", "Refreshment Beverages", "Confectionery", "Confectionery", "Intermediate Cocoa Products", "Intermediate Cocoa Products", "Intermediate Cocoa Products", "Intermediate Cocoa Products"],
    "Product": ["Bournvita", "Hot Chocolate", "Tom Tom", "Buttermint", "Cocoa Powder", "Cocoa Butter", "Cocoa Liquor", "Cocoa Cake"],
    "Brand": ["CADBURY BOURNVITA", "CADBURY 3-in-1 HOT CHOCOLATE", "TOMTOM CLASSIC", "BUTTERMINT", "COCOA POWDER", "COCOA BUTTER", "COCOA LIQUOR", "COCOA CAKE"]
}

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a .csv file
filename = "cadbury_market.csv"
df.to_csv(filename, index=False)

print(f"Data has been saved to {filename}")