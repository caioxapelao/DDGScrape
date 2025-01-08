# How to use
```Bash
git clone https://github.com/caioxapelao/DDGScrape.git
```
make sure the folder is on the same directory as your python/ipython script, then you can do
```Python
from DDGScrape import scrape

results = scrape("what does a turtle like to eat")
print(results[0])
```
the output structure is
```JSON
{
'title': 'title',
'url': 'url',
'description': 'description',
'date': 'date'
}
```
