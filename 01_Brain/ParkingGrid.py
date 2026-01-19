def createParkingGrid(rows, cols):
    parking_grid = []
    print("Enter 1 for occupied and 0 for vacant:")

    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = int(input(f"Slot ({i},{j}): "))
                    if value in [0, 1]:
                        row.append(value)
                        break
                    else:
                        print("Invalid input! Enter only 0 or 1.")
                except ValueError:
                    print("Please enter a numeric value (0 or 1).")
        parking_grid.append(row)

    return parking_grid


# Example usage:
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = createParkingGrid(rows, cols)

print("\nParking Grid:")
for row in grid:
    print(row)
