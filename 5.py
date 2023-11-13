# Data Login
login_data = [
    ["cakboyo", "pangerantampan"],
    ["konoha", "selaludihati"],
    ["cakjukir", "ahlinyaahli"]
]

# Available parking slots
parking_slots = {
    "lantai_1": {
        "sepeda_motor": ["-" for _ in range(10)] for _ in range(10)],
        "mobil": ["-" for _ in range(10)] for _ in range(10)]
    },
    "lantai_2": {
        "sepeda_motor": ["-" for _ in range(10)] for _ in range(10)],
        "mobil": ["-" for _ in range(10)] for _ in range(10)]
    },
    "lantai_3": {
        "sepeda_motor": ["-" for _ in range(10)] for _ in range(10)],
        "mobil": ["-" for _ in range(10)] for _ in range(10)],
        "bus": ["-" for _ in range(10)] for _ in range(10)]
    }
}

# Initialize daily counts and earnings
parked_counts = {
    "sepeda_motor": 0,
    "mobil": 0,
    "bus": 0
}

earnings = {
    "sepeda_motor": 0,
    "mobil": 0,
    "bus": 0
}

# Login
def login():
    for _ in range(3):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if [username, password] in login_data:
            return True
        print("Invalid username or password. Please try again.")
    return False

# Parking
def park_vehicle():
    vehicle_type = input("Enter the vehicle type (sepeda_motor/mobil/bus): ")
    plat_nomor = input("Enter the plat nomor: ")

    if vehicle_type == "sepeda_motor":
        if parked_counts["sepeda_motor"] < 30:
            for i in range(10):
                for j in range(3):
                    if parking_slots["lantai_1"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_1"][vehicle_type][i][j] = plat_nomor
                        parked_counts["sepeda_motor"] += 1
                        print("Vehicle parked at lantai_1, coordinates: {}{}".format(chr(65+j), i+1))
                        return
            for i in range(10):
                for j in range(8):
                    if parking_slots["lantai_2"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_2"][vehicle_type][i][j] = plat_nomor
                        parked_counts["sepeda_motor"] += 1
                        print("Vehicle parked at lantai_2, coordinates: {}{}".format(chr(65+j), i+1))
                        return
            for i in range(8):
                for j in range(6):
                    if parking_slots["lantai_3"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_3"][vehicle_type][i][j] = plat_nomor
                        parked_counts["sepeda_motor"] += 1
                        print("Vehicle parked at lantai_3, coordinates: {}{}".format(chr(65+j), i+1))
                        return

    elif vehicle_type == "mobil":
        if parked_counts["mobil"] < 45:
            for i in range(10):
                for j in range(8):
                    if parking_slots["lantai_1"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_1"][vehicle_type][i][j] = plat_nomor
                        parked_counts["mobil"] += 1
                        print("Vehicle parked at lantai_1, coordinates: {}{}".format(chr(65+j), i+3))
                        return
            for i in range(10):
                for j in range(8):
                    if parking_slots["lantai_2"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_2"][vehicle_type][i][j] = plat_nomor
                        parked_counts["mobil"] += 1
                        print("Vehicle parked at lantai_2, coordinates: {}{}".format(chr(65+j), i+3))
                        return
            for i in range(5):
                for j in range(7):
                    if parking_slots["lantai_3"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_3"][vehicle_type][i][j] = plat_nomor
                        parked_counts["mobil"] += 1
                        print("Vehicle parked at lantai_3, coordinates: {}{}".format(chr(65+j), i+1))
                        return

    elif vehicle_type == "bus":
        if parked_counts["bus"] < 5:
            for i in range(5):
                for j in range(10):
                    if parking_slots["lantai_3"][vehicle_type][i][j] == "-":
                        parking_slots["lantai_3"][vehicle_type][i][j] = plat_nomor
                        parked_counts["bus"] += 1
                        print("Vehicle parked at lantai_3, coordinates: {}{}".format(chr(65+j), i+8))
                        return

    print("Parking is full for this vehicle type.")

# Reports
def check_vehicle_parking(plat_nomor):
    for i in range(10):
        for j in range(10):
            if parking_slots["lantai_1"]["sepeda_motor"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_1, coordinates: {}{}".format(chr(65+j), i+1)
            elif parking_slots["lantai_1"]["mobil"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_1, coordinates: {}{}".format(chr(65+j), i+3)
            elif parking_slots["lantai_2"]["sepeda_motor"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_2, coordinates: {}{}".format(chr(65+j), i+1)
            elif parking_slots["lantai_2"]["mobil"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_2, coordinates: {}{}".format(chr(65+j), i+3)
            elif parking_slots["lantai_3"]["sepeda_motor"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_3, coordinates: {}{}".format(chr(65+j), i+1)
            elif parking_slots["lantai_3"]["mobil"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_3, coordinates: {}{}".format(chr(65+j), i+6)
            elif parking_slots["lantai_3"]["bus"][i][j] == plat_nomor:
                return "Vehicle is parked at lantai_3, coordinates: {}{}".format(chr(65+j), i+8)
    return "Vehicle is not found."

def check_parking_availability():
    availability = {
        "sepeda_motor": False,
        "mobil": False,
        "bus": False
    }

    if parked_counts["sepeda_motor"] < 90:
        availability["sepeda_motor"] = True
    if parked_counts["mobil"] < 87:
        availability["mobil"] = True
    if parked_counts["bus"] < 7:
        availability["bus"] = True
    
    return availability

def total_parked_vehicles():
    return "Total parked sepeda motor: {}\nTotal parked mobil: {}\nTotal parked bus: {}".format(parked_counts["sepeda_motor"], parked_counts["mobil"], parked_counts["bus"])

def calculate_earnings():
    total_earnings = (parked_counts["sepeda_motor"] * 2000) + (parked_counts["mobil"] * 5000) + (parked_counts["bus"] * 10000)
    return "Total earnings: {}".format(total_earnings)

# Program execution flow
if login():
    while True:
        print("\n1. Park vehicle\n2. Check vehicle parking\n3. Check parking availability\n4. Total parked vehicles\n5. Calculate earnings\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            park_vehicle()
        elif choice == "2":
            plat_nomor = input("Enter the plat nomor: ")
            print(check_vehicle_parking(plat_nomor))
        elif choice == "3":
            availability = check_parking_availability()
            print("Parking availability:\nSepeda motor: {}\nMobil: {}\nBus: {}".format(availability["sepeda_motor"], availability["mobil"], availability["bus"]))
        elif choice == "4":
            print(total_parked_vehicles())
        elif choice == "5":
            print(calculate_earnings())
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Failed to login. Program terminated.")