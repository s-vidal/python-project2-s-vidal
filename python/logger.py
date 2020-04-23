import os
import datetime as dt


class Logger:
    __log_files = []
    __path = ".." + os.sep + "log_folder" + os.sep

    def __init__(self, file_name=""):
        self.file_name = file_name

    @staticmethod
    def get_log_files():
        return Logger.__log_files

    def __open_log_file(self, mode, file_name=""):
        try:
            # create log file name if non given
            time = dt.datetime.now()
            log_name = "logger" + "_" + str(time.hour) + ".txt"
            if file_name:
                log_name = file_name
            f = open(Logger.__path + log_name, str(mode))
            # append log fil name to array of logs
            if log_name not in Logger.__log_files:
                Logger.__log_files.append(log_name)
            # if more than 24 files remove oldest log file
            if int(len(Logger.__log_files)) == 24:
                path_file_to_delete = Logger.__path + Logger.__log_files[0]
                os.remove(path_file_to_delete)
                Logger.__log_files.pop(0)
            return f
        except Exception as e:
            raise Exception(e)

    def read_log(self, file_name=""):
        try:
            f = self.__open_log_file("r", file_name)
            return f.read()
        except Exception as e:
            self.add_to_log(e)

    def add_to_log(self, msg,  file_name=""):
        try:
            f = self.__open_log_file("a", file_name)
            time = dt.datetime.now()
            f.write(time.strftime("%p%m%Y, %H:%M:%S") + " " + str(msg) + "\n")
        except Exception as e:
            self.add_to_log(e)


def run_tests_logger():
    logger = Logger("tests.txt")
    try:
        log_file_1 = Logger()
        log_file_1.add_to_log("log entry 1")
        print(log_file_1.read_log())
        log_file_1.add_to_log("log entry 2")
        print(log_file_1.read_log())
        print(Logger.get_log_files())
        log_file_1.add_to_log("log entry 5", "logger_18.txt")
        print(log_file_1.read_log("logger_18.txt"))
    except Exception as e:
        logger.add_to_log(e, "tests.txt")


if __name__ == "__main__":
    run_tests_logger()






