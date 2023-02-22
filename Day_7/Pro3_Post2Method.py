# import requests
# payload={'username':'shubhangi','password':'shubhz@06'}
# r=requests.post('https://httpbin.org/post',data=payload)
# r_dict=r.json()
#
# print(r_dict['form'])



import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

print(x.text)