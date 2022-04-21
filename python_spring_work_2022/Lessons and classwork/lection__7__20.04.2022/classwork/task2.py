# todo: задан словарь
"""
{ "sdtv_mode":2, "hdmi_drive":2, "hdmi_group":2, "hdmi_mode":16, "overscan_left":20, "overscan_right":12, "overscan_top":10 }

# Нужно создать  файл config.txt с содержимым вида:
sdtv_mode=2
hdmi_drive=2
hdmi_group=2
hdmi_mode=16
overscan_left=20
overscan_right=12
overscan_top=10"""

my_dict = {"sdtv_mode": 2, "hdmi_drive": 2, "hdmi_group": 2, "hdmi_mode": 16, "overscan_left": 20,
           "overscan_right": 12, "overscan_top": 10}


def create_file(name, dict):
    f = open(name, "w+t")
    for item in dict:
        f.write(item + "=" + str(dict[item]) + "\n")
    f.close()


file = "config.txt"
create_file(file, my_dict)
