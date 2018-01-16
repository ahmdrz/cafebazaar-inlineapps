import bs4
import re
import cafebazaar
import operator
import argparse


def calculate_total_rate(d):
    s = 0
    for key, value in d.items():
        s += key * value
    return s


def trim_space(text):
    return re.sub('^\s+|\s+$', '', text)


def fix_number(n):
    n = n.replace(u'\u066b', '.')
    return n.translate(
        {1776: 48, 1777: 49, 1778: 50, 1779: 51, 1780: 52, 1781: 53, 1782: 54, 1783: 55, 1784: 56, 1785: 57})


def main(args):
    apps = list()
    p = 0

    while True:
        page = cafebazaar.get_page(p)
        soup = bs4.BeautifulSoup(page, 'html.parser')
        app_cards = soup.select('.msht-app')
        if not app_cards:
            break

        p += len(app_cards)

        for item in app_cards:
            link = item.find('a').get('href')
            html = cafebazaar.get_app(trim_space(link))
            app_soap = bs4.BeautifulSoup(html, 'html.parser')
            modal = app_soap.select_one('#dlAppRatingModal')
            total_rate = trim_space(modal.find('h2', {'class': 'rating-total'}).text)

            rates = dict()
            for i, rate_detail in enumerate(modal.select('.rating-details .pull-right')):
                rates[5 - i] = int(fix_number(trim_space(rate_detail.text)))

            name = trim_space(app_soap.select_one('.app-name').find('h1').text)
            apps.append([name, float(fix_number(total_rate)), rates])

    if not args["sort"]:
        apps.sort(key=operator.itemgetter(1), reverse=True)
    else:
        def compare(x, y):
            return calculate_total_rate(x[2]) - calculate_total_rate(y[2])

        apps.sort(cmp=compare, reverse=True)

    count = args["count"]
    if count != -1:
        apps = apps[:count]

    for i, app in enumerate(apps):
        print "number : {}".format(i)
        print u"name : {}".format(app[0])
        print "users : {}".format(sum(app[2].values()))
        print "rate : {} ({}/{})".format(app[2], app[1], calculate_total_rate(app[2]))
        print "-----------------"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--sort", default=False, type=bool,
                    help="sort only with rates, default is count*rate")
    ap.add_argument("-c", "--count", default=-1, type=int,
                    help="count of inline-apps")
    main(vars(ap.parse_args()))
