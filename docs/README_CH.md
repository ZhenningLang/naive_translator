# naive_translator

基于一一对应字典的简单翻译器

(尽管该项目最初被用于繁体汉字转简体，但它被设计为可以支持更多翻译任务的框架形式)

## 1. 安装与使用

### 1.1 安装

```bash
pip3 install naive_translator
```

### 1.2 以包导入的形式使用

```text
>>> from naive_translator import translator
>>> translation = translator('豐田的上門女婿和女人')
>>> print(translation)
丰田的上门女婿和女人
```

### 1.3 以 Http 服务的形式使用

执行下面的命令在端口 `8001` 开启服务

```bash
naive_translator 8001
```

访问下面所列的接口

|Url|Explanation|
|:---|:---|
|http://localhost:8001|A welcome page|
|http://localhost:8001/dicts|List all available dictionaries|
|http://localhost:8001/translate?dict=&text=|Translate|

## 其他

- 字典文件放置在 `naive_translator/data` 目录
- 配置文件为 `naive_translator/config.py`
