django-simplesearch
============

A reusable [Django](http://www.djangoproject.com/) application for simple searching, based on [Julien Phalip's original code](http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap>).


How it Works
------------

A string of search terms are passed to the `get_query` function, along with a list of the model fields to search. These terms are normalized by `normalize_query`, which splits the query string into individual keyword, keeping quoted words together and removing [stop words](https://en.wikipedia.org/wiki/Stop_words). The `get_query` function then returns a [Q object](https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects) which may be used to search the given fields for the given term.


Installation
------------

django-simplesearch is available on PyPI and can be installed with PIP.

    pip install django-simplesearch

Alternatively, you may download the source and install it.

    python setup.py install


Setup
-----

Add `simplesearch` to your `settings.INSTALLED_APPS`.


Usage
-----

django-simplesearch was created to search blog posts. To search a model `Post` in the fields `title` and `body` based on a search query submitted by a form to HTTP GET, you might do something like this:

    if 'q' in request.GET:
        query_string = request.GET['q']
        entry_query = get_query(query_string, ['title', 'body'])
        results = Post.objects.published().filter(entry_query).distinct()

In this case, the `Post` objects that matched the search query is stored within `results`.
