response类
属性或属性方法	解释
r.status_code	响应的http状态码，比如404和200
r.headers	响应头，可单独取出某个字段的值，比如(r.headers)['content-type']
r.raw	原始响应，表示urllib3.response.HTTPResponse对象。使用raw时，要求在请求时设置“stream=True”
r.url	请求的最终地址
r.encoding	要解码的r.text的编码方式
r.history	请求的历史记录，可以用于查看重定向信息，以列表形式展示，排序方式是从最旧到最新的请求
r.reason	响应状态的描述，比如 "Not Found" or "OK"
r.cookies	服务器发回的cookies，RequestsCookieJar类型
r.elapsed	从发送请求到响应到达之间经过的时间量，可以用于测试响应速度。比如r.elapsed.microseconds表示响应到达需要多少微秒
r.request	PreparedRequest对象，可以用于查看发送请求时的信息，比如r.request.headers查看请求头
r.ok	检查”status_code“的值，如果小于400，则返回True，如果不小于400，则返回False 
r.is_redirect	判断是否重定向，返回True or False
r.is_permanent_redirect	判断是否永久重定向，返回True or False
r.next	返回重定向链中下一个请求的PreparedRequest对象
r.apparent_encoding	用chardet库判断出的编码方式
r.content	响应的内容，byte类型
r.text	响应的内容，unicode类型
r.links	响应的解析头链接
较为常用的r.json()方法，用于将响应解析成json格式。
应对stream时的iter_content()和iter_line()方法，避免响应内容过大占用大量内存。




pytest发现用例规则：
1、文件名以 test_.py 或者test.py
2、编写的函数名称以 test_开头
3、编写的测试类要以Test格式命名
4、方法要以test*开头
5、所有的包package必须要有__init__.py文件

pytest.ini全局配置文件，是pytest单元测试框架的核心配置文件。

作用：pytest.ini 可以改变 pytest 的默认行为
位置：一般放在项目的根目录（即当前项目的顶级文件夹下）
命名：pytest.ini，不能使用任何中文符号，包括汉字、空格、引号、冒号等等
编码格式：GBK或者ANSI，可以使用notepad++修改编码格式
运行的规则：不管是主函数模式运行，命令行模式运行，都会去读取这个全局配置文件。
格式一般是固定的，建议将中文删掉：

[pytest]
;addopts：配置命令行参数，用空格进行分隔
;可执行标记为mark的对应用例，用or表示标记为demo或者smoke的用例都会执行
addopts = -vs  --alluredir=./results/json --clean-alluredir -m "demo or smoke"

;注册 mark 标记
markers =
    demo : marks tests as demo
    smoke: marks tests as smoke
    uat : marks tests as uat
    test : marks tests as test

minversion = 5.0

;测试用例的路径，可自己配置，
;../pytestproject为上一层的pytestproject文件夹
;./testcase为pytest.ini当前目录下的同级文件夹
;改变用例的查找路径规则，当前目录的testcase文件夹
testpaths =./testcase

;模块名的规则，配置测试搜索的模块文件名称
python_files = test*.py

;类名的规则，配置测试搜索的测试类名
python_classes = Test*

;方法名的规则，配置测试搜索的测试函数名
python_functions = test


一、addopts配置：参数详解
-s：表示输出调试信息，用于显示测试函数中print()打印的信息

-v：未加前只打印模块名，加v后打印类名、模块名、方法名，显示更详细的信息

-q：表示只显示整体测试结果

-vs：这两个参数可以一起使用

-n：支持多线程或者分布式运行测试用例（前提需安装：pytest-xdist插件）

–html：生成html的测试报告（前提需安装：pytest-html插件） 如：pytest -vs --html ./reports/result.html

--reruns num： 用例失败后重跑，跑几次（前提需安装：pytest-rerunfailures插件） 如：pytest -vs --reruns=2

