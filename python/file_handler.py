import csv
import os
from csv import DictWriter


class FileHandler:
    @staticmethod
    def __get_file_path(file_name):
        file_path = ".." + os.sep + "csv" + os.sep + str(file_name)
        return file_path

    @staticmethod
    def load_from_csv(file_name):
        try:
            file_path = FileHandler.__get_file_path(file_name)
            with open(str(file_path), newline='') as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                file_data = []
                for row in reader:
                    file_data.append(row)
                    if __name__ == "__main__":
                        print(row)
                return file_data
        except Exception as e:
            print(e)

    @staticmethod
    def append_array_to_csv(file_name, data):
        try:
            file_path = FileHandler.__get_file_path(file_name)
            with open(str(file_path), "a+", newline="") as csv_file:
                append_to_file = csv.writer(csv_file, delimiter=',')
                for row in FileHandler.load_from_csv(file_name):
                    if row[0] == data[0]:
                        return False
                append_to_file.writerow(data)
                return True
        except Exception as e:
            print(e)

    @staticmethod
    def append_dict_to_csv(file_name, data):
        try:
            file_path = FileHandler.__get_file_path(file_name)
            csv_data = FileHandler.load_from_csv(file_name)
            field_names = csv_data[0]
            if list(data.keys()) == field_names:
                try:
                    with open(str(file_path), "a+", newline="") as write_obj:
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


def run_tests_file_handler():
    FileHandler.load_from_csv("user.csv")
    print("\n")
    FileHandler.load_from_csv("vehicle.csv")
    print("\n")
    FileHandler.load_from_csv("wrong_file.csv")
    print("\n")
    array_to_append_1 = ['14', 'Alex', 'ber', '12345678', 'student', '10', 'student']
    object_to_append_1 = {'id': '15', 'first_name': 'Jon', 'last_name': 'tek', 'password': '423', 'position': 'teacher', 'salary': 'Na', 'role': 'teacher'}
    FileHandler.append_array_to_csv("user.csv", array_to_append_1)
    print("\n")
    FileHandler.append_dict_to_csv("user.csv", object_to_append_1)


if __name__ == "__main__":
    run_tests_file_handler()





