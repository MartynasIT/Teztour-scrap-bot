import pathlib
from datetime import date


class Utils():
    def get_current_dir(self):
        return pathlib.Path.cwd()

    def get_current_date(self):
        return date.today().strftime('%Y-%m-%d')

