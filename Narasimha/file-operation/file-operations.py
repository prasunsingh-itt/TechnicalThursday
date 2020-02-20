
import os
import re


def count_dirs(dirnames, folder_count):
    for dir_name in dirnames:
        folder_count = folder_count+1
    return folder_count


def count_dirs_excl(dirnames, dirpath, exclude_dir_name, folder_count):
    for dir_name in dirnames:
        if dir_name.endswith(exclude_dir_name) is False and re.search("/"+exclude_dir_name+"/", dirpath) is None:
            folder_count = folder_count+1
    return folder_count


def count_files_excl(filenames, exclude_file_ext, file_count):
    for file_name in filenames:
        if exclude_file_ext is not None and file_name.endswith(exclude_file_ext) is False:
            file_count = file_count+1
    return file_count


def count_files(filenames, file_count):
    for file_name in filenames:
        file_count = file_count+1
    return file_count


def count_dirs_files(exclude_dir_name, exclude_file_ext, path):
    file_count = folder_count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        if exclude_dir_name is None or len(exclude_dir_name) == 0:
            folder_count = count_dirs(dirnames, folder_count)
        else:
            folder_count = count_dirs_excl(
                dirnames, dirpath, exclude_dir_name, folder_count)

        if exclude_file_ext is None or len(exclude_file_ext) == 0:
            file_count = count_files(filenames, file_count)
        else:
            file_count = count_files_excl(
                filenames, exclude_file_ext, file_count)

    print("{:,} files, {:,} folders".format(file_count, folder_count))


count_dirs_files(
    "Narasimha", ".pyc", "/Users/intime/Desktop/Python-Learning/TechnicalThursday/")
