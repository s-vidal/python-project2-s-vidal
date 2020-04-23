from file_handler import FileHandler
from logger import Logger


class User:
    name = ""
    user_csv = FileHandler("user.csv")
    logger = Logger()
    
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
            csv_file = self.user_csv.load_from_csv_as_array()
            for row in csv_file:
                if row[1] == name and row[3] == password:
                    return row[6]
            return False
        except Exception as e:
            self.logger.add_to_log(e)

    @staticmethod
    def get_users_by_role(role):
        try:
            user_csv_file = User.user_csv.load_from_csv_as_array()
            # create array with names by role
            users_with_role = []
            for row in user_csv_file[1:]:
                if row[6] == str(role):
                    users_with_role.append(row[1])
            if len(users_with_role) > 0:
                return users_with_role
            return False
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def add_user(_id, **kwargs):
        user_csv_file = User.user_csv.load_from_csv_as_array()
        try:
            array_to_append = [_id]
            # check if keys correspond to columns
            for key, value in kwargs.items():
                if key not in user_csv_file[0]:
                    return False
                array_to_append.append(value)
            # if all keys are passed append to csv
            if len(array_to_append) == len(user_csv_file[0]):
                User.user_csv.append_array_to_csv(array_to_append)
                return True
            return False
        except Exception as e:
            User.logger.add_to_log(e)


def run_test_user():
    logger = Logger("tests.txt")
    try:
        user_1 = User("")
        print(user_1.user_auth( "test", "alex"))
        user_2 = User("amir")
        print(user_2.user_auth("12345678"))
        User.add_user('16', first_name='Terry', last_name='J.A', passwor='1123', position='student', salary='Na', role='student')
        User.add_user('17', first_name='Thoma', last_name='J.P', password='345', position='assistant', salary='4', role='assistant')
        User.add_user('18', first_name='Thoma', password ='345', salary='4', role='assistant')
        User.add_user('19', wrong_key='na', last_name='J.P', password='345', position='assistant', salary='4', role='assistant')
    except Exception as e:
        logger.add_to_log(e, "tests.txt")


if __name__ == "__main__":
    run_test_user()
