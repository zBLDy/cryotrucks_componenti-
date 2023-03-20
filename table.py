import pandas as pd
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget

# Only needed for access to command line arguments
import sys

# Pass in sys.argv to allow command line arguments for your application.
# If you know you won't use command line arguments QApplication([]) works too.

app = QApplication(sys.argv)

# Create a Qt Widget, wich will be our window.
window = QWidget()
window.show()

# Start the event loop
app.exec_()
