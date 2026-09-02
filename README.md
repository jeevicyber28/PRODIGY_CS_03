# 🔐 Password Complexity Checker

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Cybersecurity-Password%20Security-00C853?style=for-the-badge">
  <img src="https://img.shields.io/badge/CLI-Application-212121?style=for-the-badge&logo=windows-terminal&logoColor=white">
</p>

<p align="center">
  <b>A simple Python-based tool to evaluate password complexity and provide improvement suggestions.</b>
</p>

---

## 📌 Project Overview

The **Password Complexity Checker** is a Python-based cybersecurity project designed to evaluate the strength of a password using a set of basic complexity requirements.

The program accepts a password from the user and checks whether it contains:

- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

Each successful requirement increases the password strength score by `1`.

The maximum possible score is `5`.

Based on the final score, the password is classified as:

| Score | Password Strength |
|:---:|---|
| `0 - 2` | 🔴 Weak |
| `3 - 4` | 🟡 Moderate |
| `5` | 🟢 Strong |

If a requirement is not satisfied, the program also provides suggestions to improve the password.

---

## 🎯 Objectives

The main objectives of this project are:

- To understand password complexity requirements
- To implement password validation using Python
- To use regular expressions for character checking
- To calculate password strength using a scoring system
- To provide useful feedback to the user
- To practice Python functions and conditional statements
- To understand a basic cybersecurity password-security concept

---

## ✨ Features

- 🔐 Password complexity checking
- 📏 Minimum length validation
- 🔠 Uppercase letter detection
- 🔡 Lowercase letter detection
- 🔢 Number detection
- 🔣 Special character detection
- 📊 Strength score calculation
- 💡 Suggestions for missing requirements
- 💻 Command-line interface
- 🐍 Python implementation
- 🔎 Regular-expression-based validation

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| `re` module | Regular expression based validation |
| CLI | User interaction |

---

## 📂 Project Structure

```text
PRODIGY_CS_03/
│
├── password_checker.py
│
└── README.md
