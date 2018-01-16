# cafebazaar-inlineapps
simple crawler that can index all of the Cafebazaar inline applications.

#### To get top 3 apps run based on users and rates

```
python main.py -c 3
```

#### To get top 3 apps run based on rates only

```
python main.py -c 3 -s true
```

```bash
usage: main.py [-h] [-s SORT] [-c COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -s SORT, --sort SORT  sort only with rates, default is count*rate
  -c COUNT, --count COUNT
                        count of inline-apps

```