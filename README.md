# Learning-Data

# Useful Commands
To start and stop node cluster.
```
hstart, hstop
```

```
hadoop fs -ls
hadoop fs -put <filename>
hadoop fs -get <filename>
```

# Local Test

```
head -50 purchases.txt > testfile
cat testfile | python mapper.py | sort | python reducer.py
```

# Hadoop Test
```
hadoop jar <jar location> -mapper mapper.py -reducer reducer.py -file mapper.py
-file reducer.py -input myinput -output joboutput
```
> note that myinput and joboutput are both directories,
> and hadoop will only output to directories that do not exists
> http://localhost:50030/ when cluster is running
