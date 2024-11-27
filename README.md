# 🌐 Subdomain Enumeration & Live Check Tool 🚀

Welcome to the **Subdomain Enumeration & Live Check Tool**! This tool is designed for **subdomain enumeration** and **live subdomain checking** using the powerful `Sublist3r`. It's perfect for **security researchers**, **penetration testers**, and **OSINT enthusiasts** to identify and verify live subdomains of a domain.

---

## ✨ Features

- **🔍 Subdomain Enumeration**: Efficiently gathers subdomains using `Sublist3r`.
- **✅ Live Subdomain Check**: Verifies if subdomains are live (HTTP 200 status code).
- **⚡ Multithreading Support**: Fast, concurrent subdomain checking using `ThreadPoolExecutor`.
- **🎨 User-Friendly Interface**: Color-coded terminal output for an enhanced user experience.
- **📜 Main Menu Option**: Option to exit or return to the main menu after enumeration is complete.

---

## 🚀 Requirements

To get started, ensure you have the following:

- **Python 3.x** (3.6 or higher recommended)
- **Required Dependencies**: Python packages needed for this tool.

### Install Dependencies:

```
requests==2.28.1
colorama==0.4.6
sublist3r==1.1
```
🛠️ Installation
Follow these steps to install and use the tool:

Clone the repository:
```

git clone https://github.com/4rti7t/SUBDIGGER.git
cd SUBDIGGER
```

**Install the required dependencies:**

```
pip install -r requirements.txt
```

```Make sure Sublist3r is installed (if not, you can install it via pip):```

```
pip install sublist3r
```

**🏃‍♂️ Usage**

Once everything is set up, you can start the tool with the following command:
```
python subdomain_enumeration.py
```
Enter the domain you want to check (e.g., example.com).

The tool will start enumerating subdomains and checking if they are live.
Live subdomains will be displayed in green immediately.
Once enumeration is complete, you’ll be given the option to either exit or return to the main menu.
💻 Example Output
Here’s an example of how the tool interacts with the user:

**RESULTS**:

Enter the domain (e.g., example.com): example.com
Enumerating subdomains... ◯
Enumerating subdomains... ◔
Live Subdomain Found: subdomain.example.com ✅
Enumerating subdomains... ◑
Enumerating subdomains... ◕
Live Subdomain Found: api.example.com ✅
No more live subdomains found. 🚫

**🤝 Contributing**

We welcome contributions! If you have ideas or want to improve the tool:

**Fork the repository**.
Make your changes and test thoroughly.
Submit a pull request with a detailed explanation of the changes.

**📄 License**
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 **Acknowledgements**

Sublist3r: The subdomain enumeration tool powering this project.
Colorama: Helps in adding color to the terminal output for better readability.
Python's requests library: Handles HTTP requests efficiently.

📬 **Contact**
For any questions or feedback, feel free to reach out:

Email: arti7tofficial@gmail.com
GitHub: your-github-profile
