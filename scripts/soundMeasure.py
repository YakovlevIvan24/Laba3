import requests

ip = '' # Usually 192.168.212.X. Find X in oscilloscope settings

if (ip == ''):
    print('Setup ip-address of Tekronix oscilloscope')
    quit()

url = 'http://' + ip + '/Image.png'
r = requests.get(url, allow_redirects=True)

open('tektronix.png', 'wb').write(r.content)