from .common import Conference
from bs4 import BeautifulSoup

class CCS(Conference):
    def parsing_paper(self, text):
        parser = BeautifulSoup(text, "html.parser")
        paper_list = parser.findAll("div", attrs={'class':"papers-item"})
        for paper in paper_list:
            self.papers.append(paper.b.text)
    def print_accepted_paper(self):
        print(self.papers)
        return super().print_accepted_paper()
    def update_url(self):
        self.url = "https://www.sigsac.org/ccs/CCS"+str(self.year)+"/accepted-papers.html"
