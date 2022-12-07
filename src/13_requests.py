import requests

# url = 'http://xlrelease.domain.com'

# #use the 'auth' parameter to send requests with HTTP Basic Auth:
# x = requests.get(url, auth = ('admin', 'papagaio'))

# print(x.status_code)


urlcreate = 'http://xlrelease.domain.com/api/v1/templates/Applications/Folderd9bf3cfea0294b75afce9411d3d701c6/Release31fd08e8dabb47e4805ffb094d27689e/create'

callrelease = {
  'releaseTitle': 'test',
  'scheduledStartDate': 'null',
  'autoStart': 'true' 
  }
headers = {
  'Accept': 'application/json'
  }


xrelease = requests.post(urlcreate, json = callrelease,  headers = headers, auth = ('admin', 'papagaio'))

print(xrelease.text)



