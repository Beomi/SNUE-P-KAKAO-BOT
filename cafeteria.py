import requests
from bs4 import BeautifulSoup as bs
import re
from datetime import datetime
import textwrap


def get_menus():
    html = requests.get('http://portal.snue.ac.kr/enview/2015/food.jsp').text
    soup = bs(html, 'html.parser')
    daily = soup.select('tr')

    re_date = re.compile('(\d{2}[/]\d{2})')

    for i in daily:
        try:
            info = i.text.split('\n')
            date = re.search(re_date, info[1]).group()

            py_date = datetime.strptime(date, '%m/%d').replace(year=datetime.today().year).date()
            if (py_date == datetime.now().date()):
                lunch_meal = info[3].replace(' ', '\n')
                dinner_meal = info[4].replace(' ', '\n')
                menus = f"""\
** 오늘의 학식 **
--- 점심 ---
{lunch_meal}
--- 저녁 ---
{dinner_meal}\
                """
                return menus
        except AttributeError:
            pass  # to ignore first tr


if __name__ == '__main__':
    print(get_menus())
