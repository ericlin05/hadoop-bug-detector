import os

# This class contains some utility functions that can be used by the project
class Utils:
    # This function counts number of lines in a given file by calling "wc" command in Linux
    @staticmethod
    def line_count_wc(file_path):
        return int(os.popen('wc -l ' + file_path).read().split()[0])