-x：表示只要出现一个用例失败报错则停止执行，如：pytest -vs -x
–maxfail：表示出现几个用例失败报错，则终止测试，如：pytest -vs --maxfail=2
-k：模糊匹配，运行测试用例名称中包含某个字符串的测试用例： 如： pytest -vs -k “ao or userPage”
————————————————
注册 mark 标记
我们可以在测试用例上输入@pytest.mark.login来对用例进行标记，但有时手误可能输入成@pytest.mark.loggin；这不会引起程序错误，它会以为你新加了一个标记：loggin。
为了避免这种拼写错误，避免遗漏执行测试用例。可以在ini文件中，对所有用到的标记做注册，这样程序中添加未注册的标记时就会报错。
：后面的文字，是对该标记做的说明。
testpaths配置
1）pytest默认是搜索执行当前目录下的所有以test_开头的测试用例；我们可以在pytest.ini配置testpaths = test_case/test_001.py，则只执行当前配置的文件夹下或文件里的指定用例
2）可配置多个，空格隔开：python_files = test_.py haha_.py
[pytest]
;命令行参数，用空格进行分隔
addopts = -vs --alluredir ./temp

markers =
    demo : marks tests as demo
    smoke: marks tests as smoke
    uat : marks tests as uat
    test : marks tests as test

minversion = 5.0

;测试用例文件夹，可自己配置，
;../pytestproject为上一层的pytestproject文件夹
;./testcase为pytest.ini当前目录下的同级文件夹
testpaths =./testcase

;配置测试搜索的模块文件名称
python_files = test*.py

;配置测试搜索的测试类名
python_classes = Test*

;配置测试搜索的测试函数名
python_functions = test


------------------------------------------------------------------------------------
pytest中的fixture
一、pytest中的fixture是什么
为可靠的和可重复执行的测试提供固定的基线（可以理解为测试的固定配置，使不同范围的测试都能够获得统一的配置），fixture提供了区别于传统单元测试（setup/teardown）风格的令人惊喜的功能，而且pytest做得更炫。
二、pytest中fixture的使用
- fixture 可以作为一个函数的参数被调用
被fixture装饰的函数可以作为参数使用

```python
import pytest
@pytest.fixture
def a():
    pass
def b(a):
    pass
```
- fixture可以在一个类、或者一个模块、或者整个session中被共享，加上范围即可
```python
import pytest
@pytest.fixture(scope=class,autouse=False，name='')
def conn():
    print('之前的操作')
    yield 
    print('之后的操作')
```
- scope可以是function，可以是class,可以是module，可以是session 表示作用域
- autouse表示是否自动执行，如果是True则自动在scope作用域下的之前或之后执行。False，则在指定作用域下加上fixture的名字才会执行
比如：
```python
@pytest.fixture(scope=class,autouse=False)
def conn():
    print('之前的操作')
    yield 
    print('之后的操作')
    
class dde:
    def a():
        pass
    #这个就不执行
    def b(conn):
        pass
    #这个执行
```
- 一般会将装饰器封装到独立的py文件，如：
conftest.py
```python
import pytest
@pytest.fixture(scope=class,autouse=False)
def conn():
    print('之前的操作')
    yield 
    print('之后的操作')
```
###params 是一个列表，用来存放我们要参数化的值。
```python
import pytest
@pytest.fixture(scope=class,autouse=False,params=['a','b'])
def conn():
    print('之前的操作')
    yield request.param
    print('之后的操作')
```
会将a,b分俩次传给装饰器并返回。
###name
name是重命名装饰器名字，会覆盖原来的。
###ids
给参数重命名，与params搭配使用。
YAML 是 "YAML Ain't a Markup Language"（YAML 不是一种标记语言）的递归缩写。在开发的这种语言时，YAML 的意思其实是："Yet Another Markup Language"（仍是一种标记语言）。

YAML 的语法和其他高级语言类似，并且可以简单表达清单、散列表，标量等数据形态。它使用空白符号缩进和大量依赖外观的特色，特别适合用来表达或编辑数据结构、各种配置文件、倾印调试内容、文件大纲（例如：许多电子邮件标题格式和YAML非常接近）。

