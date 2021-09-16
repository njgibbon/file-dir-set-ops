import os
import sys
import argparse


def main():
    intersection_choices = ['intersection', 'intersect']
    union_choices = ['union']
    complement_choices = ["complement", 'difference', 'diff']
    operation_choices = intersection_choices + union_choices + complement_choices

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--version', '-version', '--v', '-v', action='version', version='0.0.0.1')
    arg_parser.add_argument('--operation', '-operation', '--op', '-op', action='store', type=str, required=True, choices=operation_choices, help='Set operation to perform.')
    arg_parser.add_argument('--dir-paths', '-dir-paths', '--paths', '-paths', action='store', type=str, required=True, nargs='+', help='Directory paths for sets of files that will be used in Set operations.')
    args = arg_parser.parse_args()

    operation = args.operation
    dir_paths = args.dir_paths

    dir_paths_length = len(DIR_PATHS)

    if dir_paths_length < 2:
        print("ERROR: At least 2 valid directory paths must be input to perform Set operations.")
        sys.exit(1)

    file_set_main = set()
    file_set_rest_list = []
    counter = 0

    for dir_path in dir_paths:
        if counter == 0:
            file_set_main = get_file_set_from_dir_path(dir_path)
        else:
            file_set_rest_list.append(get_file_set_from_dir_path(dir_path))
        counter = counter + 1

    if operation in intersection_choices:
        result = file_set_main.intersection(*file_set_rest_list)
    elif operation in union_choices:
        result = file_set_main.union(*file_set_rest_list)
    elif operation in complement_choices:
        result = file_set_main.difference(*file_set_rest_list)

    print_items_with_newline(result)


def get_file_set_from_dir_path(dir_path):
    file_set = set()
    for obj in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, obj)):
            file_set.add(obj)
    return file_set


def print_items_with_newline(items):
    for item in items:
        print(item)


if __name__ == '__main__':
    main()
