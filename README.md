# Python Keylogger

![Python](https://img.shields.io/badge/python-3.x-blue.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A simple yet effective keylogger built in Python. This tool is designed to capture and record keystrokes on the machine it's running on.

## ⚠️ Disclaimer

This tool is intended for educational and research purposes only. The author is not responsible for any misuse or damage caused by this program. **Using this software on a computer without the owner's explicit permission is illegal.** Please use this tool responsibly and ethically.

## ✨ Features

* **Keystroke Logging:** Captures all keys pressed on the keyboard.
* **Log File:** Saves the recorded keystrokes to a local file (`keylog.txt`).
* **Cross-Platform:** Should work on Windows, macOS, and Linux.
* **Simple & Lightweight:** Minimal code and dependencies.

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/jitendhar27/keylogger.git](https://github.com/jitendhar27/keylogger.git)
    cd keylogger
    ```

2.  **Install the required dependencies:**
    This project uses the `pynput` library to listen to keyboard events.
    ```sh
    pip install pynput
    ```

### Usage

To start the keylogger, simply run the Python script:

```sh
python keylogger.py
```

Once the script is running, it will start capturing all keystrokes. The logs will be saved in a file named `keylog.txt` in the same directory. To stop the keylogger, you can press `Ctrl+C` in the terminal where the script is running.

## ⚙️ How It Works

The keylogger uses the `pynput` library, a powerful tool for controlling and monitoring input devices.

1.  **Listener:** The script sets up a `Listener` from `pynput.keyboard`.
2.  **Event Handling:** The `on_press` function is called every time a key is pressed.
3.  **Logging:** The pressed key is converted to a string and appended to the `keylog.txt` file. Special keys (like Shift, Ctrl, Space) are also handled and recorded appropriately.

## 📝 To-Do / Future Enhancements

* [ ] Run in stealth/background mode.
* [ ] Send logs to a remote server or email address.
* [ ] Add screenshot capturing functionality.
* [ ] Encrypt the log file for security.
* [ ] Add a feature to clear the log file periodically.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/jitendhar27/keylogger/issues).

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---
*Made with ❤️ for educational purposes.*
