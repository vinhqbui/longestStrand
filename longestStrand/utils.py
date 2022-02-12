import numpy as np
from difflib import SequenceMatcher
import os


def read_binary_file(file_name: str):
    dtype = np.dtype('B')
    try:
        with open(file_name, "rb") as f:
            numpy_data = np.fromfile(f, dtype)
            return numpy_data
    except IOError:
        print('Error While Opening the file!')


def longest_strand_two_files(file1: str, file2: str):
    data1 = read_binary_file(file1)
    data2 = read_binary_file(file2)
    s = SequenceMatcher(None, data1, data2, autojunk=False)
    return s.find_longest_match()


def all_strands(path: str):
    result = dict()
    files = os.listdir(path)
    files_path = [os.path.join(path, name) for name in files]
    n = len(files_path)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            f1, f2 = files_path[i], files_path[j]
            key = (f1, f2)
            result[key] = longest_strand_two_files(f1, f2)
    return result