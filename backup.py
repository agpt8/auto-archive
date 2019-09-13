import os
import shutil
from datetime import datetime

from validator import is_path_exists_or_creatable


def get_source() -> str:
    """Ask user for source path of the files and folder he/she wants to copy/move
    Args:
        none
    Returns:
        (str) Source path of the files and folders
    """
    # TODO: Make changes to code so that it asks the user for source path till valid path is provided.
    src_path = ''
    try:
        src_path = input('\nEnter source path: ')
        valid_src_path = is_path_exists_or_creatable(src_path)
        if valid_src_path:
            return src_path
        else:
            print('\nPlease enter a valid source path.\n')
    except Exception as exception:
        raise exception


def get_destination() -> str:
    """Ask user for destination path where he/she wants to copy/move the files and folders
    Args:
        none
    Returns:
        (str) Destination path for the files and folders
    """
    # TODO: Make changes to code so that it asks the user for destination path till valid path is provided.
    dst_path = ''
    try:
        dst_path = input('\nEnter destination path: ')
        valid_dst_path = is_path_exists_or_creatable(dst_path)
        if valid_dst_path:
            return dst_path
        else:
            print('\nPlease enter a valid destination path.\n')
    except Exception as exception:
        raise exception


def get_operation() -> str:
    """Ask user for operation he/she wants to perform on the files
    Args:
        none
    Returns:
        (str) Operation to be performed
    """
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
    """Get current date in this format: _dd_mm_YYYY
    Args:
        none
    Returns:
        (str) Current date in the given format
    """
    current_date = str(datetime.now().strftime('_%d_%m_%Y'))
    return current_date


root_src_dir = os.path.join('', get_source())
root_dst_dir = os.path.join('', get_destination())
user_operation = get_operation()


def change_name(path_: str, item: str, old: str, new: str):
    """Change the name of the files and folders in given path
    Args:
        path_: Path in which names have to be changed
        item: files/folders
        old: old name
        new: new name
    Returns:
        none
    """
    # FIXME: Partially working. Sometimes folders doesn't get renamed along with files inside.
    new_path = os.path.join(path_, item)
    new_name = os.path.join(path_, item.replace(old, new))
    os.rename(new_path, new_name)


def folder_recurse(folder_path: str, old: str, new: str):
    '''Recurse through folders to rename the folder iteself and items inside.
    Args:
        folder_path: Path of folder to recurse
        old: old name
        new: new name to be replaced
    '''
    # FIXME: Same error as function change_name()
    for path, subdirs, files in os.walk(folder_path):
        for name in files:
            if old in name:
                change_name(path, name, old, new)
        for sub_dir in subdirs:
            if old in sub_dir:
                change_name(path, sub_dir, old, new)


def rename_items(directory: str):
    '''Rename files and folders in the directory to include currennt date in a specific format. See get_date() method
    Args:
        directory: directory in which renaming has to be done
    Returns:
        none
    '''
    # FIXME: Renaming does not rename sub-folder and files. Current using this function for renaming.
    items_list = os.listdir(directory)
    os.chdir(directory)
    for item_name in items_list:
        file_name = os.path.splitext(item_name)[0]
        file_extension = os.path.splitext(item_name)[1]
        new_name = file_name + get_date() + file_extension
        os.rename(item_name, new_name)
        # folder_recurse(root_dst_dir, file_name, new_name)


def perform_operation():
    """Perform the operation told by the user on the files and folders at user specified path.
    Args:
        none
    Returns:
        none
    """
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
            elif user_operation is 'move':
                # FIXME: moving the files does not move the folder but rather make a copy of them
                shutil.move(src_file, dst_dir)


def main():
    """Starts the program
    Args:
        none
    Returns:
        none
    """
    perform_operation()
    rename_items(root_dst_dir)

    # TODO: Ask user if he/she wants to start over.
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
