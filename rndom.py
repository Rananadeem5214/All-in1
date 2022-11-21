import os, platform

try:

    import requests

except:

    os.system('pip install requests')
    os.system('xdg-open https://www.facebook.com/ITXRANA.5214')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import rana_menu
    rana_menu()
    #kr()

elif bit == '32bit':

    from rana1 import rana_menu

    rana_menu()

else:

    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')

    os.system('exit')
    
