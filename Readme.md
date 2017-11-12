# Poorly Drawn API

# Installing
```sh
$ git clone git@github.com:othreecodes/Poorly-Drawn-API.git
$ cd Poorly-Drawn-API
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ gunicorn poorlydrawn.config.wsgi:application # run with gunicorn

```

# Usage
API is hosted at https://poorlydrawnlines.herokuapp.com/api/v1/comics/


GET - https://poorlydrawnlines.herokuapp.com/api/v1/comics/?limit=5&offset=200
```javascript

{
    "count": 918,
    "next": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/?limit=5&offset=205",
    "previous": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/?limit=5&offset=195",
    "results": [
        {
            "id": 200,
            "url": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/200/",
            "created": "2017-11-12T22:25:16.919387+01:00",
            "title": "The Shop",
            "link": "http://www.poorlydrawnlines.com/comic/the-shop/",
            "description": "the-shop",
            "image": "https://www.poorlydrawnlines.com/wp-content/uploads/2016/07/the-shop.png",
            "slug": "the-shop"
        },
        {
            "id": 201,
            "url": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/201/",
            "created": "2017-11-12T22:25:18.448551+01:00",
            "title": "Turn to History",
            "link": "http://www.poorlydrawnlines.com/comic/turn-to-history/",
            "description": "turn-to-history",
            "image": "https://www.poorlydrawnlines.com/wp-content/uploads/2016/07/turn-to-history.png",
            "slug": "turn-to-history"
        },
        {
            "id": 202,
            "url": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/202/",
            "created": "2017-11-12T22:25:19.754206+01:00",
            "title": "Have it All",
            "link": "http://www.poorlydrawnlines.com/comic/have-it-all/",
            "description": "have-it-all",
            "image": "https://www.poorlydrawnlines.com/wp-content/uploads/2016/07/have-it-all.png",
            "slug": "have-it-all"
        },
        {
            "id": 203,
            "url": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/203/",
            "created": "2017-11-12T22:25:21.019026+01:00",
            "title": "Bird Shopping",
            "link": "http://www.poorlydrawnlines.com/comic/bird-shopping/",
            "description": "bird-shopping",
            "image": "https://www.poorlydrawnlines.com/wp-content/uploads/2016/07/bird-shopping.png",
            "slug": "bird-shopping"
        },
        {
            "id": 204,
            "url": "https://poorlydrawnlines.herokuapp.com/api/v1/comics/204/",
            "created": "2017-11-12T22:25:22.099542+01:00",
            "title": "Not Much",
            "link": "http://www.poorlydrawnlines.com/comic/not-much/",
            "description": "not-much",
            "image": "https://www.poorlydrawnlines.com/wp-content/uploads/2016/06/not-much.png",
            "slug": "not-much"
        }
    ]
}
```