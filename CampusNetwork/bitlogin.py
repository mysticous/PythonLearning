import requests
url = 'http://10.0.0.55:801/srun_portal_pc.php'
s = requests.session()
username = ''
password = ''
response = s.post(
    url,
    data={
        'action': 'login',
        'username': username,
        'password': password,
        'ac_id': 8,
        'save_me': 0,
        'ajax': 1
    })

print(response.content.decode())
