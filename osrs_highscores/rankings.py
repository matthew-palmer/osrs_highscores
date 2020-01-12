from bs4 import BeautifulSoup
import requests
from .categories import OSRSInfo, OSRSRank
from .base import OSRSBase


class Rankings(OSRSBase):
    def __init__(self, target="default"):
        super(Rankings, self).__init__(target)
        self.index = "overall.ws"

    def get_rank_in_skill(self, skill, rank):
        table = OSRSInfo().index_inverse[skill]
        rank_page = int(float(rank/25))
        table_string = "{}&page={}".format(table, rank_page)
        target_url = self._request_build(table=table_string)
        response = requests.get(target_url).content
        bs = BeautifulSoup(response, features="lxml")
        rows = bs.find("table").find("tbody").findAll("tr")
        for row in rows:
            cells = row.findAll("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    level = cells[2].getText().replace('\n', '')
                    xp = cells[3].getText().replace('\n', '')
                    return OSRSRank(user, level, xp, skill)
            except TypeError:
                pass

    def get_rank_in_skill(self, skill, rank):
        table = OSRSInfo().index_inverse[skill]
        rank_page = int(float(rank/25))
        table_string = "{}&page={}".format(table, rank_page)
        target_url = self._request_build(table=table_string)
        response = requests.get(target_url).content
        bs = BeautifulSoup(response, features="lxml")
        rows = bs.find("table").find("tbody").findAll("tr")
        for row in rows:
            cells = row.findAll("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    level = cells[2].getText().replace('\n', '')
                    xp = cells[3].getText().replace('\n', '')
                    return OSRSRank(user, 'skill', rank=rank, level=level, xp=xp, skill=skill)
            except TypeError:
                pass

    def get_rank_in_target(self, target, rank):
        table = OSRSInfo().alt_index_inverse[target]
        rank_page = int(float(rank / 25))
        category_string = "1&table={}&page={}".format(table, rank_page)
        target_url = self._request_build(category_type=category_string)
        response = requests.get(target_url).content
        bs = BeautifulSoup(response, features="lxml")
        rows = bs.find("table").find("tbody").findAll("tr")
        for row in rows:
            cells = row.findAll("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    score = cells[2].getText().replace('\n', '')
                    return OSRSRank(user, 'nonskill', rank=rank, score=score)
            except TypeError:
                pass
