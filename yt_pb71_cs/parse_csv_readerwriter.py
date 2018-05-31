import csv

with open('persons_info.csv', 'r') as pf:
    pf_reader = csv.reader(pf)
    # print(pf_reader)

    with open('persons_info_copy.csv', 'w') as pw:
        pw_writer = csv.writer(pw)

        for line in pf_reader:
            pw_writer.writerow(line)

with open('persons_info_copy.csv', 'r') as cs_file:
    csf_reader = csv.reader(cs_file, delimiter='\t')

    for line in csf_reader:
        print(line)
