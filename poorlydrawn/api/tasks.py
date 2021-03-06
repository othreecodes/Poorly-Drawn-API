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
    if x is None:
        return None
    soup = BeautifulSoup(x.text, "html.parser")
    try:
        title = soup.select_one('head > title').text.replace("Poorly Drawn Lines – ", "")
        image = soup.select_one('.post > p > img').attrs['src']
        description = soup.select_one('.post > p > img').attrs['alt']
    except AttributeError as e:
        print(x)

        return None

    if not models.Comic.objects.filter(title=title).exists():
        comic = models.Comic()
        comic.description = description
        comic.title = title
        comic.image = image
        comic.link = x.url

        return comic
    else:

        return None


@periodic_task(run_every=datetime.timedelta(hours=5))
def fetch_comics():
    print("fething ...............")
    response = requests.get(settings.ARCHIVE_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    all_comics = soup.select('.content > ul > li > a')

    # to_fetch = grequests.map((grequests.get(x.attrs['href']) for x in all_comics))
    # TODO: 502/503 while running asyncronoously use syncronous requets?

    print("fetched now saving....")

    for index, x in enumerate(all_comics):
        res = requests.get(x.attrs['href'])
        comic = fetch_and_insert_in_db(res)

        if comic:
            comic.save()

        print(index)


# @periodic_task(run_every=datetime.timedelta(hours=5))
# def fetch_comics():
#     print("fething ...............")
#     response = requests.get(settings.ARCHIVE_URL)
#
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     all_comics = soup.select('.content > ul > li > a')
#
#     # to_fetch = grequests.map((grequests.get(x.attrs['href']) for x in all_comics))
#     # TODO: 502/503 while running asyncronoously use syncronous requets?
#     to_fetch = [requests.get(x.attrs['href']) for x in all_comics]
#     print("fetched now saving....")
#
#     comiccs = [fetch_and_insert_in_db(x) for x in to_fetch]
#     comicsave = [x for x in comiccs if x is not None]
#     print(len(comicsave))
#
#     models.Comic.objects.bulk_create(comicsave)


def f():
    print("fething ...............")
    response = requests.get(settings.ARCHIVE_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    all_comics = soup.select('.content > ul > li > a')

    # to_fetch = grequests.map((grequests.get(x.attrs['href']) for x in all_comics))
    # TODO: 502/503 while running asyncronoously use syncronous requets?

    print("fetched now saving....")

    for index, x in enumerate(all_comics):
        res = requests.get(x.attrs['href'])
        comic = fetch_and_insert_in_db(res)

        if comic:
            comic.save()

        print(index)
