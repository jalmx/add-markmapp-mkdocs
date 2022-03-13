# Script for add markmap to Markdown in Mkdocs

```bash
usage: cli.py [-h] [-p PATH] [-v] [-e paths/to/exclude [paths/to/exclude ...]]

Command to add markmap to index to all folders, search all index.md with a flag where insert information

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path from folder to have inside docs folder. Default: Here (.)
  -v, --verbose         Show all logs
  -e paths/to/exclude [paths/to/exclude ...], --exclude paths/to/exclude [paths/to/exclude ...]
                        Exclude directories or folders inside PATH. Ex: -e path/to/exclude path/to/exclude2
```