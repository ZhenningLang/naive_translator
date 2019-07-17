# naive_translator

A very simple translator based on a word to word dictionary

(Though this project is designed to convert traditional 
Chinese to simplified, it owns the ability to do more things.)

[Chinese Doc](docs/README_CH.md)

## 1. How to Use

### 1.1 Installation

```bash
pip3 install naive_translator
```

### 1.2 Use as a package

```text
>>> from naive_translator import translator
>>> translation = translator('豐田的上門女婿和女人')
>>> print(translation)
丰田的上门女婿和女人
```

### 1.3 Use as a server

To start the server, run the following command

```bash
naive_translator 8001
```

Then you could visit

|Url|Explanation|
|:---|:---|
|http://localhost:8001|A welcome page|
|http://localhost:8001/dicts|List all available dictionaries|
|http://localhost:8001/translate?dict=&text=|Translate|

## Others

- Dictionary files are placed in `naive_translator/data` directory
- Configure file is `naive_translator/config.py`
