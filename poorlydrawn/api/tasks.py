# from celery.decorators import task
from celery import shared_task
from django.conf import settings
import requests
import  grequests


from bs4 import BeautifulSoup

@shared_task(name="fetch_comics")
def fetch_comics(x):
    response = requests.get(settings.ARCHIVE_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    all_comics = soup.select('.content > ul > li > a')

    to_fetch = (grequests.get(x.attrs['href']) for x in all_comics)

    def insert(x):
        soup = BeautifulSoup(requests.get(x))


    h = [insert(x) for x in to_fetch]





