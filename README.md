# easy_bench

a simple benchmark utility. 

## install

```
git clone https://github.com/napman/easy_bench.git
```

or

```
wget https://raw.githubusercontent.com/napman/easy_bench/master/bench.py
```

## usage

```
from easy_bench.bench import *

with bench("some_process"):
	some_process()
```

That's it. it makes a file "benchmark.log" and stores benchmark 

## alternative usage

```
bench = Bench("some_process")
some_process()
bench.end()
```

## changing logfile name

```
set_logfile("another_logfile_name")
```

## summary

"sum.py" sums up the logs and show the summary

```
$ sum.py [logfile]
```

it's useful when you took a benchmark with loops like;

```
for i in xrange(1000):
	with bench("some_process"):
		some_process()
```


