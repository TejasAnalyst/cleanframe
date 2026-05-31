# cleanframe 🪄

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

**Automated Data Cleaning for Faster Analytics**

`cleanframe` is a lightweight, fast, and intuitive Python library designed to automate dataset diagnostics and cleaning. It helps data analysts, scientists, and beginners clean messy datasets, handle missing values, drop low-quality columns, and cap outliers in just one line of code.

---

## 🚀 Features

* **One-Line Auto-Clean:** Drop duplicates, remove low-quality columns, impute missing values, and handle outliers instantly using `cf.auto_clean(df)`.
* **Advanced Outlier Handling:** Automatically detects and caps extreme numerical outliers using the Interquartile Range (IQR) method.
* **Smart Column Dropping:** Drops columns automatically if their missing data percentage crosses your defined threshold.
* **Dataset Diagnostics:** Get a quick, comprehensive report of data types, missing values, and percentages.
* **Modern Pandas Ready:** Built from the ground up to support modern Pandas (2.0+) Copy-on-Write behaviors without annoying warnings.

---

## 🛠️ Installation

*(Once published to PyPI, you can install it via pip)*

```bash
pip install cleanframe

