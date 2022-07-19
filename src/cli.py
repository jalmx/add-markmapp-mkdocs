#!/usr/bin/python3

import argparse

from addmap import add_map

# options
# path = path where exist folder docs and file config yml
# exclude = paths to excludes, default
# flag_to_insert =
# clear = delete the map from file


"""All logical to create a cli with options to run
    """


def main():
    parser = argparse.ArgumentParser(
        description="Command to add markmap to index to all folders, search all index.md with a flag where insert information. Default flag <!-- Map site insert -->"
    )
    parser.add_argument(
        "-p",
        "--path",
        help="Path from folder to have inside docs folder. Default: Here (.)",
        default="./docs/",
    )
    parser.add_argument("-v", "--verbose", help="Show all logs", action="store_true")
    parser.add_argument(
        "-e",
        "--exclude",
        metavar="paths/to/exclude",
        help="Exclude directories or folders inside PATH. Ex: -e path/to/folder path/to/index.md",
        nargs="+",
        default="[]"
    )
    parser.add_argument(
        "-f",
        "--flag",
        metavar="\"#flag\"",
        help="Flag to insert the markmap only in files index.md",
        default="<!-- Map site insert -->",
    )

    argument = parser.parse_args()

    try:
        add_map(
            flag_to_insert=argument.flag,
            base_dir=argument.path,
            debug=argument.verbose,
            paths_to_exclude=(argument.exclude or [])
        )
    except:
        print("Error with the path, please exec addmap --help")


if __name__ == "__main__":
    main()
