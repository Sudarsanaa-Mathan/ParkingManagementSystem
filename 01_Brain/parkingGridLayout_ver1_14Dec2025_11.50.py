rows = 6
cols = 5

matrix = []

for i in range(1, rows + 1):
    row = []
    for j in range(1, cols + 1):
        row.append(f"Lot{i}{j}")
    matrix.append(row)

# Display the matrix
for row in matrix:
    print(row)

lift_facilities = ['Lift1', 'Lift2']
# Lifts
#lifts = ["Lift1", "Lift2"]

# Nearest slots for each lift (Priority 1)
nearest_slots = {
    "Lift1": ["Lot63", "Lot64", "Lot62", "Lot53", "Lot52", "Lot54"],
    "Lift2": ["Lot15", "Lot14", "Lot16", "Lot25", "Lot24", "Lot26"]
}

# Create the final list
lift_priority_list = []

for lift in lift_facilities:
    lift_priority_list.append(
        [lift, ["P1"] + nearest_slots[lift]]
    )

# Display result
# for item in lift_priority_list:
# print(item)

#occupany_flag = ["Occupied", "Not Occupied"]

#function Start - fun_ParkingStatus
"""
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9


"""

occupancy_status = []
for i in range(rows):
    occupancy_status_row = []
    for j in range(cols):
        occupancy_status_row.append("Not Occupied")
    occupancy_status.append(occupancy_status_row)


def display_occupancy():
    print("\nPARKING OCCUPANCY MATRIX")
    for i in range(rows):
        for j in range(cols):
            if occupancy_status[i][j] == "Occupied":
                print("🟥", end=" ")
            else:
                print("🟩", end=" ")
        print()


def fun_allocate_nearest_slot(lift, car):
    
    if lift == 'Lift1':
        lift1_slots = nearest_slots["Lift1"]
    #lift1_len = len(nearest_slots["Lift1"])
    
    #lift1_occupany = []
    #for _ in range(len(lift1_slots)):
    # lift1_occupany[i] = "Not Occupied"
    #    lift1_occupany.append("Not Occupied")

    
    if(car == 'Y'):
        for i in range(len(lift1_slots)):
                row = int(lift1_slots[i][3]) - 1
                col = int(lift1_slots[i][4]) - 1

                if(occupancy_status[row][col] == "Not Occupied"):
                    occupancy_status[row][col] = "Occupied"
                    print("Car allocated", lift1_slots[i])
                    break
        else:
            print("No free slots available near lift1")
            
    

        
    display_occupancy()
        
                
lift = "Lift1"
car = input("Car 1 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 2 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 3 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 4 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 5 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 6 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 7 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 8 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 9 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)

car = input("Car 10 entry(Y) ?:").upper()
fun_allocate_nearest_slot(lift, car)


#function End - fun_ParkingStatus




