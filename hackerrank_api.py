import requests

run_url = ''
key = ''

post_data = {
    'source':'print 1',
    'lang':5,
    'testcases':'["1","2"]',
    'api_key':key,
    'wait':True,
    'format':'xml'
}

r = requests.post(run_url , data = post_data)
r =  r.json()

print r
