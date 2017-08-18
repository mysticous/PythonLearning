import requests
url = 'http://10.0.0.55:801/srun_portal_pc.php'
s = requests.session()
username = ''
password = ''
response = s.post(
    url,
    data={
        'action': 'logout',
        'username': username,
        'password': password,
        'ajax': 1
    })

print(response.content.decode())