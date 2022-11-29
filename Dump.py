import os, platform

try:

    import requests

except:

    os.system('pip install requests')
    os.system('xdg-open https://www.facebook.com/ITXRANA.5214')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    import p_dump
    p_dump()
    #kr()

elif bit == '32bit':

    from dump import p_dump

    p_dump()

else:

    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')

    os.system('exit')
    
