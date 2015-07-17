import json
import requests
import xmltodict

def github_getuser(username):
    response = requests.get('https://api.github.com/users/%s' % username)
    decoded_json = response.content.decode('utf8')
    js=json.loads(decoded_json)
    return js

def github_user_xml(username):
    userdict = {"GITHUB_USER":github_getuser(username)}
    xml = xmltodict.unparse(userdict)
    return xml

if __name__=='__main__':
    USER = "leandrolsilva"
    print(github_user_xml(USER))
