from file_handler import FileHandler
from logger import Logger


class Vehicle:
    vehicle_csv = FileHandler("vehicle.csv")
    vehicle_id = 0
    logger = Logger()

    def __init__(self, vehicle_id, test_time):
        self.vehicle_id = vehicle_id
        self.test_time = test_time

    def get_row_index_from_csv(self, vehicle_csv_file, _id=False):
        try:
            if not _id:
                _id = self.vehicle_id
            # get row index with given id
            for row in vehicle_csv_file:
                if row[0] == _id:
                    row_index = vehicle_csv_file.index(row)
                    return row_index
            return False
        except Exception as e:
            raise Exception(e)

    def update_vehicle_by_id(self, _id, **kwargs):
        vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
        # get index of row with given _id
        row_index = self.get_row_index_from_csv(vehicle_csv_file)
        if row_index:
            try:
                # get key's indexes and replace values
                for key, value in kwargs.items():
                    key_index = vehicle_csv_file[0].index(key)
                    vehicle_csv_file[row_index][key_index] = value
                self.vehicle_csv.write_to_csv(vehicle_csv_file)
                return True
            except Exception as e:
                self.logger.add_to_log(e)
        return False

    def get_time_to_test(self, _id=False):
        try:
            # if no id given use self.vehicle_id
            if not _id:
                _id = self.vehicle_id
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            row_index = self.get_row_index_from_csv(vehicle_csv_file, _id)
            if row_index:
                #  get last test from csv
                last_test = vehicle_csv_file[row_index][3]
                # calculate time to next test
                time_to_next_test = self.test_time - int(last_test)
                return time_to_next_test
            return False
        except Exception as e:
            self.logger.add_to_log(e)


def run_tests_vehicle():
    logger = Logger("tests.txt")
    try:
        vehicle_1 = Vehicle("3", 4)
        vehicle_1.update_vehicle_by_id("3", brand="opel", color="gr", door_count="6")
        vehicle_2 = Vehicle("4", 3)
        vehicle_2.update_vehicle_by_id("4", brand="Peugeot", color="yl")
        print(vehicle_1.get_time_to_test())
        print(vehicle_2.get_time_to_test())
    except Exception as e:
        logger.add_to_log(e, "tests.txt")


if __name__ == "__main__":
    run_tests_vehicle()