YAML 的配置文件后缀为 .yml，如：runoob.yml 。

基本语法
大小写敏感
使用缩进表示层级关系
缩进不允许使用tab，只允许空格
缩进的空格数不重要，只要相同层级的元素左对齐即可
'#'表示注释
数据类型
YAML 支持以下几种数据类型：

对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
纯量（scalars）：单个的、不可再分的值
YAML 对象
对象键值对使用冒号结构表示 key: value，冒号后面要加一个空格。

也可以使用 key:{key1: value1, key2: value2, ...}。

还可以使用缩进表示层级关系；

key: 
    child-key: value
    child-key2: value2
较为复杂的对象格式，可以使用问号加一个空格代表一个复杂的 key，配合一个冒号加一个空格代表一个 value：

?  
    - complexkey1
    - complexkey2
:
    - complexvalue1
    - complexvalue2
意思即对象的属性是一个数组 [complexkey1,complexkey2]，对应的值也是一个数组 [complexvalue1,complexvalue2]

YAML 数组
以 - 开头的行表示构成一个数组：

- A
- B
- C
YAML 支持多维数组，可以使用行内表示：

key: [value1, value2, ...]
数据结构的子成员是一个数组，则可以在该项下面缩进一个空格。

-
 - A
 - B
 - C
一个相对复杂的例子：

companies:
    -
        id: 1
        name: company1
        price: 200W
    -
        id: 2
        name: company2
        price: 500W
意思是 companies 属性是一个数组，每一个数组元素又是由 id、name、price 三个属性构成。

数组也可以使用流式(flow)的方式表示：

companies: [{id: 1,name: company1,price: 200W},{id: 2,name: company2,price: 500W}]
复合结构
数组和对象可以构成复合结构，例：

languages:
  - Ruby
  - Perl
  - Python 
websites:
  YAML: yaml.org 
  Ruby: ruby-lang.org 
  Python: python.org 
  Perl: use.perl.org
转换为 json 为：

{ 
  languages: [ 'Ruby', 'Perl', 'Python'],
  websites: {
    YAML: 'yaml.org',
    Ruby: 'ruby-lang.org',
    Python: 'python.org',
    Perl: 'use.perl.org' 
  } 
}
纯量
纯量是最基本的，不可再分的值，包括：

字符串
布尔值
整数
浮点数
Null
时间
日期
使用一个例子来快速了解纯量的基本使用：

boolean: 
    - TRUE  #true,True都可以
    - FALSE  #false，False都可以
float:
    - 3.14
    - 6.8523015e+5  #可以使用科学计数法
int:
    - 123
    - 0b1010_0111_0100_1010_1110    #二进制表示
null:
    nodeName: 'node'
    parent: ~  #使用~表示null
string:
    - 哈哈
    - 'Hello world'  #可以使用双引号或者单引号包裹特殊字符
    - newline
      newline2    #字符串可以拆成多行，每一行会被转化成一个空格
date:
    - 2018-02-17    #日期必须使用ISO 8601格式，即yyyy-MM-dd
datetime: 
    -  2018-02-17T15:02:31+08:00    #时间使用ISO 8601格式，时间和日期之间使用T连接，最后使用+代表时区
引用
& 锚点和 * 别名，可以用来引用:

defaults: &defaults
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  <<: *defaults

test:
  database: myapp_test
  <<: *defaults
相当于:

defaults:
  adapter:  postgres
  host:     localhost

development:
  database: myapp_development
  adapter:  postgres
  host:     localhost

test:
  database: myapp_test
  adapter:  postgres
  host:     localhost
& 用来建立锚点（defaults），<< 表示合并到当前数据，* 用来引用锚点。

下面是另一个例子:

- &showell Steve 
- Clark 
- Brian 
- Oren 
- *showell 
转为 JavaScript 代码如下:

[ 'Steve', 'Clark', 'Brian', 'Oren', 'Steve' ]