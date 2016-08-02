import os

class Utils:
    @staticmethod
    def line_count_wc(file_path):
        return int(os.popen('wc -l ' + file_path).read().split()[0])