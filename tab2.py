from PyQt5 import QtWidgets

class Tab2Action():
    def __init__(self):
        self.numberOfPage = 0
        self.amountOfPossibleGroups = 0

    def changeLabelActualPage(self):
        if(self.amountOfPossibleGroups == 0):
            self.label_38.setText("Сторінка 1 з 1")
        else:
            self.label_38.setText("Сторінка " + str(self.numberOfPage + 1) + " з " + str(self.amountOfPossibleGroups))

    def takeDataTab2(self):
        result1_from_comboBox = self.comboBox_3.currentText()
        result2_from_comboBox_2 = self.comboBox_4.currentText()
        result1_from_checkBox = self.checkBox_5.checkState()
        result2_from_checkBox_2 = self.checkBox_7.checkState()
        result1_from_checkBox_3 = self.checkBox_6.checkState()
        result2_from_checkBox_4 = self.checkBox_8.checkState()
        return result1_from_comboBox, result2_from_comboBox_2, result1_from_checkBox, result2_from_checkBox_2, result1_from_checkBox_3, result2_from_checkBox_4

    def actionTab2(self):
        bloodType1, bloodType2, rhesus1, rhesus2, heterozygosity1, heterozygosity2 = self.takeDataTab2()
        bloodType1, bloodType2, rhesus1, rhesus2 = self.algorithmTab2(bloodType1, bloodType2, rhesus1, rhesus2, heterozygosity1, heterozygosity2)
        
        possibleGenesFromMother = self.findCoincidence(bloodType1, bloodType2)
        rhesusResult = self.findRhesusOfParent(rhesus1, rhesus2)
        rhesusResultRawView, rhesus2ResultRawView= self.findRhesusOfParentRawView(rhesus1, rhesus2)

        if(possibleGenesFromMother != [] and rhesusResult != ""):
            groupResult = self.substituteGameteForGroups(possibleGenesFromMother)
            genotypResultRawView = self.convertGroupsToGenotyp(groupResult)
            self.amountOfPossibleGroups = len(genotypResultRawView)
            self.printTheResult(groupResult, rhesusResult)

            massive1, masyk1 = self.calcGenotypTab2(bloodType1, rhesus2ResultRawView)
            massive2, masyk2 = self.calcGenotypTab2(genotypResultRawView[self.numberOfPage], rhesusResultRawView)
            self.changeLabelActualPage()
            self.updateTableTab2(massive1, massive2, masyk1, masyk2)
        else:
            self.amountOfPossibleGroups = 0
            self.changeLabelActualPage()
            self.clearTable()
            self.caseOfIncompatibleGroupsOrRhesuses()
        
    def goBackPage(self):
        if(self.numberOfPage - 1 >= 0):
            self.numberOfPage = self.numberOfPage - 1
        self.actionTab2()
    
    def goNextPage(self):
        if(self.numberOfPage + 1 < self.amountOfPossibleGroups):
            self.numberOfPage = self.numberOfPage + 1
        self.actionTab2()

    def calcGenotypTab2(self, word, word1):
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

    def updateTableTab2(self, mass1, mass2, masyk1, masyk2):
        for i in range(4):
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText(mass1[i])
        for j in range(4):
            item = self.tableWidget_3.horizontalHeaderItem(j)
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
                self.tableWidget_3.setItem(g, j, QtWidgets.QTableWidgetItem(masyk1[counter1] + masyk2[counter2] + masyk1[2 + counter12] + masyk2[2 + counter22]))
                counter2 = counter22 = 0
            counter12 = 0

    def clearTable(self):
        for i in range(4):
            for j in range(4):
                self.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(""))
            item = self.tableWidget_3.verticalHeaderItem(i)
            item.setText("")
            item = self.tableWidget_3.horizontalHeaderItem(i)
            item.setText("")

    def algorithmTab2(self, bloodType1, bloodType2, rhesus1, rhesus2, heterozygosity1, heterozygosity2):
        if (heterozygosity1 == 0):
            switcher = {
                "I" : "IoIo",
                "II" : "IaIa",
                "III" : "IbIb",
                "IV" : "IaIb"
                }
        else:
            switcher = {
                "II" : "IaIo",
                "III" : "IbIo"
                }
        bloodType1 = switcher.get(bloodType1, "Error")
        if (heterozygosity2 == 0):
            switcher = {
                "I" : "IoIo",
                "II" : "IaIa",
                "III" : "IbIb",
                "IV" : "IaIb"
                }
        else:
            switcher = {
                "II" : "IaIo",
                "III" : "IbIo"
                }
        bloodType2 = switcher.get(bloodType2, "Error")
        switcher1 = {
            0 : "r",
            2 : "R"
            }
        rhesus1 = switcher1.get(rhesus1, "Error")
        rhesus2 = switcher1.get(rhesus2, "Error")
        return bloodType1, bloodType2, rhesus1, rhesus2

    def findRhesusOfParent(self, rhesus1, rhesus2):
        if rhesus1 == "R" and rhesus2 == "r":
            rhesusOfParent = ""
        elif rhesus2 == "R" and rhesus1 == "r":
            rhesusOfParent = "Позитивний резус" # ["R"]
        elif rhesus2 == "R":
            rhesusOfParent = "Як позитивний, так і негативний" # ["r", "R"]
        elif rhesus2 == "r":
            rhesusOfParent =  "Негативний резус" # ["r"]
        return rhesusOfParent

    def findRhesusOfParentRawView(self, rhesus1, rhesus2):
        if rhesus1 == "R" and rhesus2 == "r":
            rhesusOfParentRawView = ""
            rhesusOfSecondParentRawView = ""
        elif rhesus2 == "R" and rhesus1 == "r":
            rhesusOfParentRawView = "RR" # ["R"]
            rhesusOfSecondParentRawView = "rr"
        elif rhesus2 == "R":
            rhesusOfParentRawView = "Rr" # ["r", "R"]
            rhesusOfSecondParentRawView = "Rr"
        elif rhesus2 == "r":
            rhesusOfParentRawView = "rr" # ["r"]
            rhesusOfSecondParentRawView = "rr"
        return rhesusOfParentRawView, rhesusOfSecondParentRawView

    def findCoincidence(self, bloodType1, bloodType2):
        arrParentGenotyp = []
        # Add first gamete to array
        arrParentGenotyp.append(bloodType1[:2])
        # If second gamete is different - add its to array
        if(bloodType1[:2] != bloodType1[2:]):
            arrParentGenotyp.append(bloodType1[2:])
        print(bloodType1, bloodType2)
        # Find equal gametes
        possibleGenesFromMother = []
        for i in arrParentGenotyp:
            if(i == bloodType2[:2]):
                possibleGenesFromMother.append(bloodType2[2:])
            elif(i == bloodType2[2:]):
                possibleGenesFromMother.append(bloodType2[:2])
        return possibleGenesFromMother

    def caseOfIncompatibleGroupsOrRhesuses(self):
        self.label_27.setText("Введені групи чи резуси не можуть бути у одного з батьків та дитини")
        return 0

    def substituteGameteForGroups(self, possibleGenesFromMother):
        possibleGroupsFromMother = []
        swiper = dict(
            Io = ['I, гомозиготний', 'II, гетерозиготний', 'III, гетерозиготний'],
            Ia = ['II, гомозиготний', 'IV, гетерозиготний'],
            Ib = ['III, гомозиготний', 'IV, гетерозиготний']
        )
        possibleGroupsFromMother.append(swiper[possibleGenesFromMother[0]])
        if(len(possibleGenesFromMother) == 2):
            possibleGroupsFromMother.append(swiper[possibleGenesFromMother[1]])
            possibleGroupsMerger = list(set(possibleGroupsFromMother[0] + possibleGroupsFromMother[1]))
            return possibleGroupsMerger
        return possibleGroupsFromMother[0]

    def convertGroupsToGenotyp(self, groupsArray):
        switcher = {
                "I, гомозиготний" : "IoIo",
                "II, гомозиготний" : "IaIa",
                "III, гомозиготний" : "IbIb",
                "IV, гетерозиготний" : "IaIb",
                "II, гетерозиготний" : "IaIo",
                "III, гетерозиготний" : "IbIo"
                }
        counter = 0
        for i in groupsArray:
            groupsArray[counter] = switcher.get(i, "Error")
            counter += 1
        return groupsArray
    
    # write results into lables
    def printTheResult(self, groupData, rhesusData):
        # groups
        self.label_27.setText(str(groupData[0]))
        if(len(groupData) > 1):
            self.label_28.setText(str(groupData[1]))
        if(len(groupData) > 2):
            self.label_29.setText(str(groupData[2]))
        if(len(groupData) > 3):
            self.label_26.setText(str(groupData[3]))
        if(len(groupData) > 4):
            self.label_37.setText(str(groupData[4]))

        # rhesus
        self.label_36.setText(rhesusData)

    # clean the output labels
    def clearLabelsTab2(self):
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_29.setText("")
        self.label_26.setText("")
        self.label_37.setText("")
        self.label_36.setText("")
