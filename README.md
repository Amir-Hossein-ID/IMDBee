# IMDBee
A python module to retrieve data from imdb

# Install
```console
$ python -m pip install IMDBee
```

# How to Use

```python
from IMDBee import Query, fetch

query = Query()
title = query.title(id='tt0468569')

# tell the library which details you need
title.title_text.text()

# fetch the requested data
title = fetch(query).title

print(title.title_text.text)s # -> "The Dark Knight"

```

# Why IMDBee
- Unlike similar libraries IMDBee doesn't scrape title pages to get info, it gets the only information you need without any additional data and this makes it fast.
- ...

# TODO
- auto complete field names
- documentation
