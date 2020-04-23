import csv
import os
from csv import DictWriter
from logger import Logger


class FileHandler:
    __file_path = ".." + os.sep + "csv" + os.sep
    file_name = ""
    logger = Logger()

    def __init__(self, file_name):
        self.file_name = file_name
        self.__file_path = ".." + os.sep + "csv" + os.sep + self.file_name

    def load_from_csv_as_array(self, print_csv="false"):
        try:
            # load as arrays using csv module
            with open(str(self.__file_path), newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                file_data = []
                for row in reader:
                    file_data.append(row)
                    if print_csv == "print":
                        print(row)
                return file_data
        except Exception as e:
            self.logger.add_to_log(e)

    def load_from_csv_as_dict(self):
        # load as dict using csv module
        reader = csv.DictReader(open(self.__file_path))
        csv_dict = {}
        for row in reader:
            # use id as dict key
            key = row.pop('id')
            csv_dict[key] = row
        return csv_dict

    def append_array_to_csv(self, data):
        try:
            with open(str(self.__file_path), "a+", newline="") as csv_file:
                append_to_file = csv.writer(csv_file, delimiter=',')
                # check if id is not already in file
                for row in self.load_from_csv_as_array():
                    if row[0] == data[0]:
                        return False
                append_to_file.writerow(data)
                return True
        except Exception as e:
            self.logger.add_to_log(e)

    def append_dict_to_csv(self, data):
        try:
            csv_data = self.load_from_csv_as_array()
            field_names = csv_data[0]
            # check if column names match
            if list(data.keys()) == field_names:
                try:
                    with open(self.__file_path, "a+", newline="") as write_obj:
                        dict_writer = DictWriter(write_obj,  fieldnames=field_names)
                        # check if id is not already in file
                        for row in csv_data:
                            if row[0] == data.get("id"):
                                return False
                        dict_writer.writerow(data)
                        return True
                except Exception as e:
                    raise Exception(e)
        except Exception as e:
            self.logger.add_to_log(e)

    def write_to_csv(self, csv_array):
        try:
            # write to csv file using csv module
            with open(str(self.__file_path), "w", newline="") as write_file:
                writer = csv.writer(write_file, delimiter=',')
                writer.writerows(csv_array)
        except Exception as e:
            self.logger.add_to_log(e)

    def remove_row_from_csv(self, user_id):
        try:
            csv_array = self.load_from_csv_as_array()
            # find row with given id
            for row in csv_array:
                if (row[0]) == str(user_id):
                    # remove row
                    csv_array.remove(row)
                    self.write_to_csv(csv_array)
                    return True
            return False
        except Exception as e:
            self.logger.add_to_log(e)

    def update_csv(self, user_id, new_row):
        # check if id's match
        if new_row[0] == user_id:
            try:
                csv_array = self.load_from_csv_as_array()
                # update row in array
                csv_array = [new_row if row[0] == user_id else row for row in csv_array]
                # update csv file
                self.write_to_csv(csv_array)
                return True
            except Exception as e:
                self.logger.add_to_log(e)
        return False


def run_tests_file_handler():
    logger = Logger("tests.txt")
    try:
        user_csv = FileHandler("user.csv")
        user_csv.load_from_csv_as_array("print")
        print("\n")
        vehicle_csv = FileHandler("vehicle.csv")
        vehicle_csv.load_from_csv_as_array("print")
        array_to_append_1 = ['14', 'Alex', 'ber', '12345678', 'student', '10', 'student']
        object_to_append_1 = {'id': '15', 'first_name': 'Jon', 'last_name': 'tek', 'password': '423', 'position': 'teacher', 'salary': '8', 'role': 'teacher'}
        user_csv.append_array_to_csv(array_to_append_1)
        user_csv.append_dict_to_csv(object_to_append_1)
        print("\n")
        print(user_csv.load_from_csv_as_dict())
        user_csv.remove_row_from_csv("")
        user_csv.remove_row_from_csv("18")
        new_row = ['7', 'Jhon', 'ber', '12345678', 'student', '8', 'student']
        user_csv.update_csv("7", new_row)
        user_csv.update_csv("8", new_row)
    except Exception as e:
        logger.add_to_log(e, "tests.txt")



if __name__ == "__main__":
    run_tests_file_handler()





