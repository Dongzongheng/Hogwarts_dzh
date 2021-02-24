## 课程
- Lesson1： pytest框架及实战----计算器功能pytest测试框架及用例设计
  - pytest 介绍与安装
  - pytest 常用执行参数
  - pytest 框架结构
  - pytest 参数化与数据驱动
  - pytest fixture
- Lesson2：pytest框架及实战----计算器功能pytest测试及测试报告生成
  - fixture高级用法 
  - pytest常用插件
  - hook函数
  - Allure生成测试报告

## 个人作业地址
https://github.com/Dongzongheng/Hogwarts_dzh

## 课程总结
### Lesson 1
#### Pytest
- pytest 规则
  - 测试用例命名规范
    - 文件要在test_开头，或者_test结尾
    - 类要以Test开头，方法要以test_开头
    - 常用参数
      - pytest --collect-only 只收集用例
      - pytest -k “add ”   匹配所有名称中包含add的用例（‘add or div’ ‘TestClass’）
      - pytest  -m mark标签名  标记
      - pytest  - - junitxml=./result.xml   生成执行结果文件
      - pytest  --setup-show   回溯fixture的执行过程
 
### Lesson2
#### Pytest
- Fixture
  - Fixture作用
    - Fixture是在测试函数运行前后，由pytest执行的外壳函数，代码可以定制，满足多变的测试需求，功能包括：
      - 定义传入测试中的数据集
      - 配置测试前系统的初始状态
      - 为批量测试提供数据源等
        - Fixture 是pytest 用于将测试前后进行预备，清理工作的代码分离出核心测试逻辑的一种机制
  - Fixture用法        
    - Fixture 是为了测试⽤例的执⾏，初始化⼀些数据和⽅法
      - 1、类似 setUp, tearDown 功能，但⽐ setUp, tearDown 更灵活
      - 2、直接通过函数名字调⽤或使用装饰器@pytest.mark.usefixtures(‘test1’)
      - 3、允许使用多个Fixture
      - 4、使用 autouse 自动应用，如果要返回值，需要传fixture函数名
      - 5、作用域（session>module>class>function）
      - 6、也可以提供测试数据，实现参数化的功能
      - 7、Fixture也可以调用Fixture
#### 打包  
- 安装软件：
  - setuptools
  - pip install wheel
- 打包命令
  - python setup.py sdist bdist_wheel

#### allure 用法
- 安装使用
  - 从官网下载，并配置环境变量
- 为测试用例分类：
  - @allure.feature("name")
    @allure.story("name")
- 为测试用例加标题： 
  - @allure.title()
  
- 生成测试报告：
  - 1.生成 allure 测试结果 ：pytest —alluredir=./report/
  - 2.展示报告：allure serve ./report
  - 3.生成最终版本的报告：   allure generate ./report
  在本地搭建一个网站服务（例如：Django）
  python manage.py runserver  (http://127.0.0.1:8000/)