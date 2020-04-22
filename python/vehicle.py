from file_handler import FileHandler


class Vehicle:
    vehicle_csv = FileHandler("vehicle.csv")

    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_row_index_from_csv(self, vehicle_csv_file):
        try:
            for row in vehicle_csv_file:
                if row[0] == self.vehicle_id:
                    row_index = vehicle_csv_file.index(row)
                    return row_index
        except Exception as e:
            raise Exception(e)

    def update_vehicle_by_id(self, _id, **kwargs):
        vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
        # get index of row with given _id
        row_index = self.get_row_index_from_csv(vehicle_csv_file)
        # get key's indexes and replace values
        try:
            for key, value in kwargs.items():
                key_index = vehicle_csv_file[0].index(key)
                vehicle_csv_file[row_index][key_index] = value
            self.vehicle_csv.write_to_csv(vehicle_csv_file)
            print(f"Updated row with id {_id}: \n", vehicle_csv_file)
            return True
        except Exception as e:
            raise Exception(e)


def run_tests_vehicle():
    vehicle_1 = Vehicle("3")
    vehicle_1.update_vehicle_by_id("3", brand="opel", color="gr", door_count="6")
    print("\n")
    vehicle_2 = Vehicle("4")
    vehicle_2.update_vehicle_by_id("4", brand="Peugeot", color="yl")


if __name__ == "__main__":
    run_tests_vehicle()