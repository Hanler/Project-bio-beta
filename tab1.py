from PyQt5 import QtWidgets

class Tab1Action():
    def takeData(self):
        result1_from_comboBox = self.comboBox.currentText()
        result2_from_comboBox_2 = self.comboBox_2.currentText()
        result1_from_checkBox = self.checkBox.checkState()
        result2_from_checkBox_2 = self.checkBox_2.checkState()
        result1_from_checkBox_3 = self.checkBox_3.checkState()
        result2_from_checkBox_4 = self.checkBox_4.checkState()
        self.algorithm(result1_from_comboBox,result2_from_comboBox_2,result1_from_checkBox,result2_from_checkBox_2,result1_from_checkBox_3,result2_from_checkBox_4)
    
    def algorithm(self, bloodType1, bloodType2, rhesus1, rhesus2, heterozygosity1, heterozygosity2):
        if (heterozygosity1 == 0):
            switcher = {
                "I" : "IoIo",
                "II" : "IaIa",
                "III" : "IbIb",
                "IV" : "IaIb"
                }
        else:
            switcher = {
                "I" : "IoIo",
                "II" : "IaIo",
                "III" : "IbIo",
                "IV" : "IaIb"
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
                "I" : "IoIo",
                "II" : "IaIo",
                "III" : "IbIo",
                "IV" : "IaIb"
                }
        bloodType2 = switcher.get(bloodType2, "Error")
        switcher1 = {
            0 : "rr",
            2 : "Rr"
            }
        rhesus1 = switcher1.get(rhesus1, "Error")
        rhesus2 = switcher1.get(rhesus2, "Error")
        massive1, masyk1 = self.calcGenotyp(bloodType1, rhesus1)
        massive2, masyk2 = self.calcGenotyp(bloodType2, rhesus2)
        self.updateTable(massive1, massive2, masyk1, masyk2)

    def updateTable(self, mass1, mass2, masyk1, masyk2):
        for i in range(4):
            item = self.tableWidget_2.verticalHeaderItem(i)
            item.setText(mass1[i])
        for j in range(4):
            item = self.tableWidget_2.horizontalHeaderItem(j)
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
                self.tableWidget_2.setItem(g, j, QtWidgets.QTableWidgetItem(masyk1[counter1] + masyk2[counter2] + masyk1[2 + counter12] + masyk2[2 + counter22]))
                counter2 = 0
                counter22 = 0
            counter12 = 0
        self.analyzingResults(self.getFromTable())

    def getFromTable(self):
        array=[]
        for i in range(4):
            for j in range(4):
                array.append(self.tableWidget_2.item(i,j).text())
        return array

    def calcGenotyp(self, word, word1):
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

    def analyzingResults(self, array):
        arr = []
        arr1 = []
        for i in array:
            for j in i:
                arr.append(j)
        for g in range(int(len(arr)/6)):
            arr1.append(arr[6*g] + arr[(6*g) + 1])
            arr1.append(arr[(6*g) + 2] + arr[(6*g) + 3] + arr[(6*g) + 4] + arr[(6*g) + 5])
        switcherRes = {
            "RR" : "Позитивний резус",
            "Rr" : "Позитивний резус",
            "rR" : "Позитивний резус",
            "rr" : "Негативний резус",
            "IoIo" : "I група",
            "IaIo" : "II група",
            "IoIa" : "II група",
            "IaIa" : "II група",
            "IbIo" : "III група",
            "IoIb" : "III група",
            "IbIb" : "III група",
            "IaIb" : "IV група",
            "IbIa" : "IV група"
            }
        amountI = amountIn = amountII = amountIIn = amountIII = amountIIIn = amountIV = amountIVn = 0
        for i in range(len(arr1)):
            arr1[i] = switcherRes.get(arr1[i], "Error")
        for i in range(1, len(arr1)):
            if(arr1[i] == 'I група'):
                amountI += 1
                if(arr1[i-1] == 'Негативний резус'):
                    amountIn += 1
            else:
                if(arr1[i] == 'II група'):
                    amountII += 1
                    if(arr1[i-1] == 'Негативний резус'):
                        amountIIn += 1
                else:
                    if(arr1[i] == 'III група'):
                        amountIII += 1
                        if(arr1[i-1] == 'Негативний резус'):
                            amountIIIn += 1
                    else:
                        if(arr1[i] == 'IV група'):
                            amountIV += 1
                            if(arr1[i-1] == 'Негативний резус'):
                                amountIVn += 1
            i += 1
        arrayStatistic = [amountI, amountIn, amountII, amountIIn, amountIII, amountIIIn, amountIV, amountIVn]
        arrayOutput = []
        if(amountI != 0):
            arrayOutput.append("I група, негативний резус - " + str(int(amountI/(len(arr1)/2)*(amountIn/amountI)*100)) + "%") # percantage with negative R
            arrayOutput.append("I група, позитивний резус - " + str(int(amountI/(len(arr1)/2)*((amountI-amountIn)/amountI)*100)) + "%") # percantage with positive R
        else:
            arrayOutput.append("I група, негативний резус - 0%")
            arrayOutput.append("I група, позитивний резус - 0%")
        if(amountII != 0):
            arrayOutput.append("II група, негативний резус - " + str(int(amountII/(len(arr1)/2)*(amountIIn/amountII)*100)) + "%") # percantage with negative R
            arrayOutput.append("II група, позитивний резус - " + str(int(amountII/(len(arr1)/2)*((amountII-amountIIn)/amountII)*100)) + "%") # percantage with positive R
        else:
            arrayOutput.append("II група, негативний резус - 0%")
            arrayOutput.append("II група, позитивний резус - 0%")
        if(amountIII != 0):
            arrayOutput.append("III група, негативний резус - " + str(int(amountIII/(len(arr1)/2)*(amountIIIn/amountIII)*100)) + "%") # percantage with negative R
            arrayOutput.append("III група, позитивний резус - " + str(int(amountIII/(len(arr1)/2)*((amountIII-amountIIIn)/amountIII)*100)) + "%") # percantage with positive R
        else:
            arrayOutput.append("III група, негативний резус - 0%")
            arrayOutput.append("III група, позитивний резус - 0%")
        if(amountIV != 0):
            arrayOutput.append("IV група, негативний резус - " + str(int(amountIV/(len(arr1)/2)*(amountIVn/amountIV)*100)) + "%") # percantage with negative R
            arrayOutput.append("IV група, позитивний резус - " + str(int(amountIV/(len(arr1)/2)*((amountIV-amountIVn)/amountIV)*100)) + "%") # percantage with positive R
        else:
            arrayOutput.append("IV група, негативний резус - 0%")
            arrayOutput.append("IV група, позитивний резус - 0%")

        self.label_7.setText(arrayOutput[0] + "   " + arrayOutput[1])
        self.label_8.setText(arrayOutput[2] + "   " + arrayOutput[3])
        self.label_9.setText(arrayOutput[4] + "   " + arrayOutput[5])
        self.label_10.setText(arrayOutput[6] + "   " + arrayOutput[7])