import codecs
import glob
import bs4 as bs
from contextlib import contextmanager

import psycopg2


@contextmanager
def dbcontext(connection):
    cur = connection.cursor()
    try:
        yield cur
        connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()

connection = psycopg2.connect("dbname=sia user=postgres password=1234")

for htmlFile in glob.glob("./data/*.html"):
    with codecs.open(htmlFile, encoding="utf8") as fp:
        toParse = fp.read()

    soup_html = bs.BeautifulSoup(toParse,"htmlFile.parser")

    print soup_html
