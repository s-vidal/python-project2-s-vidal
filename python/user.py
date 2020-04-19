from file_handler import FileHandler


class User:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def user_auth(name, password):
        try:
            csv_file = FileHandler.load_from_csv("user.csv")
            for row in csv_file:
                if row[1] == name and row[3] == password:
                    print("\n" + str(name) + "'s role is: " + row[4])
                    return row[4]
            else:
                print("\nincorrect username/ password ")
                return False
        except Exception as e:
            print(e)


def run_test_user():
    User.user_auth("alex", "test")
    User.user_auth("amir", "12345678")


if __name__ == "__main__":
    run_test_user()
