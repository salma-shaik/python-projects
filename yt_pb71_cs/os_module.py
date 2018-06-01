import os
from datetime import datetime

# print(dir(os))


# print(os.getcwd())
# os.chdir('/Users/salma/Studies/Python/python-projects')
# print(os.getcwd())
# print(os.listdir())


# os.mkdir('test-dir/sub-dir1')
# os.makedirs('test-dir1/sub-dir1')
# print(os.listdir())


# os.rmdir('test-dir/sub-dir1')
# os.removedirs('test-dir1/sub-dir1')
# os.removedirs('test-dir/sub-dir1')
# print(os.listdir())


# os.mkdir('test-dir')
# os.rename('test-dir', 'demo-dir')
# print(os.listdir())


# print(os.stat('demo-dir').st_size)
# mod_time = os.stat('demo-dir').st_mtime
# print(datetime.fromtimestamp(mod_time))


# for dir_path, dir_names, file_names in os.walk('/Users/salma/Studies/Python/python-projects'):
#     print('Current Path: ', dir_path)
#     print('Directories: ', dir_names)
#     print('Files: ', file_names)
#     print()


print(os.environ.get('HOME'))
# file_path = os.environ.get('HOME') + 'test.txt'
# print(file_path)
# file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
# print(file_path)


# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))
# print(os.path.isdir('/tmp/test.txt'))
# print(os.path.isfile('/tmp/test.txt'))
# print(os.path.splitext('/tmp/test.txt'))
# print(dir(os.path))
