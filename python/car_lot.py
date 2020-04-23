from file_handler import FileHandler
from user import User
from logger import Logger


class CarLot:
    car_lot_location = ""
    __fleet_size = 0
    vehicle_csv = FileHandler("vehicle.csv")
    user_csv = FileHandler("user.csv")
    logger = Logger()

    def __init__(self, car_lot_location):
        self.car_lot_location = car_lot_location

    def update_salary_by_name(self, new_employee_salary, name, user_name, user_password):
        # verify if current user has admin rights
        current_user = User(user_name)
        if current_user.user_auth(user_password) == "admin" and int(new_employee_salary):
            try:
                user_csv_file = self.user_csv.load_from_csv_as_array()
                # update salary
                for row in user_csv_file:
                    if row[1] == name:
                        row[5] = new_employee_salary
                self.user_csv.write_to_csv(user_csv_file)
                return True
            except Exception as e:
                self.logger.add_to_log(e)
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
                    return False
            # append new rows to csv file
            for row in ext_csv_fleet_file[1:]:
                # check if all data is present before appending
                if len(row) == len(ext_csv_fleet_file[0]):
                    self.vehicle_csv.append_array_to_csv(row)
                    return True
            return False
        except Exception as e:
            self.logger.add_to_log(e)

    def get_fleet_size(self):
        try:
            # create self.fleet_size
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            self.__fleet_size = len(vehicle_csv_file) - 1
            return self.__fleet_size
        except Exception as e:
            self.logger.add_to_log(e)

    def get_all_cars_by_brand(self, brand):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            brand_list = []
            # find rows with given brand
            for row in vehicle_csv_file:
                if row[1].lower() == brand.lower():
                    brand_list.append(brand)
            return len(brand_list)
        except Exception as e:
            self.logger.add_to_log(e)

    # wasn't able to figure that one out
    def get_all_cars_by_filter(self, and_or="and", **kwargs):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_dict()
            matches = []
            for i in list(range(1, len(vehicle_csv_file)+1)):
                for t in range(len(list(kwargs.keys()))):
                    if vehicle_csv_file.get(str(i)).get(list(kwargs.keys())[t]) == list(kwargs.values())[t]:
                        continue
                matches.append(vehicle_csv_file.get(str(i)))
            return matches
        except Exception as e:
            self.logger.add_to_log(e)

    def how_many_own_more_than_one_car(self):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            # create a list will all the owners
            all_vehicle_owners = []
            for row in vehicle_csv_file[1:]:
                # check if it's a car and append
                if int(row[5]) > 1:
                    all_vehicle_owners.append(row[2])
            # find duplicates in all_vehicle_owners array
            owners_with_more_than_one_car = set([owner for owner in all_vehicle_owners if all_vehicle_owners.count(owner) > 1])
            return owners_with_more_than_one_car
        except Exception as e:
            self.logger.add_to_log(e)

    def does_employee_have_car(self, name=""):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            # get array with all employees names
            employees = User.get_users_by_role("employee")
            # check if employee owns a car
            employees_who_own_cars = []
            for employee_name in employees:
                for row in vehicle_csv_file:
                    if row[2] == employee_name:
                        employees_who_own_cars.append(employee_name)
            if len(employees_who_own_cars) > 0:
                return set(employees_who_own_cars)
            return False
        except Exception as e:
            self.logger.add_to_log(e)

    def get_all_employee_who_own_car_brand(self, brand):
        try:
            vehicle_csv_file = self.vehicle_csv.load_from_csv_as_array()
            # get all employees who own cars
            employees_who_own_cars = list(self.does_employee_have_car())
            employees_with_car_brand = []
            # check if employees with car have given brand
            for row in vehicle_csv_file:
                if row[1] == brand and row[2] in employees_who_own_cars:
                    employees_with_car_brand.append(row[2])
            if len(employees_with_car_brand) > 0:
                return employees_with_car_brand
            return False
        except Exception as e:
            self.logger.add_to_log(e)


def run_tests_car_lot():
    logger = Logger("tests.txt")
    try:
        car_lot_1 = CarLot("345")
        car_lot_1.update_salary_by_name(20, "amir", "hen", "12345678")
        car_lot_1.add_to_fleet("external_csv_fleet_file.csv")
        print(car_lot_1.get_fleet_size())
        print("\n")
        print(car_lot_1.get_all_cars_by_brand("toyota"))
        print("\n")
        car_lot_1.get_all_cars_by_filter("and", brand="toyota", door_count = "4")
        print(car_lot_1.how_many_own_more_than_one_car())
        print("\n")
        print(car_lot_1.does_employee_have_car())
        print("\n")
        print(car_lot_1.get_all_employee_who_own_car_brand("toyota"))
    except Exception as e:
        logger.add_to_log(e, "tests.txt")


if __name__ == "__main__":
    run_tests_car_lot()