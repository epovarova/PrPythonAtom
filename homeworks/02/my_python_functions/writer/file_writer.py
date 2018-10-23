import os
import pickle as pkl

class FileWriter:

    def __init__(self, path):
        """path - путь до файла"""
        if self._check_path(os.path.split(path)[0]):
            self.path_ = path
            self.file = None
        else:
            raise Exception("Init error!")
    def __enter__(self):
        self.file = open(self.path_, "a+")
        return self
    def __exit__(self, type, value, traceback):
         self.file.close()
    @property
    def path(self):
        return self.path_
    @path.setter
    def path(self, new_path):
        if self._check_path(os.path.split(new_path)[0]):
            self.path = new_path
        else:
            raise Exception("Set path error!")
    def del_path(self):
        del self.path

    def _check_path(self, path):
        return os.path.exists(path)

    def print_file(self):
        #self.file = open(self.file, "a+")
        self.file.seek(0)
        for line in self.file:
            print(line)

    def write(self, some_string):
        self.file = open(self.file, "a+")
        self.file.write(some_string)

    def save_yourself(self, file_name):
        with open(file_name, "wb") as pf:
            pkl.dump(self.__dict__, pf)

    @classmethod
    def load_file_writer(cls, pickle_file):
        with open(pickle_file, "rb") as pf:
            file = pkl.load(pf)
        return file

a = FileWriter('./new_file.txt')
with a as fw:
    fw.print_file()
