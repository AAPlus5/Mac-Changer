from generate_mac import generate_mac
import subprocess
import argparse
import re
import time

def user_input():
    parse_object = argparse.ArgumentParser()
    parse_object.add_argument("-i","--interface",dest="interface",help="Enter a interface")
    parse_object.add_argument("-m","--mac_address",dest="mac_address",help="Enter a mac address",nargs="?")
    parse_object.add_argument("-rm","--random_mac_address",dest="random_mac",help="For a random mac address",nargs="?",default=1)
    return parse_object.parse_args()


def change_mac(interface,mac_address):
    subprocess.call(["ifconfig",args.interface,"down"])
    subprocess.call(["ifconfig",args.interface,"hw","ether",args.mac_address])
    subprocess.call(["ifconfig",args.interface,"up"])

def control_mac_address(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig.decode("utf-8"))
    ifconfig.decode("utf-8")
    return mac

args = user_input()

print("""

  __  __                    _____ _                                  __      ____ 
 |  \/  |                  / ____| |                                 \ \    / /_ |
 | \  / | __ _  ___ ______| |    | |__   __ _ _ __   __ _  ___ _ __   \ \  / / | |
 | |\/| |/ _` |/ __|______| |    | '_ \ / _` | '_ \ / _` |/ _ | '__|   \ \/ /  | |
 | |  | | (_| | (__       | |____| | | | (_| | | | | (_| |  __| |       \  _   | |
 |_|  |_|\__,_|\___|       \_____|_| |_|\__,_|_| |_|\__, |\___|_|        \(_)  |_|
                                                     __/ |                        
                                                    |___/                         

""")

if args.random_mac == None:
    args.mac_address = generate_mac.total_random()
else:
    pass

old_mac = control_mac_address(args.interface)
change_mac(args.interface,args.mac_address)
new_mac = control_mac_address(args.interface)

if old_mac != new_mac:
    for i in range(1,4):
        for j in range(1, i + 1):
            print("* ", end="")
            time.sleep(0.50)
        print()
    time.sleep(0.3)
    print("\nSuccess !","\nYour New Mac:",str(new_mac)[42:59],"\nYour Old Mac",str(old_mac)[42:59])
else:
    for i in range(1, 4):
        for j in range(1, i + 1):
            print("* ", end="")
            time.sleep(0.50)
        print()
    time.sleep(0.3)
    print("Error !")




