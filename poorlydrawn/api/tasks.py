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
from . import models


@shared_task()
def fetch_and_insert_in_db(x):
    soup = BeautifulSoup(x.text, "html.parser")

    title = soup.select_one('head > title').text.replace("Poorly Drawn Lines – ", "")
    image = soup.select_one('.post > p > img').attrs['src']
    description = soup.select_one('.post > p > img').attrs['alt']

    if not models.Comic.objects.filter(title=title).exists():
        comic = models.Comic()
        comic.description = description
        comic.title = title
        comic.image = image
        comic.link = x.url
        comic.save()

        return comic
    else:
        models.Comic.objects.filter(title=title).first()


@periodic_task(run_every=datetime.timedelta(hours=5))
def fetch_comics():
    print("fething ...............")
    response = requests.get(settings.ARCHIVE_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    all_comics = soup.select('.content > ul > li > a')

    to_fetch = grequests.map((grequests.get(x.attrs['href']) for x in all_comics[:5]))
    print("fetched now saving....")

    for x in to_fetch:
        try:
            fetch_and_insert_in_db.delay(x)

        except Exception as e:  # TODO: Catch actual exception
            print(e)
