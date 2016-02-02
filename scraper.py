import scraperwiki           
import lxml.html
import re
import urlparse     
import requests

# We're always asking for json because it's the easiest to deal with
morph_api_url = "https://api.morph.io/techwhiz/infibooks-list/data.json"

# Keep this key secret!
morph_api_key = "asPO65qEmH9YJO5XepKc"

imported_datas = requests.get(morph_api_url, params={
  'key': morph_api_key,
  'query': "select * from 'data' limit 100"
})

for imported_data in imported_datas:
  print imported_data[0]
