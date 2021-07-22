# redesigned-tabi

## Start & Stop db
Only for test/dev:

```shell=
# start
$ cd scripts
$ ./db_start.sh

# stop
<press Ctrl+c>
<Enter your password to sudo for DELETING THE DBFILES GENERATED>
```

## Start Web service
Make sure that the db service is running.

```shell=
$ python3 run.py
```

## Add dummy data to db
Make sure that the db service is running.

```shell=
$ python3 load.py
```
