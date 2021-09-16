from abc import abstractmethod
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