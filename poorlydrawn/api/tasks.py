# from celery.decorators import task
from celery import shared_task
from django.conf import settings
import requests
import grequests
import celery
import datetime
from celery.task.base import periodic_task
import datetime
from bs4 import BeautifulSoup

# @periodic_task(run_every=datetime.timedelta(seconds=30))
# def myfunc():
#     print('periodic_task')
#     return True


@periodic_task(run_every=datetime.timedelta(hours=5))
def fetch_comics():
    print("fething ...............")
    response = requests.get(settings.ARCHIVE_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    all_comics = soup.select('.content > ul > li > a')

    to_fetch = (grequests.get(x.attrs['href']) for x in all_comics)

    def insert(x):
        soup = BeautifulSoup(requests.get(x))

    h = [insert(x) for x in to_fetch]
