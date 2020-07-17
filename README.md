# Easy Actions

**pre-pre-pre-pre alpha, there's almost nothing here**

## Wish list

The code below should:

1. Emit a landing page
2. With login buttons using google, github and basic auth
3. When the user is logged in, there's a button for the `open_xpto` action
4. When that button is clicked, `__call__` is invoked

``` python
from easy_actions import App
from easy_actions.authenticators import BasicAuth, GithubAuth, GoogleAuth
from easy_actions.actuators import AWSActions

basic_auth = BasicAuth(username="admin", password="this should not be used in prod")
sesame = App('open-sesame', authenticators=[basic_auth])

github_auth = GithubAuth(params="All the cool parameters github needs")
sesame.register_auth(github_auth)

@sesame.authenticator
class CustomGoogleAuth(GoogleAuth):

    def __init__(self):
        super.etc

    def auth(self, lots, of, params, probably):
        return user.email in list_of_authorized_users

class OpenSGPort(AWSActions):
    def __init__(self, params):
        self.title = "Allow connection from your IP to the XPTO security group"
        super.etc

    def __call__(self):
        boto3.etc.etc.add_ip_to_sg_allow_all_ports

open_xpto = OpenSGPort(probably="auth params", to_boto="go here!")

sesame.register_action(open_xpto)

if __name__ == "__main__":
    sesame.run(debug=True)
```
