# 🔐 Password Generator (CLI)
A simple and secure Python-based CLI tool to generate random passwords using letters, digits, and special characters.

---

## 📦 Features

- Secure random password generation using `secrets`
- Customizable password length (minimum 8 characters)
- Clean CLI interface with `argparse`
- Easy to extend or integrate into other tools

---

## 🛠️ Requirements

- Python 3.6 or higher (uses `secrets`, `argparse`, `strings`, which are built-in)

---

## 🚀 Usage

```bash
# Basic usage (default 12 characters)
python3 main.py

# Custom length (e.g., 16 characters)
python3 main.py --length 16

