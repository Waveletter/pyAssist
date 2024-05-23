import argparse
import sys

from pathlib import Path


def comprehend_package(file: Path) -> (str, str, str):
    """
    Returns name of the module, type and a version, if present.
    :param file:
    :return: name type version
    """
    type_delim = file.name.rfind('.')
    if type_delim == -1:
        ftype = None
    else:
        ftype = file.name[type_delim:]

    name = file.name[:type_delim]

    return name, ftype, None

def main() -> None:
    parser = argparse.ArgumentParser(prog='pyAssistant',
                                     description='this app assists you in deploying python packages to offline indexes')

    parser.add_argument('-s', '--source', dest='source_dir', type=str,
                        help='source foulder that contains the packages')

    parser.add_argument('-t', '--target', dest='target_dir', type=str, default='.',
                        help='destination folder for packages to be unpacked into')

    args = parser.parse_args()

    if args.source_dir and args.target_dir:
        s_path = Path(args.source_dir)
        if not s_path.exists():
            raise Exception("Source directory does not exist")
        if not s_path.is_dir():
            raise Exception("Source is not a directory")

        files = [f for f in s_path.iterdir() if f.is_file()]
        if len(files) == 0:
            raise Exception("Source dir does not contain any files")

        print(f"Detected {len(files)} files to be distributed")

        packages = [comprehend_package(f) for f in files]

        for package in packages:
            print(f"Module {package[0]} typed as {package[1]} version {package[2]}")




if __name__ == "__main__":
    main()


