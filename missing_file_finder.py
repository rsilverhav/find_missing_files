import os
import sys
from collections import namedtuple

FilesInfo = namedtuple('FileInfo', ['files', 'files_sizes', 'files_path', 'total_size', 'file_count'])

def get_files_size_dir(directory):
    total_size = 0
    file_count = 0
    fs = []
    files_sizes = {}
    files_path = {}
    for root, subdirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            size = os.stat(path).st_size
            total_size += size
            file_count += 1
            fs.append(f)
            files_sizes[f] = size
            files_path[f] = path
    return FilesInfo(fs, files_sizes, files_path, total_size, file_count)

if len(sys.argv) != 3:
    print('incorrect arguments')
    exit(1)
root_dir = get_files_size_dir(sys.argv[1])
backup_dir = get_files_size_dir(sys.argv[2])

all_files = set(root_dir.files) | set(backup_dir.files)

missing_files = []
size_diff_files = []

for f in all_files:
    if not f in backup_dir.files and f in root_dir.files:
        missing_files.append(root_dir.files_path[f])
    elif f in backup_dir.files and f in root_dir.files and root_dir.files_sizes[f] != backup_dir.files_sizes[f]:
        size_diff_files.append(root_dir.files_path[f])

print('= SUMMARY =')
print(' total size:              ', root_dir.total_size)
print(' total size backup:       ', backup_dir.total_size)
print(' total nr of files:       ', root_dir.file_count)
print(' total nr of files backup:', backup_dir.file_count)
print('===================')
print('== MISSING FILES ==')
for f in missing_files:
    print(f)
print('== SIZE DIFF FILES ==')
for f in size_diff_files:
    print(f)
