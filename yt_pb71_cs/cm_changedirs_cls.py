import os


class ChangeDirs:
    cwd = os.getcwd()

    def __init__(self, destination):
        self.destination = destination

    def __enter__(self):
        os.chdir(self.destination)

    def __exit__(self, exc_type, exc_val, traceback):
        os.chdir(self.cwd)


with ChangeDirs('Sample-Dir-One'):
    print(os.listdir())

with ChangeDirs('Sample-Dir-Two'):
    print(os.listdir())

