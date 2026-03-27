# mox-to-dataframe

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

Convert `.mox` (XML-based) files into clean pandas DataFrames.

---

## 🚀 Features

* Extracts all channels automatically
* Supports floats and scientific notation
* Handles channels with different lengths
* Returns a ready-to-use pandas DataFrame

---

## 📦 Installation

```bash
pip install .
```

---

## 🧪 Usage

```python
from mox_reader import mox_to_dataframe

df = mox_to_dataframe("Marche normale.mox")

print(df.head())
print(df.describe())
```

---

## 📦 Dependencies

* numpy
* pandas

---

## 📄 License

MIT License
# mox-to-dataframe
# mox-to-dataframe
