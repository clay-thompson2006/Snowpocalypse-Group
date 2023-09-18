import csv

# Sample data
data = [
    ["Name", "Age", "Location"],
    ["John", 25, "New York"],
    ["Alice", 30, "Los Angeles"],
]

# Open a CSV file in write mode
with open("output.csv", "w", newline="") as csvfile:
    # Create a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Write the data to the CSV file
    for row in data:
        csvwriter.writerow(row)

print("Data has been written to output.csv")
