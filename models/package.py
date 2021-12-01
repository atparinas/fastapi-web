from typing import List


class Package:

    def __init__(self, package_name: str,
                 summary: str,
                 description: str,
                 home_page: str,
                 package_license: str,
                 author_name: str,
                 maintainers: List
                 ):
        self.package_name = package_name
        self.id = package_name
        self.summary = None
        self.description = None
        self.home_page = None
        self.package_license = None
        self.author_name = None
        self.maintainers = []
