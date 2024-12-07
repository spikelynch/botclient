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
        r = requests.post(
            f"{self.base_url}/api/v1/statuses",
            data=json_d,
            headers=self.headers,
        )
        r.raise_for_status()
        return True
    
    def post_image(self, status, imgfile, alt_text, mime_type, options=None):
        """Post with one attached image

Args:
    img (str): image file
    text (str): text part of toot
    options (dict): options

Returns:
    status (bool): True if the post was successful
        """
        with open(imgfile, "rb") as ifh:
            files = { 'file': (imgfile, ifh, mime_type)}
            r = requests.post(
                f"{self.base_url}/api/v1/media",
                files=files,
                data={"description": alt_text},
                headers={"Authorization": f"Bearer {self.access_token}"}
            ) 
            r.raise_for_status()
            rjson = r.json()
            options["media_ids"] = [ rjson["id"] ]
            return self.post(status, options)
        

if __name__ == "__main__":
    r = requests.post("Testing again");
    print(r.text)
