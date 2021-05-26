## 项目介绍
霍格沃兹测试学员 测开17期实战

## 作业地址
https://github.com/Dongzongheng/Hogwarts_dzh.git


## 报错汇总

1.AttributeError: partially initialized module 'pymysql' has no attribute 'connect' (most likely due to a circular import)
该报错大概率是由于文件名与需要导入的模块名冲突，导致循环调用，造成冲突。
