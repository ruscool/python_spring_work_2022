# переделка


def add_com():
    f = open('mac.md', 'r+')
    for i in f:
        line = f.readline()
        line = '#### ' + line
        # print(line)
        save_f = open('../md_Files/tabs_mac.md', 'a+')
        save_f.write(line)
    save_f.close()
    f.close()


add_com()
