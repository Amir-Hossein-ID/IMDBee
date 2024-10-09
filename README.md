# IMDBee
a python module to retrieve data from imdb

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

# TODO
- auto complete field names
- documentation
