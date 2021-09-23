| The Link Your Class                        | https://bbs.csdn.net/forums/MUEE308FZ?category=0             |
| :----------------------------------------- | :----------------------------------------------------------- |
| The Link of Requirement of This Assignment | https://bbs.csdn.net/topics/600798588                        |
| The Aim of This Assignment                 | Code personally & learn git and github & learn the process of writing a project & learn unit test and performance test |
| MU STU ID and FZU STU ID                   | 19104308 & 831901320                                         |

### GitHub Repository



## Code Standard（Python)



## PSP Form

| Personal Software Process Stages | Estimated Time/hours | Completed Time/hours |
| :------------------------------- | :------------------- | :------------------- |
| Planning                         | 1.5                  | 2                    |
| Estimate                         | 0.5                  | 0.5                  |
| Development                      | 10                   | 10                   |
| Analysis                         | 15                   | 10                   |
| Design Spec                      | 1                    | 1                    |
| Design Review                    | 1                    | 1                    |
| Coding Standard                  | 1.5                  | 2                    |
| Design                           | 2                    | 2                    |
| Coding                           | 12                   | 10                   |
| Code Review                      | 5                    | 3                    |
| Test                             | 5                    | 2.5                  |
| Reporting                        | 3                    | 1.5                  |
| Test Report                      | 2                    | 1                    |
| Size Measurement                 | 0.5                  | 0.5                  |
| Postmortem&Process Improvement   | 2                    | 2                    |
| total                            | 62                   | 49                   |

## Problem-Solving Ideas

- 一开始看到这道题的时候感觉还挺平易近人的，起码能够完全看懂题目，没有一开始就出现一些让人需要搜索才能懂的词汇；题目主要涉及到的是对于文本的字符串操作，需要从C/C++文件中提取出足够的信息，用于判断代码的结构，最终达到关键字提取的目的；
- 在读完该题后，我首先想到的是用最简单的字典配对方法来进行关键字查找，想到C语言还要用到 <vector> ，Java 我通常是来进行数据处理使用的，于是我选择了可能相对更简单的 Python 。

## My Study

- 我首先学习了Git的使用，学习了Git的几块内容，文件上传到缓存区，文件评论，以及仓库克隆和更新，分支的使用等等。但是我看的教程太过古老，我还是使用原先的账号密码操作而不是个人令牌，以及私有邮箱的问题。我在网上找了其他教程，才解决了这个问题。

- 关于正则表达式的问题，大一学过太久没用了我已经忘记的差不多了，虽然 <vector> 还记得，但我还是更想使用Python，于是再去看教程学了正则表达式的使用。

- 关于个人代码标准，我在写完代码后去知乎了解了一下具体的内容，然后找到了 Google 代码规范，从中选出我自己的代码规范。

- 关于 Python 栈的使用，我又忘光了，于是我还是去找教程学习。

- 在数据处理方面，我也参考了一些CSDN的资料，虽然最后发现数据处理可能是多此一举，但我还是放上来了。

- ```正则表达式
  我使用了以下几个正则表达式
  - 所有注释：(//.*)|(/\*[\s\S]*?\*/)|(/\*[\s\S]*)
  - 单引号字符串：(\'[\s\S]*?\')|(\'[\s\S]*)
  - 双引号字符串：(\”[\s\S]*?\“)|(\”[\s\S]*)
  - 所有可能为关键字的字符串：[a-zA-Z]{2,}
  ```

  

## Data Processing

- 拿到 C/C++ 文件后，首先需要进行的是数据处理，由于是从 Python 中读取 C/C++ 文件，我首先想到的是将文件后缀全部改成 txt 文件，然后将文件中的注释全部删除，在删除的同时我想到了使用正则表达式删除。但就引出了新的问题，我是在文件处理部分先删除注释和关键字后的大括号来方便我后续使用字典查询，还是直接用关键词的正则表达式呢？我不想在数据处理耗太多时间，所以选择了在后续的代码使用正则表达式（虽然后面发现这四个作业都能使用栈完成）。

