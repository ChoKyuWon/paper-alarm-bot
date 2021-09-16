from time import sleep
# from conferences.common import *
from conferences.ccs import CCS
from conferences.ndss import NDSS
from conferences.sec import SEC_FALL, SEC_SUMMER
from conferences.snp import SnP


def check_update(conferences_list):
    while True:
        flag = True
        for conference in conferences_list:
            if conference.check_update() == False:
                flag = False
        if flag == False:
            sleep(86400) # 1 day
        


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
