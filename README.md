# 🔐 Password Strength Analyzer & Breach Checker

A professional **command-line tool** that evaluates password strength using entropy analysis and checks whether the password has been leaked in data breaches using the **Have I Been Pwned API**.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features
- Real-time password strength scoring
- Entropy calculation (bits)
- Crack time estimation
- Detection of common weak patterns
- Secure breach checking using **k-Anonymity** (only first 5 characters of SHA-1 hash are sent)
- Beautiful terminal interface using Rich

## 🛠 Tech Stack
- Python 3
- `rich` – Terminal UI
- `requests` – API communication
- Have I Been Pwned API

## How It Works
The tool uses the **k-Anonymity** model so your full password is never transmitted over the internet — only the first 5 characters of its SHA-1 hash are sent.

## Installation & Usage

```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
cd password-strength-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py <password>
