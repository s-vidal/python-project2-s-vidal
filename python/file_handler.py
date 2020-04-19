import csv


class FileHandler:
    @staticmethod
    def load_from_csv(file_name):
        try:
            file_path = "../csv/" + str(file_name)
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
    def append_to_csv(file_name, data):
        try:
            file_path = "../csv/" + str(file_name)
            with open(str(file_path), "a+", newline="") as csv_file:
                append_to_file = csv.writer(csv_file, delimiter=',')
                for row in FileHandler.load_from_csv("user.csv"):
                    if row[0] == data[0]:
                        return False
                append_to_file.writerow(data)
                return True
        except Exception as e:
            print(e)


def run_tests_file_handler():
    FileHandler.load_from_csv("user.csv")
    print("\n")
    FileHandler.load_from_csv("vehicle.csv")
    print("\n")
    FileHandler.load_from_csv("wrong_file.csv")
    print("\n")
    data_to_append_1 = ['14', 'Alex', 'bernstein', '12345678', 'student', '10', 'student']
    FileHandler.append_to_csv("user.csv", data_to_append_1)


if __name__ == "__main__":
    run_tests_file_handler()





