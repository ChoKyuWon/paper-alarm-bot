from .common import Conference

class SEC(Conference):
    def print_accepted_paper(self):
        return super().print_accepted_paper()

class SEC_SUMMER(SEC):
    def update_url(self):
        self.url = "https://www.usenix.org/conference/usenixsecurity"+str(self.year)[2:4]+"/summer-accepted-papers"


class SEC_FALL(SEC):
    def update_url(self):
        self.url = "https://www.usenix.org/conference/usenixsecurity"+str(self.year)[2:4]+"/fall-accepted-papers"
