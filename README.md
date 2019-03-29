## Python 学习路径

记录自己学习 Python 的点点滴滴。

## 作用：

- 爬虫
- 大数据与数据分析（Spark）
- 自动化运维与自动化测试
- Web 开发（Flask、Django）
- 机器学习（Tensor Flow）
- 胶水语言（混合其他如 C++、Java 等来编程。能够用将其他模块轻松联动到一起）

## 数据类型：

### 字符串

- 普通字符串： 'hello world'
- 多行字符串：

  - 写法 1：

    > '''
    > hello
    >
    > word
    > '''

  - 写法 2：
    > '''
    > hello\
    >
    > word
    > '''

- 转义字符

  > \n 换行

  > \\' 单引号

  > \t 横向制表符

  > 等等很多

  - 特殊的字符：
    1. 无法“看见“的字符；
    2. 与语言本身语法有冲突的符；

- 获取指定长度的字符串
  - 字符串[a:b]
  - a - start
  - b - end
  - a 和 b 都可以被省略
    > "hello world[0:5]" //hello

### 组（List）

- 例如：
  > [[1, 2, 3]], 'test', true, 4]

#### 元祖（Tuple）

- 例如：
  > (1, 2, 'asd', true)
- 访问：
  > (1,2,3)[0:2] // (1,2,3)
  >
  > (1,2,3)\*3 // (1,2,3,1,2,3,1,2,3)

### 集合（set）

- 例如
  > {1,2,3}
- 特点

  1.无序

  2.不重复

- 排重的写法
  > {1,2,3} - {1,2} // {3}
- 交集 - 寻找相同的成员
  > {1,2,3} & {1,2} // {1,2}
- 并集 - 去除已存在的成员
  > {1,2,3} | {3,4,5} // {1,2,3,4,5}

### 字典（dict）

- 例如

  > { key: value ... }
  >
  > { 'q': '测试' }['q'] // 测试

- 注意
  - 不能有重复的 key（键）
  - 键名可以是字符串也可以是数字

## 变量

- 定义
  - > A = [1, 2, 3, 4, 5, 6]
- 命名规则
  - 变量名首字符不能是数字
  - 可以用字母、数字、下划线来组合
  - 不可以使用系统保留的关键字