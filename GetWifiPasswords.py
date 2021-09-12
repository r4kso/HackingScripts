# Import subprocess so we can use system commands
import subprocess
# Import re so we can use regular expressions
import re

output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
names = (re.findall("All User Profile     : (.*)\r", output))

list = []

if len(names) != 0:
    for name in names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pswd = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            pswd = re.search("Key Content            : (.*)\r", profile_info_pswd)
            if pswd == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = pswd[1]
            list.append(wifi_profile)

for x in range(len(list)):
    print(list[x])