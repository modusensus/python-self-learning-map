la

# Python 内置函数速查手册

> Python 3.x 共有 **70+** 个可直接使用的内置函数，无需 `import`。
> 分类整理，方便查阅学习。

---

## 📖 速查索引

| 分类                               | 函数                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| [类型转换](#1-类型转换)             | `int` `float` `str` `bool` `list` `tuple` `set` `dict` `chr` `ord` `bin` `oct` `hex`           |
| [输入输出](#2-输入输出)             | `print` `input` `format`                                                                                           |
| [数学运算](#3-数学运算)             | `abs` `sum` `round` `min` `max` `pow` `divmod`                                                             |
| [序列与集合](#4-序列与集合)         | `len` `range` `enumerate` `zip` `map` `filter` `sorted` `reversed` `slice` `all` `any`             |
| [对象与属性](#5-对象与属性)         | `type` `id` `isinstance` `issubclass` `hasattr` `getattr` `setattr` `delattr` `dir` `vars` `super` |
| [迭代器与生成器](#6-迭代器与生成器) | `iter` `next`                                                                                                        |
| [文件与代码执行](#7-文件与代码执行) | `open` `exec` `eval` `compile` `__import__`                                                                    |
| [帮助与调试](#8-帮助与调试)         | `help` `repr` `hash` `memoryview` `breakpoint`                                                                 |
| [其他 / 装饰器](#9-其他--装饰器)    | `callable` `staticmethod` `classmethod` `property` `globals` `locals` `ascii` `ord`                      |

---

## 1. 类型转换

| 函数                | 说明                 | 示例                                              |
| ------------------- | -------------------- | ------------------------------------------------- |
| `int(x)`          | 转整数               | `int("42")` → `42`                           |
| `float(x)`        | 转浮点数             | `float("3.14")` → `3.14`                     |
| `str(x)`          | 转字符串             | `str(123)` → `"123"`                         |
| `bool(x)`         | 转布尔值             | `bool(1)` → `True`，`bool(0)` → `False` |
| `list(iterable)`  | 转列表               | `list("abc")` → `['a', 'b', 'c']`            |
| `tuple(iterable)` | 转元组               | `tuple([1,2,3])` → `(1, 2, 3)`               |
| `set(iterable)`   | 转集合（去重）       | `set([1,1,2])` → `{1, 2}`                    |
| `dict(mapping)`   | 转字典               | `dict([("a",1)])` → `{'a': 1}`               |
| `chr(i)`          | Unicode 编码 → 字符 | `chr(65)` → `'A'`                            |
| `ord(c)`          | 字符 → Unicode 编码 | `ord('A')` → `65`                            |
| `bin(x)`          | 转二进制字符串       | `bin(10)` → `'0b1010'`                       |
| `oct(x)`          | 转八进制字符串       | `oct(8)` → `'0o10'`                          |
| `hex(x)`          | 转十六进制字符串     | `hex(255)` → `'0xff'`                        |

---

## 2. 输入输出

| 函数                    | 说明                       | 示例                                    |
| ----------------------- | -------------------------- | --------------------------------------- |
| `print(*objects)`     | 打印输出                   | `print("hello", "world", sep="-")`    |
| `input(prompt)`       | 获取用户输入（返回字符串） | `name = input("请输入名字：")`        |
| `format(value, spec)` | 格式化值                   | `format(3.1415, ".2f")` → `"3.14"` |

---

## 3. 数学运算

| 函数                       | 说明                     | 示例                             |
| -------------------------- | ------------------------ | -------------------------------- |
| `abs(x)`                 | 绝对值                   | `abs(-5)` → `5`             |
| `sum(iterable)`          | 求和                     | `sum([1, 2, 3])` → `6`      |
| `round(number, ndigits)` | 四舍五入                 | `round(3.1415, 2)` → `3.14` |
| `min(iterable)`          | 最小值                   | `min(3, 1, 2)` → `1`        |
| `max(iterable)`          | 最大值                   | `max(3, 1, 2)` → `3`        |
| `pow(x, y)`              | 幂运算（等于`x ** y`） | `pow(2, 3)` → `8`           |
| `divmod(a, b)`           | 返回 (商, 余数)          | `divmod(10, 3)` → `(3, 1)`  |

---

## 4. 序列与集合

| 函数                         | 说明                         | 示例                                                     |
| ---------------------------- | ---------------------------- | -------------------------------------------------------- |
| `len(s)`                   | 返回长度                     | `len("hello")` → `5`                                |
| `range(stop)`              | 生成整数序列                 | `list(range(5))` → `[0,1,2,3,4]`                    |
| `enumerate(iterable)`      | 带索引遍历                   | `list(enumerate(["a","b"]))` → `[(0,'a'),(1,'b')]`  |
| `zip(*iterables)`          | 打包成元组                   | `list(zip([1,2], ["a","b"]))` → `[(1,'a'),(2,'b')]` |
| `map(func, iterable)`      | 对每个元素执行函数           | `list(map(str, [1,2,3]))` → `['1','2','3']`         |
| `filter(func, iterable)`   | 过滤出满足条件的元素         | `list(filter(lambda x: x>0, [-1,0,2]))` → `[2]`     |
| `sorted(iterable)`         | 排序（返回新列表）           | `sorted([3,1,2])` → `[1,2,3]`                       |
| `reversed(seq)`            | 反转序列                     | `list(reversed([1,2,3]))` → `[3,2,1]`               |
| `slice(start, stop, step)` | 切片对象                     | `"hello"[slice(1,4)]` → `"ell"`                     |
| `all(iterable)`            | 全部为`True` 返回 `True` | `all([True, 1, "a"])` → `True`                      |
| `any(iterable)`            | 任一为`True` 返回 `True` | `any([False, 0, "a"])` → `True`                     |

---

## 5. 对象与属性

| 函数                          | 说明                      | 示例                                           |
| ----------------------------- | ------------------------- | ---------------------------------------------- |
| `type(obj)`                 | 返回对象类型              | `type(42)` → `<class 'int'>`              |
| `id(obj)`                   | 返回内存地址（唯一标识）  | `id("hello")`                                |
| `isinstance(obj, class)`    | 判断类型                  | `isinstance(3.14, (int, float))` → `True` |
| `issubclass(cls, base)`     | 判断是否为子类            | `issubclass(bool, int)` → `True`          |
| `hasattr(obj, name)`        | 是否有某属性              | `hasattr("hello", "upper")` → `True`      |
| `getattr(obj, name)`        | 获取属性                  | `getattr("hello", "upper")()` → `"HELLO"` |
| `setattr(obj, name, value)` | 设置属性                  | `setattr(obj, "x", 10)`                      |
| `delattr(obj, name)`        | 删除属性                  | `delattr(obj, "x")`                          |
| `dir(obj)`                  | 列出所有属性和方法        | `dir("hello")`                               |
| `vars(obj)`                 | 返回`__dict__` 属性字典 | `vars(obj)`                                  |
| `super()`                   | 调用父类方法              | `super().__init__()`                         |

---

## 6. 迭代器与生成器

| 函数               | 说明           | 示例                                         |
| ------------------ | -------------- | -------------------------------------------- |
| `iter(obj)`      | 获取迭代器     | `it = iter([1,2,3])`                       |
| `next(iterator)` | 获取下一个元素 | `next(it)` → `1`，`next(it)` → `2` |

```python
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
```

---

## 7. 文件与代码执行

| 函数                     | 说明                         | 示例                                        |
| ------------------------ | ---------------------------- | ------------------------------------------- |
| `open(file, mode)`     | 打开文件                     | `open("test.txt", "r", encoding="utf-8")` |
| `exec(code)`           | 执行 Python 代码（无返回值） | `exec("x = 10")`                          |
| `eval(expr)`           | 计算表达式（有返回值）       | `eval("1 + 2 * 3")` → `7`              |
| `compile(source, ...)` | 编译代码为字节码             | 高级用法，了解即可                          |
| `__import__(name)`     | 动态导入模块                 | `__import__("math")`                      |

> ⚠️ `exec` 和 `eval` 有安全风险，不要用于执行用户输入。

---

## 8. 帮助与调试

| 函数                | 说明                            | 示例                               |
| ------------------- | ------------------------------- | ---------------------------------- |
| `help(obj)`       | 查看帮助文档                    | `help(print)`                    |
| `repr(obj)`       | 返回对象的"官方"字符串表示      | `repr("hello")` → `"'hello'"` |
| `hash(obj)`       | 返回哈希值                      | `hash("hello")`                  |
| `memoryview(obj)` | 内存视图（处理二进制数据）      | `memoryview(b"abc")`             |
| `breakpoint()`    | 设置断点（调试用，Python 3.7+） | `breakpoint()`                   |

---

## 9. 其他 / 装饰器

| 函数                   | 说明                      | 示例                            |
| ---------------------- | ------------------------- | ------------------------------- |
| `callable(obj)`      | 判断是否可调用            | `callable(print)` → `True` |
| `staticmethod(func)` | 静态方法装饰器            | 用`@staticmethod`             |
| `classmethod(func)`  | 类方法装饰器              | 用`@classmethod`              |
| `property(fget)`     | 属性装饰器                | 用`@property`                 |
| `globals()`          | 返回全局变量字典          | `globals()`                   |
| `locals()`           | 返回局部变量字典          | `locals()`                    |
| `ascii(obj)`         | 返回 ASCII 可表示的字符串 | `ascii("中文")`               |

---

## 🎯 学习路线建议

### 第一阶段：必会（每天用）

```
print, input, int, float, str, bool, list, len, range, type
```

### 第二阶段：常用（每周用）

```
dict, tuple, set, sorted, enumerate, zip, min, max, sum, abs, round, open, isinstance, format
```

### 第三阶段：进阶（按需学）

```
map, filter, all, any, iter, next, reversed, slice, property, staticmethod, classmethod, super, breakpoint
```

---

## 🔍 快速查询

```python
# 查看所有内置函数
print(dir(__builtins__))

# 查看某个函数的详细用法
help(print)

# 查看某个函数的简单说明
print(print.__doc__)
```

---

> 💡 **提示：** 不需要一次性记完所有函数，遇到不熟悉的查这个文档就行。
> 用得多了自然就记住了。
