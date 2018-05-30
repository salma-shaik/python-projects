import os
os.chdir('C:/Users/arvind1613/Desktop/Salma/Python/python-projects/yt_pb71_cs/planets')
# print("Current dir: ", os.getcwd())

for item in os.listdir():
    # print(item)
    # print(os.path.splitext(item))
    f_name, f_ext = os.path.splitext(item)
    # print(filename)

    # print(filename.split('-'))
    f_title, f_module, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_module = f_module.strip()
    f_num = f_num.strip()[1:].zfill(2) #to pad the nummbers
    # print(f_name)
    # print(f_module)
    # print(f_num)

    newname = '{}-{}{}'.format(f_num,f_title,f_ext)
    # print(newname)
    os.rename(item, newname)
    