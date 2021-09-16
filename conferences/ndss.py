from .common import Conference

class NDSS(Conference):
    def update_url(self):
        self.url = "https://www.ndss-symposium.org/ndss"+str(self.year)+"/accepted-papers/"

    def print_accepted_paper(self):
        return super().print_accepted_paper()