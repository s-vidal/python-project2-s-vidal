from file_handler import FileHandler
from user import User


class CarLot:
    car_lot_location = ""
    __fleet_size = 0
    vehicle_csv = FileHandler("vehicle.csv")

    def __init__(self, car_lot_location):
        self.car_lot_location = car_lot_location

    def update_salary_by_name(self, new_employee_salary, name):
        # how to get the current user?
        current_user = User("hen")
        if current_user.user_auth("12345678") == "admin" and int(new_employee_salary):
            try:
                user_csv = FileHandler("user.csv")
                user_csv_file = user_csv.load_from_csv_as_array()
                for row in user_csv_file:
                    if row[1] == name:
                        row[5] = new_employee_salary
                user_csv.write_to_csv(user_csv_file)
                print(f"successfully updated the salary of: {name}, to: {new_employee_salary}")
                return True
            except Exception as e:
                print(e)
        else:
            print("unable to update csv file")
            return False

    def add_to_fleet(self, external_csv_fleet_file):
        try:
            # load csv files
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            external_csv_fleet = FileHandler(str(external_csv_fleet_file))
            ext_csv_fleet_file = external_csv_fleet.load_from_csv_as_array()
            # check if columns match:
            for col_name in range(len(vehicle_csv_file[0])):
                if vehicle_csv_file[0][col_name] != ext_csv_fleet_file[0][col_name]:
                    print("invalid input")
                    return False
            # append new rows to csv file
            has_successfully_appended = False
            for row in ext_csv_fleet_file[1:]:
                # check if all data is present before appending
                if len(row) == len(ext_csv_fleet_file[0]):
                    self.vehicle_csv.append_array_to_csv(row)
                    print(f"successfully appended: {row}, to file")
                    has_successfully_appended = True
            return has_successfully_appended
        except Exception as e:
            print(e)

    def get_fleet_size(self):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            self.__fleet_size = len(vehicle_csv_file) - 1
            print(self.__fleet_size)
            return self.__fleet_size
        except Exception as e:
            print(e)

    def get_all_cars_by_brand(self, brand):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            brand_list = []
            for row in vehicle_csv_file:
                if row[1].lower() == brand.lower():
                    brand_list.append(brand)
            print(len(brand_list))
            return len(brand_list)
        except Exception as e:
            print(e)


def run_tests_car_lot():
    car_lot_1 = CarLot("345")
    car_lot_1.update_salary_by_name(20, "amir")
    car_lot_1.add_to_fleet("external_csv_fleet_file.csv")
    car_lot_1.get_fleet_size()
    car_lot_1.get_all_cars_by_brand("toyota")
    car_lot_1.get_all_cars_by_brand("mitsubishi")
    car_lot_1.get_all_cars_by_brand("opel")


if __name__ == "__main__":
    run_tests_car_lot()