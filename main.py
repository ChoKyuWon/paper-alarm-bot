from abc import abstractmethod
from time import sleep
import requests

class Conference:
    def __init__(self, _year):
        self.year = _year
        self.update_url()

    def check_update(self):
        print("access on "+ self.url)
        self.ret = requests.get(self.url, allow_redirects=False)
        if self.ret.status_code == 200:
            self.year += 1
            self.update_url()
            self.print_accepted_paper()
            return True
        else:
            return False
    @abstractmethod
    def update_url():
        pass
    def print_accepted_paper(self):
        print(self.url)

class CCS(Conference):
    def print_accepted_paper(self):
        return super().print_accepted_paper()
    def update_url(self):
        self.url = "https://www.sigsac.org/ccs/CCS"+str(self.year)+"/accepted-papers.html"

class NDSS(Conference):
    def update_url(self):
        self.url = "https://www.ndss-symposium.org/ndss"+str(self.year)+"/accepted-papers/"

    def print_accepted_paper(self):
        return super().print_accepted_paper()

class SnP(Conference):
    def update_url(self):
        self.url = "https://www.ieee-security.org/TC/SP"+str(self.year)+"/program-papers.html"

    def print_accepted_paper(self):
        return super().print_accepted_paper()

class USENIX(Conference):
    def print_accepted_paper(self):
        return super().print_accepted_paper()

class USENIX_SUMMER(USENIX):
    def update_url(self):
        self.url = "https://www.usenix.org/conference/usenixsecurity"+str(self.year)[2:4]+"/summer-accepted-papers"


class USENIX_FALL(USENIX):
    def update_url(self):
        self.url = "https://www.usenix.org/conference/usenixsecurity"+str(self.year)[2:4]+"/fall-accepted-papers"


def print_accepted_paper(url, text):
    print(url)

def url_update(url):
    return url

def check_update(conferences):
    while True:
        flag = True
        for conference in conferences:
            if conference.check_update() == False:
                print(conference.url + "is False!")
                flag = False
        if flag == False:
            sleep(10000)
        


def main():
    init_year = 2022
    conferences = []
    conferences.append(CCS(init_year))
    conferences.append(NDSS(init_year))
    conferences.append(SnP(init_year))
    conferences.append(USENIX_SUMMER(init_year))
    conferences.append(USENIX_FALL(init_year))
    check_update(conferences)

if __name__ == '__main__':
    main()
