from file_handler import FileHandler


class User:
    name = ""
    
    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def user_auth(self, password, name=""):
        try:
            if not name:
                name = self.name
            user_csv = FileHandler("user.csv")
            csv_file = user_csv.load_from_csv_as_array()
            for row in csv_file:
                if row[1] == name and row[3] == password:
                    print("\n" + str(name) + "'s role is: " + row[4])
                    return row[6]
            print("\nincorrect username/ password ")
            return False
        except Exception as e:
            print(e)


def run_test_user():
    user_1 = User("")
    user_1.user_auth( "test", "alex")
    user_2 = User("amir")
    user_2.user_auth("12345678")


if __name__ == "__main__":
    run_test_user()
