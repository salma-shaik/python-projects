with open('flower.JPG','rb') as rf:
    with open('flower_copy.JPG', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
        chunk_size = 4096
        rf_chunk_size = rf.read(chunk_size)
        while len(rf_chunk_size) > 0:
            wf.write(rf_chunk_size)
            rf_chunk_size = rf.read(chunk_size)

