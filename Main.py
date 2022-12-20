import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

# Define a list of people
people = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

# Choose two random people from the list
person1 = random.choice(people)
person2 = random.choice(people)

# Make sure the same person is not paired with themselves
while person1 == person2:
    person2 = random.choice(people)

# Create a QApplication object
app = QApplication([])

# Create a QWidget object
window = QWidget()

# Set the window title
window.setWindowTitle('Random Pairing')

# Create a QLabel to display the pairing
label = QLabel(f'{person1} has been paired with {person2}')

# Set the label as the central widget of the window
window.setCentralWidget(label)

# Show the window
window.show()

# Run the application loop
app.exec_()
