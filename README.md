# mox-to-dataframe

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

Convert .mox (XML-based) files into clean, structured pandas DataFrames.


🚀 Overview

mox-to-dataframe is a lightweight Python package designed to parse .mox files and convert them into ready-to-use pandas DataFrames.


✨ Features
📂 Parse .mox XML files
📊 Convert channels into pandas DataFrame
⚡ Simple and fast

📦 Installation

✅ From PyPI

pip install mox-to-dataframe

🔧 From GitHub

pip install git+https://github.com/AnisToumiPhD/mox-to-dataframe.git

🧪 Usage

from mox_reader import mox_to_dataframe

df = mox_to_dataframe("trial.mox")

print(df.head())

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch

Submit a pull request

📄 License

MIT License