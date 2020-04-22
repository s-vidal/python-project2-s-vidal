import os
import datetime as dt


class Logger:
    __log_files = []
    __path = ".." + os.sep + "log_folder" + os.sep

    def get_log_files(self):
        print(Logger.__log_files)
        return Logger.__log_files

    def __open_log_file(self, file_name, mode):
        try:
            time = dt.datetime.now()
            log_name = "logger" + "_" + str(time.hour) + ".txt"
            if file_name:
                log_name = file_name
            f = open(Logger.__path + log_name, str(mode))
            if log_name not in Logger.__log_files:
                Logger.__log_files.append(log_name)
            if int(len(Logger.__log_files)) == 24:
                path_file_to_delete = Logger.__path + Logger.__log_files[0]
                os.remove(path_file_to_delete)
                Logger.__log_files.pop(0)
            return f
        except Exception as e:
            raise Exception(e)

    def read_log(self, file_name=False):
        try:
            f = self.__open_log_file(file_name, "r")
            print(f.read())
            return f.read()
        except Exception as e:
            print(e)

    def add_to_log(self, msg,  file_name=False):
        try:
            f = self.__open_log_file(file_name, "a")
            time = dt.datetime.now()
            f.write(time.strftime("%p%m%Y, %H:%M:%S") + " " + str(msg) + "\n")
            print(f"successfully added: '{msg}' to log file: {f.name}")
        except Exception as e:
            print(e)


def run_tests_logger():
    log_file_1 = Logger()
    log_file_1.add_to_log("log entry 1")
    log_file_1.read_log()
    log_file_1.add_to_log("log entry 2")
    log_file_1.read_log()
    log_file_1.get_log_files()
    log_file_1.add_to_log("log entry 5", "logger_18.txt")
    log_file_1.read_log("logger_18.txt")


if __name__ == "__main__":
    run_tests_logger()






