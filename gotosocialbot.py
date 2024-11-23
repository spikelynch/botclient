import requests
import json

"""
gotosocialbot 
"""

DEFAULT_OPTIONS = {
    'visibility': 'unlisted'
}


class GoToSocialBot():
    def __init__(self):
        self.char_limit = 5000
        self.char_limit_img = 5000
        self.auth_cf_fields = [ 'access_token', 'base_url' ]

    def auth(self, cf):
        """GoToSocial doesn't need a pre-auth so just build headers"""
        self.base_url = cf['base_url']
        self.access_token = cf['access_token']
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.access_token}"
        }
        return True
    
    def post(self, status, options=None):
        """Post a string as a new status."""
        if len(status) > self.char_limit:
            print("Status text is over %d chars" % self.char_limit)
            return False
        e_options = DEFAULT_OPTIONS.copy()
        if options:
            for o, v in options.items():
                e_options[o] = v
        e_options['status'] = status
        json_d = json.dumps(e_options)
        print(json_d)
        print(self.headers)
        r = requests.post(
            f"{self.base_url}/api/v1/statuses",
            data=json_d,
            headers=self.headers,
        )
        r.raise_for_status()
        return True
    
#     def post_image(self, imgfile, text, options=None):
#         """Post a toot with one attached image

# Args:
#     img (str): image file
#     text (str): text part of toot
#     options (dict): options

# Returns:
#     status (bool): True if the post was successful
#        """
#         pass


if __name__ == "__main__":
    r = requests.post("Testing again");
    print(r.text)
