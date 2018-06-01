import csv

names = []
with open('persons_info_forhtml.csv', 'r') as fr:
    # fr_reader = csv.reader(fr)
    fr_reader = csv.DictReader(fr)

    # Skipping the header and rewards description sentences
    # with dict reader, we need the header row, so skipping the 2nd No Rewards Description sentence
    next(fr_reader)
    # next(fr_reader)

    for line in fr_reader:
        # if line[0] == 'No Reward':
        if line['first_name'] == 'No Reward':
            break
        name = f"{line['first_name']} {line['last_name']}"
        names.append(name)

    print(f'<p>There are {len(names)} contributors. Thank you!</p>')
    # print(names)
    print('<ul>')
    for name in names:
        print(f'\t<li>{name}</li>')
    print('</ul>')
    # with open('persons_mnames_html', 'w') as fw:
    #     fw_writer = csv.writer(fw)
    #
    #         fw_writer.write(line)
    #         print(line)
