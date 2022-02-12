from utils import *


class FileWithStrand:
    def __init__(self, file_name, offset, longest):
        self.file_name = file_name
        self.offset = offset
        self.longest = longest

    def __eq__(self, other):
        if self.offset == other.offset and \
                self.file_name == other.file_name and self.longest == other.longest:
            return True
        return False


def longest_strand(info: dict):
    # Find the length of longest strand
    longest = 0
    for k, v in info.items():
        if v.size > longest:
            longest = v.size

    # Filter out all the strand that
    same_longest = []
    for k, v in info.items():
        if v.size == longest:
            file_name1, file_name2 = k
            file1 = FileWithStrand(file_name1, v.a, longest)
            file2 = FileWithStrand(file_name2, v.b, longest)
            added = False

            if len(same_longest) > 0:
                for pack in same_longest:
                    if file1 in pack and file2 not in pack:
                        pack.append(file2)
                        added = True
                    elif file2 in pack and file1 not in pack:
                        pack.append(file1)
                        added = True
            if not added:
                same_longest.append([file1, file2])

    return same_longest, longest


information = all_strands('./data')
result, strand_size = longest_strand(information)
print('Length of strand: ', strand_size)
for file_pack in result:
    for file in file_pack:
        print(f'File: {file.file_name}, Offset: {file.offset}')
