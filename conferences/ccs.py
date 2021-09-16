from .common import Conference
class CCS(Conference):
    def print_accepted_paper(self):
        return super().print_accepted_paper()
    def update_url(self):
        self.url = "https://www.sigsac.org/ccs/CCS"+str(self.year)+"/accepted-papers.html"
