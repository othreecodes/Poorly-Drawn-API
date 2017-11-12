from celery.decorators import task



@task(name="fetch_comics")
def fetch_comics(x):
    
    return x