```python
import os
import sys
import re

files = os.listdir('.')
for filename in files:
	portion = os.path.splitext(filename)
	if portion[1] == ".cpp" or portion[1] == ".c":
		
		newname = "test" + ".txt"
		os.rename(filename,newname)

PY_PATTERN = re.compile(

	r"""

     \s*\#(?:[^\r\n])*

     | \s*__(?:[^\r\n]*)

     | "{3}(?:\\.|[^\\])*"{3}

     | '{3}(?:\\.|[^\\])*'{3}

     """,

	re.VERBOSE | re.MULTILINE | re.DOTALL

)

txt = open("test.txt").readlines()

b = re.sub(PY_PATTERN, '', ''.join(txt))

single = re.compile(r"\n\n")

b = re.sub(single, '\n', b)

print(b)
```

## Step1：Output "keyword" statistics

- 我首先建立了一个list,用来存放关键词，然后用几个正则表达式转换的关键词进行迭代遍历，来与之前的list 进行配对，得出了个没有打印出来的数组 count[key] ,以及一次次配对成功累加的总数。

```python
def keywords_num (code):
    count = {}
    Key_sum = 0
    key_list = ['auto','break','case','char','const','continue','default','do','if','while','static','double','else','enum','extern','float','for','goto','int','long','register','return','short','signed','sizeof','struct','switch','typedef','union','unsigned','void','volatile']
    for key in key_list:
        n = len(re.findall("[^0-9a-zA-Z\_]" + key + "[^0-9a-zA-Z\_]", code))
        if n != 0:
            count[key] = n
            Key_sum += n
    print('The total num is: ',Key_sum)
    #return Key_sum
```

## Step2 And Step3：'Switch case' And 'if else'

同时统计 switch 的个数和 case 的个数，相减可以得出每组的 case 个数，但我认为结果是对的可能是这次的示例代码刚好对，所以请看后面的测试验证。

```python
def switch_num(code):
    case_num = []
    switch_num = 0
    switch_list = re.finditer(r"\sswitch\([^)]*\)\s*{",code)
    for i in switch_list:
        switch_num += 1
        index = i.end()
        case_list = re.findall(r"\scase\s",code[index:])
        case_num.append(len(case_list))
    for j in range(switch_num-1):
        case_num[j] = case_num[j]-case_num[j+1]
    print ('The swith num is: ',switch_num)
    print('The case num is',case_num[0],case_num[1])
    #return switch_num, case_num
```

## Step4:'if, else if, else' 

用 Python 的栈，在队列中判断是否是 if 与 else if，如果是就将其入栈。在队列中判断 else ，然后判断前一个是 if 还是 else if，是 if 将 if-else +1 并出栈 if ，是else if将if-else if-else +1 并一直出栈到第一个 if 出栈。

```
def count_if_else(code):
    if_stack = []
    # if-else num
    if_else_num1 = 0
    # if-elseif-else num
    if_else_num2 = 0
    match_else_if = False
    #find all if、elseif、else
    all_list = re.findall(r"else if|\s*else[{\s][^i]|if", code)
    for i in range(len(all_list)):
        if all_list[i] == "if":
            if_stack.append(1)
        elif all_list[i] == "else if":
            if_stack.append(2)
        else:
            while True:
                if if_stack.pop() == 2:
                    match_else_if = True
                else:
                    break
            if match_else_if:
                if_else_num2 += 1
                match_else_if = False
            else:
                if_else_num1 += 1
    
    return if_else_num1,if_else_num2

```

## Unit Coverage And Performance Testing





# **Summary**

这次代码还是比较难的，因为Python这部分代码我基本上忘光了，这个是个问题，所以我是边学边做一步步做下去的。在打代码时还是遇到了许多问题，多亏了百度和 Google ,让我成功度过难关。在这次代码的项目作业我也意识到自己和身边同学之间的差距，还后面的项目中我需要抓紧赶上来！

