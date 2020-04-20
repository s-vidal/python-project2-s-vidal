import os
import datetime as dt


class Logger:
    __log_files = []

    def get_log_files(self):
        print(Logger.__log_files)
        return Logger.__log_files

    def __open_log_file(self, mode):
        try:
            time = dt.datetime.now()
            log_name = "logger" + "_" + str(time.hour) + ".txt"
            f = open(".." + os.sep + "log_folder" + os.sep + log_name, str(mode))
            if int(len(Logger.__log_files)) == 24:
                Logger.__log_files.pop(0)
            if log_name not in Logger.__log_files:
                Logger.__log_files.append(log_name)
            return f
        except Exception as e:
            raise Exception(e)

    def read_log(self):
        try:
            f = self.__open_log_file("r")
            print(f.read())
            return f.read()
        except Exception as e:
            print(e)

    def add_to_log(self, msg):
        try:
            f = self.__open_log_file("a")
            time = dt.datetime.now()
            f.write(time.strftime("%p%m%Y, %H:%M:%S") + " " + str(msg) + "\n")
            print(f"successfully added: '{msg}' to log")
        except Exception as e:
            print(e)


def run_test_logger():
    log_file_1 = Logger()
    log_file_1.add_to_log("log entry 1")
    log_file_1.read_log()
    log_file_1.add_to_log("log entry 2")
    log_file_1.read_log()
    log_file_1.get_log_files()


if __name__ == "__main__":
    run_test_logger()
