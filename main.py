import csv
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog

from About import Ui_About
from Definitions import Ui_Definitions
from MainWindow import Ui_MainWindow
from Settings import Ui_SettingsWindow

def_button_is_clicked = None
term_button_is_clicked = None
def_name_number = None
term_name_number = None
set_name = ""
correct_counter = 0
data = None


# Open Settings on Settings Button press
def settings_open():
    settings.show()
    pass


# Open About on About Button press
def about_open():
    about.show()
    pass


# Set selection on Open Set Button press
def definitions_open():
    global set_name
    set_name = str(QFileDialog.getExistingDirectory(window, "Select Directory", "sets"))  # File Dialog for Set Select
    definitions_innit()  # Call Innit Function


# Innit on Set Select/Refresh on new Round for Definitions
def definitions_innit():
    global set_name  # Selected Set from definitions_open()
    global data
    data = csv_to_lists(set_name + "/def1.csv")  # Call CSV function (see below)
    items = list(range(0, len(data)))  # Index of all Elements from data
    shuffle = [0, 1, 2]  # Shuffle-List for 2nd assignment
    random.shuffle(items)  # Shuffling both lists for randomness
    random.shuffle(shuffle)

# Assign first 3 Items(Definitions) from Index to buttons
    def1 = items[0]
    def2 = items[1]
    def3 = items[2]

# Assign the 3 corresponding shuffled Items(Terms)
    term1 = items[shuffle[0]]
    term2 = items[shuffle[1]]
    term3 = items[shuffle[2]]

    definitions_ui.def1_button.setText(data[def1][0])  # Assigning chosen text to Buttons
    definitions_ui.def1_button.setToolTip(str(def1))  # Assigning Index as Tooltip for later use
    definitions_ui.def1_button.setVisible(True)  # In case of refresh
    definitions_ui.def1_button.setChecked(False)  # In case of refresh
    definitions_ui.term1_button.setText(data[term1][1])
    definitions_ui.term1_button.setToolTip(str(term1))
    definitions_ui.term1_button.setVisible(True)
    definitions_ui.term1_button.setChecked(False)
    definitions_ui.def2_button.setText(data[def2][0])
    definitions_ui.def2_button.setToolTip(str(def2))
    definitions_ui.def2_button.setVisible(True)
    definitions_ui.def2_button.setChecked(False)
    definitions_ui.term2_button.setText(data[term2][1])
    definitions_ui.term2_button.setToolTip(str(term2))
    definitions_ui.term2_button.setVisible(True)
    definitions_ui.term2_button.setChecked(False)
    definitions_ui.def3_button.setText(data[def3][0])
    definitions_ui.def3_button.setToolTip(str(def3))
    definitions_ui.def3_button.setVisible(True)
    definitions_ui.def3_button.setChecked(False)
    definitions_ui.term3_button.setText(data[term3][1])
    definitions_ui.term3_button.setToolTip(str(term3))
    definitions_ui.term3_button.setVisible(True)
    definitions_ui.term3_button.setChecked(False)

    definitions.show()  # Show Window
    pass


# Checks on Button clicked (see below)
def def_button_clicked(index, number):
    global term_button_is_clicked
    global def_button_is_clicked
    global term_name_number
    global def_name_number
    global correct_counter
    def_button_is_clicked = index
    def_name_number = number

    if term_button_is_clicked is not None:
        if term_button_is_clicked == def_button_is_clicked:
            term_button_is_clicked = None
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setVisible(False)
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setVisible(False)
            correct_counter = correct_counter + 1
            if correct_counter == 3:
                definitions_innit()
                correct_counter = 0
        else:
            term_button_is_clicked = None
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setChecked(False)
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setChecked(False)
    pass


def term_button_clicked(index, number):
    global term_button_is_clicked  # Set-Index of last pressed Term-Button parsed as ToolTip
    global def_button_is_clicked  # Set-Index of last pressed Def-Button parsed as ToolTip
    global term_name_number  # Number in Term-Button Name
    global def_name_number  # Number in Def-Button Name
    global correct_counter  # Counter for refresh trigger
    term_button_is_clicked = index  # Assign parsed Index to var
    term_name_number = number  # Assign Name Number

    if def_button_is_clicked is not None:  # If this is the second click
        if term_button_is_clicked == def_button_is_clicked:  # If both buttons have the same Index (are corresponding)
            term_button_is_clicked = None  # Reset Index Vars
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setVisible(False)  # Hiding Buttons
            # for User Feedback
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setVisible(False)
            correct_counter = correct_counter + 1  # Counter Count-Up
            if correct_counter == 3:  # Check if time for refresh
                definitions_innit()  # Run Refresh function
                correct_counter = 0  # Reset counter
        else:  # If not corresponding
            term_button_is_clicked = None  # Reset so no false checks happen
            def_button_is_clicked = None
            getattr(definitions_ui, "term" + str(term_name_number) + "_button").setChecked(False)  # QOL reset
            getattr(definitions_ui, "def" + str(def_name_number) + "_button").setChecked(False)
    pass


def csv_to_lists(file_path):
    with open(file_path, newline='', encoding="utf-8") as csv_file:  # magic library things (encoding for umlaute)
        reader = csv.reader(csv_file)
        rows = list(reader)
    return rows


app = QApplication([])
window = QMainWindow()
settings = QWidget()
about = QWidget()
definitions = QWidget()

# Landingpage Setup
landingpage_ui = Ui_MainWindow()
landingpage_ui.setupUi(window)
# Settings Setup
settings_ui = Ui_SettingsWindow()
settings_ui.setupUi(settings)
# About Setup
about_ui = Ui_About()
about_ui.setupUi(about)
# Definitions Setup
definitions_ui = Ui_Definitions()
definitions_ui.setupUi(definitions)

# Landingpage Connects
landingpage_ui.SettingsButton.clicked.connect(settings_open)
landingpage_ui.OpenButton.clicked.connect(definitions_open)  # Replace with Set Select
# Settings Connects
settings_ui.about_button.clicked.connect(about_open)
# Definitions Connects
definitions_ui.def1_button.clicked.connect(lambda: def_button_clicked(definitions_ui.def1_button.toolTip(), 1))
definitions_ui.def2_button.clicked.connect(lambda: def_button_clicked(definitions_ui.def2_button.toolTip(), 2))
definitions_ui.def3_button.clicked.connect(lambda: def_button_clicked(definitions_ui.def3_button.toolTip(), 3))
definitions_ui.term1_button.clicked.connect(lambda: term_button_clicked(definitions_ui.term1_button.toolTip(), 1))
definitions_ui.term2_button.clicked.connect(lambda: term_button_clicked(definitions_ui.term2_button.toolTip(), 2))
definitions_ui.term3_button.clicked.connect(lambda: term_button_clicked(definitions_ui.term3_button.toolTip(), 3))

window.show()
app.exec()
