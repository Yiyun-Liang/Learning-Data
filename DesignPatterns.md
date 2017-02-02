# Design Patterns

### Filtering Patterns
Eg. filtering data, sampling data, generating top N from list

+ [Filtering out posts on forum that matches certain pattern](https://github.com/Yiyun-Liang/Learning-Data/blob/master/forumData/filterMapper.py)
+ [Top-N longest posts](https://github.com/Yiyun-Liang/Learning-Data/blob/master/forumData/topNMapper.py)

### Summarization Patterns
Eg. counting records, min/max, statistics, create index

+ [Inverted Index Mapper - count how many times a word is used on the forum](https://github.com/Yiyun-Liang/Learning-Data/blob/master/forumData/invertedIndexMapper.py)
+ [Inverted Index Reducer - count how many times a word is used on the forum](https://github.com/Yiyun-Liang/Learning-Data/blob/master/forumData/invertedIndexReduer.py)

#### Numerical Summarization
Eg. word/record count, mean, median, standard deviation

+ [Mean Mapper - is there any correlation between the day of the week and how much people spent on items](https://github.com/Yiyun-Liang/Learning-Data/blob/master/totalSales/meanMapper.py)
+ [Mean Reducer - is there any correlation between the day of the week and how much people spent on items](https://github.com/Yiyun-Liang/Learning-Data/blob/master/totalSales/meanReducer.py)

-> Use of combiners (like semi-reducers in MapReduce)
```
gedit ~/.bashrc
```

### Structural Patterns
Eg. combining data sets, RDBMS to Hadoop (take advantage of hierarchical data)

1) Data sources linked by foreign keys

2) Data must be structured and row based

+ [Combine Dataset Mapper - what is the reputation of a post's author](https://github.com/Yiyun-Liang/Learning-Data/blob/master/forumData/combineMapper.py)
+ [Combine Dataset Reducer - what is the reputation of a post's author](https://github.com/Yiyun-Liang/Learning-Data/blob/master/forumData/combineReducer.py)
