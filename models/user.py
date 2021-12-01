from datetime import datetime


class User:

    def __init__(self, name, email, hashed_password):
        self.name = name
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = None
        self.profile_image_url = ""
        self.last_login: datetime = None

