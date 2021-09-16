from time import sleep
from conferences.ccs import CCS
from conferences.ndss import NDSS
from conferences.sec import SEC_FALL, SEC_SUMMER
from conferences.snp import SnP

from alarm_bot import alarm

def check_update(conferences_list):
    while True:
        flag = False
        for conference in conferences_list:
            if conference.check_update() == True:
                flag = True
                alarm(conference)
        if flag == False:
            sleep(86400) # Every conference is up-to-data, sleep 1 day
        


def main():
    init_year = 2022
    conferences_list = []
    conferences_list.append(CCS(init_year))
    conferences_list.append(NDSS(init_year))
    conferences_list.append(SEC_SUMMER(init_year))
    conferences_list.append(SEC_FALL(init_year))
    conferences_list.append(SnP(init_year))
    check_update(conferences_list)

if __name__ == '__main__':
    main()
