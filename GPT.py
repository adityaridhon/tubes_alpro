import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel('Select an option:', self)

        # Create a QComboBox (dropdown)
        dropdown = QComboBox(self)
        dropdown.addItem('Option 1')
        dropdown.addItem('Option 2')
        dropdown.addItem('Option 3')

        # Connect the dropdown to a function
        dropdown.currentIndexChanged.connect(self.dropdownChanged)

        layout.addWidget(label)
        layout.addWidget(dropdown)

        self.setLayout(layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Dropdown Button Example')
        self.show()

    def dropdownChanged(self, index):
        # This function is called when the dropdown selection changes
        selected_option = self.sender().currentText()
        print(f'Selected option: {selected_option}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
