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
For example:
```
hadoop jar
/usr/local/Cellar/hadoop/2.7.3/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar
-files mapper.py,reducer.py -mapper mapper.py -reducer reducer.py -input
myinput -output joboutput
```

> note that myinput and joboutput are both directories,
> and hadoop will only output to directories that do not exists
> http://localhost:50030/ when cluster is running


# Random
```
hadoop jar
/usr/local/Cellar/hadoop/2.7.3/libexec/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar
-info
```
Some additional information that are extremely useful yet missing:
> -Dmapreduce.job.maps=10
> -Dmapreduce.job.reduces=10  
> -Dmapreduce.map.java.opts=-Xmx12000M
> -Dmapreduce.reduce.java.opts=-Xmx12000M
