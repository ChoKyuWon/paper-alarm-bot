from .common import Conference
class SnP(Conference):
    def update_url(self):
        self.url = "https://www.ieee-security.org/TC/SP"+str(self.year)+"/program-papers.html"

    def print_accepted_paper(self):
        return super().print_accepted_paper()