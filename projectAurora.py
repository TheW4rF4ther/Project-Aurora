import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel, QDialog, QLineEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
import requests
import openai

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.api_key = None  # Initialize API key storage
        self.title = 'Chat with GPT-4'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setStyleSheet("QWidget { background-color: maroon; }")

        # Font setup
        terminal_font = QFont("Terminal", 10)
        
        layout = QVBoxLayout()
        self.label = QLabel('GPT-4 Response:')
        self.label.setStyleSheet("color: white;")
        layout.addWidget(self.label)

        self.answerEdit = QTextEdit(self)
        self.answerEdit.setFont(terminal_font)
        self.answerEdit.setStyleSheet("background-color: black; color: white;")
        self.answerEdit.setReadOnly(True)
        self.answerEdit.setFixedSize(QSize(480, 320))
        layout.addWidget(self.answerEdit)

        self.questionEdit = QTextEdit(self)
        self.questionEdit.setFont(terminal_font)
        self.questionEdit.setStyleSheet("QTextEdit { background-color: black; color: white; }")
        self.questionEdit.setFixedSize(QSize(480, 40))
        layout.addWidget(self.questionEdit)

        button = QPushButton('Ask GPT-4', self)
        button.setStyleSheet("QPushButton { background-color: black; color: #39FF14; }"
                             "QPushButton:hover { background-color: grey; }"
                             "QPushButton:pressed { margin-top: 5px; margin-left: 5px; }")
        button.clicked.connect(self.on_click)
        layout.addWidget(button)

        self.apiKeyButton = QPushButton('API_KEY', self)
        self.apiKeyButton.setStyleSheet("QPushButton { background-color: black; color: white; }")
        self.apiKeyButton.clicked.connect(self.openApiKeyDialog)
        layout.addWidget(self.apiKeyButton)

        self.setLayout(layout)

    def on_click(self):
        if not self.api_key:
            print("API key is not set.")
            return
        question = self.questionEdit.toPlainText()
        response = requests.post('http://127.0.0.1:5000/ask', json={'question': question})
        answer = response.json()
        current_text = self.answerEdit.toPlainText()
        new_text = f"David - {answer}"
        if current_text:
            new_text = f"\n{new_text}"
        self.answerEdit.setText(current_text + new_text)
        self.questionEdit.clear()

    def openApiKeyDialog(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle('Enter API Key')
        layout = QVBoxLayout()

        self.apiKeyEdit = QLineEdit(self.dialog)
        self.apiKeyEdit.setPlaceholderText("Enter your OpenAI API key here...")
        layout.addWidget(self.apiKeyEdit)

        submitButton = QPushButton('Submit', self.dialog)
        submitButton.clicked.connect(self.saveApiKey)
        layout.addWidget(submitButton)

        self.dialog.setLayout(layout)
        self.dialog.exec_()

    def saveApiKey(self):
        self.api_key = self.apiKeyEdit.text()
        openai.api_key = self.api_key
        self.dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())

    def on_click(self):
        question = self.questionEdit.toPlainText()
        response = requests.post('http://127.0.0.1:5000/ask', json={'question': question})
        answer = response.json()
        current_text = self.answerEdit.toPlainText()
        new_text = f"Aurora - {answer}"
        if current_text:
            new_text = f"\n{new_text}"
        self.answerEdit.setText(current_text + new_text)
        self.questionEdit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
