from PyQt5 import QtWidgets

class Tab3Action():

    numberOfChosenFathersGroup = 0
    amountOfFathersGroups = 0
    numberOfChosenMothersGroup = 0
    amountOfMothersGroups = 0

    def clearGlobalVarTab3(self):
        self.numberOfChosenFathersGroup = 0
        self.amountOfFathersGroups = 0
        self.numberOfChosenMothersGroup = 0
        self.amountOfMothersGroups = 0

    def goUpFather(self):
        self.actionTab3()
        if(self.numberOfChosenFathersGroup - 1 >= 0):
            self.numberOfChosenFathersGroup = self.numberOfChosenFathersGroup - 1
        print(self.numberOfChosenFathersGroup)
        self.actionTab3()

    def goDownFather(self):
        if(self.numberOfChosenFathersGroup + 1 < self.amountOfFathersGroups):
            self.numberOfChosenFathersGroup = self.numberOfChosenFathersGroup + 1
        print(self.numberOfChosenFathersGroup)
        self.actionTab3()

    def goUpMother(self):
        if(self.numberOfChosenMothersGroup - 1 >= 0):
            self.numberOfChosenMothersGroup = self.numberOfChosenMothersGroup - 1
        self.actionTab3()

    def goDownMother(self):
        if(self.numberOfChosenMothersGroup + 1 < self.amountOfMothersGroups):
            self.numberOfChosenMothersGroup = self.numberOfChosenMothersGroup + 1
        self.actionTab3()

    def resetToDefaultGroupsLabels(self):
        labelObjects = [self.label_50, self.label_51, self.label_52, self.label_53, self.label_54, self.label_55]
        for i in labelObjects:
            i.setStyleSheet("")

    def setStyleToChosenGroup(self):
        labelObjects1 = [self.label_50, self.label_51, self.label_52]
        labelObjects1[self.numberOfChosenFathersGroup].setStyleSheet("padding: 0px 10px; color: grey;")
        labelObjects2 = [self.label_53, self.label_54, self.label_55]
        labelObjects2[self.numberOfChosenMothersGroup].setStyleSheet("padding: 0px 10px; color: grey;")
    
    def actionTab3(self):
        self.resetToDefaultGroupsLabels()
        bloodType, rhesus, heterozygosity = self.takeDataTab3()
        gametes, rhesus = self.algorithmTab3(bloodType, rhesus, heterozygosity)
        fathersGroups = self.substituteGameteForGroupsTab3(gametes[0], "man")
        mothersGroups = self.substituteGameteForGroupsTab3(gametes[1], "woman")

        fathersRhesus, mothersRhesus, rhesusForOutput = self.findRhesusTab3(rhesus)

        self.clearLabelsTab3()
        self.printTheResultTab3(fathersGroups, mothersGroups, rhesusForOutput)

        fathersGroupsRawView = self.convertGroupsToRawViewTab3(fathersGroups)
        mothersGroupsRawView = self.convertGroupsToRawViewTab3(mothersGroups)

        self.amountOfFathersGroups = len(fathersGroups)
        self.amountOfMothersGroups = len(mothersGroups)

        massive1, masyk1 = self.calcGenotypTab3(fathersGroupsRawView[self.numberOfChosenFathersGroup], fathersRhesus) #
        massive2, masyk2 = self.calcGenotypTab3(mothersGroupsRawView[self.numberOfChosenMothersGroup], mothersRhesus) #

        self.updateTableTab3(massive1, massive2, masyk1, masyk2)

        self.setStyleToChosenGroup()

    def takeDataTab3(self):
        result_from_comboBox_5 = self.comboBox_5.currentText()
        result_from_checkBox_9 = self.checkBox_9.checkState()
        result_from_checkBox_10 = self.checkBox_10.checkState()
        return result_from_comboBox_5, result_from_checkBox_9,  result_from_checkBox_10

    def algorithmTab3(self, bloodType, rhesus, heterozygosity):
        if (heterozygosity == 0):
            switcher = {
                "I" : ["Io", "Io"],
                "II" : ["Ia", "Ia"],
                "III" : ["Ib", "Ib"],
                "IV" : ["Ia", "Ib"]
                }
        else:
            switcher = {
                "II" : ["Ia", "Io"],
                "III" : ["Ib", "Io"]
                }
        bloodType = switcher.get(bloodType, "Error")
        switcher1 = {
            0 : "r",
            2 : "R"
            }
        rhesus = switcher1.get(rhesus, "Error")
        return bloodType, rhesus
    
    def substituteGameteForGroupsTab3(self, gamete, sex):
        if(sex == "man"):
            swiper = dict(
                Io = ['I, гомозиготний', 'II, гетерозиготний', 'III, гетерозиготний'],
                Ia = ['II, гомозиготний', 'IV, гетерозиготний'],
                Ib = ['III, гомозиготний', 'IV, гетерозиготний']
            )
        else:
            swiper = dict(
                Io = ['I, гомозиготна', 'II, гетерозиготна', 'III, гетерозиготна'],
                Ia = ['II, гомозиготна', 'IV, гетерозиготна'],
                Ib = ['III, гомозиготна', 'IV, гетерозиготна']
            )
        print(gamete)
        gamete = swiper[gamete]
        return gamete

    def convertGroupsToRawViewTab3(self, groups):
        groupsRawView =[]
        switcher = {
                "I, гомозиготна" : "IoIo",
                "II, гетерозиготна" : "IaIo",
                "III, гетерозиготна" : "IbIo",
                "II, гомозиготна" : "IaIa",
                "IV, гетерозиготна" : "IaIb",
                "III, гомозиготна" : "IbIb",
                "I, гомозиготний" : "IoIo",
                "II, гетерозиготний" : "IaIo",
                "III, гетерозиготний" : "IbIo",
                "II, гомозиготний" : "IaIa",
                "IV, гетерозиготний" : "IaIb",
                "III, гомозиготний" : "IbIb"
                }
        for i in groups:
            groupsRawView.append(switcher.get(i, "Error"))
        return groupsRawView

    def findRhesusTab3(self, rhesus):
        if(rhesus == "r"):
            fathersRhesus = "rr"
            mothersRhesus = "rr"
            rhesusForOutput = "У батьків негативний резус"
        else:
            fathersRhesus = "Rr"
            mothersRhesus = "rr"
            rhesusForOutput = "У одного з батьків або у обох батьків позитивний резус"
        return fathersRhesus, mothersRhesus, rhesusForOutput

    def calcGenotypTab3(self, word, word1):
        arrayList = []
        for i in word:
            arrayList.append(i)
        geno1 = arrayList[0] + arrayList[1]
        geno2 = arrayList[2] + arrayList[3]
        arrayList1 = []
        for j in word1:
            arrayList1.append(j)
        geno1_1 = arrayList1[0]
        geno2_1 = arrayList1[1]
        return [geno1_1 + geno1, geno1_1 + geno2, geno2_1 + geno1, geno2_1 + geno2], [geno1_1, geno2_1, geno1, geno2]

    def updateTableTab3(self, mass1, mass2, masyk1, masyk2):
        for i in range(4):
            item = self.tableWidget_4.verticalHeaderItem(i)
            item.setText(mass1[i])
        for j in range(4):
            item = self.tableWidget_4.horizontalHeaderItem(j)
            item.setText(mass2[j])
            counter1 = counter2 = counter12 = counter22 = 0
        for g in range(4):
            if g > 1:
                counter1 = 1
            if g == 1 or g == 3:
                counter12 = 1
            for j in range(4):
                if j > 1:
                    counter2 = 1
                if j == 1 or j == 3:
                    counter22 = 1
                self.tableWidget_4.setItem(g, j, QtWidgets.QTableWidgetItem(masyk1[counter1] + masyk2[counter2] + masyk1[2 + counter12] + masyk2[2 + counter22]))
                counter2 = counter22 = 0
            counter12 = 0
        
    def printTheResultTab3(self, fatherGroups, motherGroups, rhesus):
        self.label_50.setText(str(fatherGroups[0]))
        if(len(fatherGroups) > 1):
            self.label_51.setText(str(fatherGroups[1]))
        if(len(fatherGroups) > 2):
            self.label_52.setText(str(fatherGroups[2]))

        self.label_53.setText(str(motherGroups[0]))
        if(len(motherGroups) > 1):
            self.label_54.setText(str(motherGroups[1]))
        if(len(motherGroups) > 2):
            self.label_55.setText(str(motherGroups[2]))

        self.label_56.setText(rhesus)

    # clean the output labels
    def clearLabelsTab3(self):
        self.label_50.setText("")
        self.label_51.setText("")
        self.label_52.setText("")
        self.label_53.setText("")
        self.label_54.setText("")
        self.label_55.setText("")
        self.label_56.setText("")