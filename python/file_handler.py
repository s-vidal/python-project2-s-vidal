import csv
import os
from csv import DictWriter


class FileHandler:
    __file_path = ".." + os.sep + "csv" + os.sep
    file_name = ""

    def __init__(self, file_name):
        self.file_name = file_name
        self.__file_path = ".." + os.sep + "csv" + os.sep + self.file_name

    def load_from_csv_as_array(self, print_csv=False):
        try:
            with open(str(self.__file_path), newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                file_data = []
                for row in reader:
                    file_data.append(row)
                    if print_csv == "print":
                        print(row)
                return file_data
        except Exception as e:
            print(e)

    def load_from_csv_as_dict(self):
        reader = csv.DictReader(open(self.__file_path))
        csv_dict = {}
        for row in reader:
            key = row.pop('id')
            csv_dict[key] = row
        print(csv_dict)
        return csv_dict

    def append_array_to_csv(self, data):
        try:
            with open(str(self.__file_path), "a+", newline="") as csv_file:
                append_to_file = csv.writer(csv_file, delimiter=',')
                for row in self.load_from_csv_as_array():
                    if row[0] == data[0]:
                        return False
                append_to_file.writerow(data)
                return True
        except Exception as e:
            print(e)

    def append_dict_to_csv(self, data):
        try:
            csv_data = self.load_from_csv_as_array()
            field_names = csv_data[0]
            if list(data.keys()) == field_names:
                try:
                    with open(self.__file_path, "a+", newline="") as write_obj:
                        dict_writer = DictWriter(write_obj,  fieldnames=field_names)
                        for row in csv_data:
                            if row[0] == data.get("id"):
                                return False
                        dict_writer.writerow(data)
                        return True
                except Exception as e:
                    raise Exception(e)
        except Exception as e:
            print(e)

    def remove_row_from_csv(self, user_id):
        try:
            csv_array = self.load_from_csv_as_array()
            for row in csv_array:
                if (row[0]) == str(user_id):
                    csv_array.remove(row)
                    with open(str(self.__file_path), "w", newline="") as write_file:
                        writer = csv.writer(write_file, delimiter=',')
                        writer.writerows(csv_array)
                        print(f"successfully removed row with id: {user_id}, from csv file")
                        return True
            print("id not found")
            return False
        except Exception as e:
            print(e)


def run_tests_file_handler():
    user_csv = FileHandler("user.csv")
    user_csv.load_from_csv_as_array("print")
    print("\n")
    vehicle_csv = FileHandler("vehicle.csv")
    vehicle_csv.load_from_csv_as_array("print")
    array_to_append_1 = ['14', 'Alex', 'ber', '12345678', 'student', '10', 'student']
    object_to_append_1 = {'id': '15', 'first_name': 'Jon', 'last_name': 'tek', 'password': '423', 'position': 'teacher', 'salary': 'Na', 'role': 'teacher'}
    user_csv.append_array_to_csv(array_to_append_1)
    user_csv.append_dict_to_csv(object_to_append_1)
    print("\n")
    user_csv.load_from_csv_as_dict()
    print("\n")
    user_csv.remove_row_from_csv("9")
    print("\n")
    user_csv.remove_row_from_csv("18")


if __name__ == "__main__":
    run_tests_file_handler()





