from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)    # equivalent to init in cm cls - setup
        yield f                 # equivalent to enter in cm cls - main business execution
    finally:
        f.close()               # equiv to exit in cm cls - teardown


with open_file('cm_func_samplefile.txt', 'w') as wf:
    wf.write('testing from cm func')

print(wf.closed)

