class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # setup part of context manager
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file # will be returing the object that we are working with within our context manager

    # teardown part of context manager. gets run when we exit the context manager. Need to make sure that the file gets closed at this point
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()


with Open_File('cm_samplefile.txt', 'w') as wf:
    wf.write('testing cm')

print(wf.closed)