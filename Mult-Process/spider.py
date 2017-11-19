import sys
import requests
import json
# input from|batchsize|No
startFrom = int(sys.argv[1])
batchSize = int(sys.argv[2])
s = requests.session()
response1 = s.post(
    "https://pente.org/gameServer/index.jsp",
    data={
        'name2': 'PsychoLsc',
        'password2': '362546643Lsc',
    })
with open('result' + sys.argv[3] + '.txt', 'a') as f:
    # Read
    d = {}
    for numbercount in range(startFrom, startFrom - batchSize, -1):
        string = str(numbercount)
        while len(string) < 6:
            string = '0' + string
        url = 'https://pente.org/gameServer/pgn.jsp?g=50000000' + string
        response = s.get(url, data={'g': '50000000' + string})
        result = response.content.decode()
        # process
        if 'Connect6' not in result:
            print('Useless No.{}'.format(string))
            pass
        else:
            print('Useful No.{}'.format(string))
            result = result.split('\r\n')[17:-1]
            res = ''
            for j in result:
                res += j
            res = res[0:-3]
            steps = res.count('.')
            output = res.split(str(steps) + '.')[1].strip()
            res = res.split(str(steps) + '.')[0]
            for i in range(steps, 0, -1):
                res = res.replace(str(i) + '.', '')
            input_ = res.replace(' ', '')
            print(input_, output, sep='\n')
            d['No'] = string
            d['Input'] = input_
            d['Output'] = output
            f.write(json.dumps(d))
            f.write('\n')

# print(sys.argv[3])
