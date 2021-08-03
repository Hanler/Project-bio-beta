def checkCondition(input, check):
    valueInComboBox = input.currentText()
    if (valueInComboBox == "I" or valueInComboBox == "IV"):
        check.setEnabled(False)
        check.setChecked(False)
    else:
        check.setEnabled(True)