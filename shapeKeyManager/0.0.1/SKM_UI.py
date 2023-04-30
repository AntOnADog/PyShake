import sys
import QApplication

app = QApplication([])

window =  QWidget()
window.setWindowTitle("ShapeKey Manager")
window.setGeometry(100,100, 280, 80)
helloMsg = QLabel("<h1>This window stuff is kinda interesting</h1>", parent=window)
helloMsg.move(60,15)