# 🔐 Password Complexity Checker

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-00C853?style=for-the-badge&logo=hackthebox&logoColor=white" />
  <img src="https://img.shields.io/badge/Type-Security%20Tool-FF6F00?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Interface-CLI-212121?style=for-the-badge&logo=windows-terminal&logoColor=white" />
</p>

<p align="center">
  <b>A simple Python-based tool for evaluating password complexity and providing security recommendations.</b>
</p>

---

## 📌 About The Project

**Password Complexity Checker** is a Python-based cybersecurity utility designed to evaluate the strength of a password using a set of commonly used complexity requirements.

The application accepts a password from the user and checks whether it satisfies five important conditions:

- Minimum password length
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Presence of special characters

Each satisfied requirement contributes to the password's overall strength score.

The program then classifies the password as:

- 🟢 **Strong**
- 🟡 **Moderate**
- 🔴 **Weak**

If one or more requirements are missing, the application also provides specific suggestions to help improve the password.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Understand the fundamentals of password security
- Implement password complexity validation using Python
- Practice regular expressions
- Work with functions and conditional statements
- Implement a simple scoring mechanism
- Provide meaningful feedback to users
- Understand how password policies can be implemented programmatically
- Build a small cybersecurity-focused command-line application

---

# 🚀 Key Features

### 🔐 Password Length Validation

Checks whether the password contains at least **8 characters**.

```text
Minimum requirement: 8 characters
