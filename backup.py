import os
import shutil
from datetime import datetime


def get_source() -> str:
    '''Ask user for source path of the files and folder he/she wants to copy/move
    Args:
        none
    Returns:
        (str) Source path of the files and folders
    '''
    src_path = ''
    try:
        src_path = input('\nEnter source path: ')
        return src_path
    except Exception as exception:
        raise exception


def get_destination() -> str:
    '''Ask user for destination path where he/she wants to copy/move the files and folders
    Args:
        none
    Returns:
        (str) Destination path for the files and folders
    '''
    dst_path = ''
    try:
        dst_path = input('\nEnter destination path: ')
        return dst_path
    except Exception as exception:
        raise exception


def get_operation() -> str:
    '''Ask user for operation he/she wants to perform on the files
    Args:
        none
    Returns:
        (str) Operation to be performed
    '''
    operation = ''
    while operation.lower() not in ['copy', 'move']:
        operation = input('\nDo you want to copy or move the files? Type copy or move.\n').lower()
        if operation == 'copy':
            return 'copy'
        if operation == 'move':
            return 'move'
        else:
            print('Please enter a valid operation.\n')


def get_date() -> str:
    '''Get current date in this format: _dd_mm_YYYY
    Args:
        none
    Returns:
        (str) Current date in the given format
    '''
    current_date = str(datetime.now().strftime('_%d_%m_%Y'))
    return current_date


def rename_items(directory: str):
    '''Rename files and folders in the directory to include currennt date in a specific format. See {get_date()} method
    Args:
        directory: directory in which renaming has to be done
    Returns:
        none
    '''
    items_list = os.listdir(directory)
    os.chdir(directory)
    for item_name in items_list:
        file_name = os.path.splitext(item_name)[0]
        file_extension = os.path.splitext(item_name)[1]
        os.rename(item_name, file_name + get_date() + file_extension)


root_src_dir = os.path.join('', get_source())
root_dst_dir = os.path.join('', get_destination())
user_operation = get_operation()


def perform_opertation():
    '''Perform the opertation told by the user on the files and folders at user specified path.
    Args:
        none
    Returns:
        none
    '''
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir)

        if not os.path.exists(dst_dir):
            os.mkdir(dst_dir)

        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            if user_operation is 'copy':
                shutil.copy2(src_file, dst_dir)
                # print('\nCopy complete\n')
            elif user_operation is 'move':
                shutil.move(src_file, dst_dir)
                # print('\nMove complete\n')


def main():
    '''Starts the program
    Args:
        none
    Returns:
        none
    '''
    perform_opertation()
    rename_items(root_dst_dir)

    # # Restart if user wants to..
    # restart = input(
    #     '\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
    # while restart not in ['yes', 'no']:
    #     print("Invalid input. Please type 'yes' or 'no'.")
    #     restart = input(
    #         '\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
    # if restart == 'yes':
    #     main()
    # else:
    #     print("Good Bye!")
    #     return

if __name__ == "__main__":
    main()
