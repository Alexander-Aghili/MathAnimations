def getDetails(filename):
    # Initialize an empty list to store rows
    rows = []

    # Open the file for reading
    with open(filename, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into individual values and convert them to float
            row = [float(value) for value in line.split()]

            # Add the row to the list of rows
            rows.append(row)

    return rows


arr = getDetails("TerrainGeneration/out.txt")

for row in arr:
    print(row)