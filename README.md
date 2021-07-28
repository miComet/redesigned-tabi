# redesigned-tabi

## Launch service locally

### Step 1: Launch db

```shell=
# start
$ ./scripts/launch_db.sh

# stop
<press Ctrl+c>
<Enter your password to sudo for DELETING THE DBFILES GENERATED>
```

### Setep 2: Launch backend

```shell=
$ ./scripts/launch_backend.sh /path/to/json/dir/
```

## Launch service all inside docker

```shell=
$ ./scripts/launch_all_in_docker.sh [/path/to/json/dir/]
```

Note: The argument of json dir is optional.

## Launch service all inside docker(2)

-   For someone who dosen't have bash in their env or just want to run it manually.

```shell=
$ export PROJECT_DIR=<project root>
$ export STORAGE_SUBDIR=<the RELATIVE path under project root to store data generated by services>

$ mkdir -p $PROJECT_DIR/$STORAGE_SUBDIR
$ cd $PROJECT_DIR
$ docker-compose up
```

Note: You have to delete all the file under the storage path, after you finish the test.

## To run docker actions locally for unittest

-   Prerequisite: install [nektos/act](https://github.com/nektos/act)

```shell=
$ act -j list-events-test -b
```
