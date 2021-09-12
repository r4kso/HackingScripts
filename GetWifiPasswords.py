###########################################
# Made by R4kso                           #
# https://github.com/r4kso                #
# https://www.instagram.com/notaboutfran/ #
###########################################

import subprocess
import re

output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
names = (re.findall("All User Profile     : (.*)\r", output))

list = []

if len(names) != 0:
    for name in names:
        wifi_profile = {}
        pinfo = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", pinfo):
            continue
        else:
            wifi_profile["ssid"] = name
            pinfo_pswd = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            pswd = re.search("Key Content            : (.*)\r", pinfo_pswd)
            if pswd == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = pswd[1]
            list.append(wifi_profile)

for x in range(len(list)):
    print(list[x])