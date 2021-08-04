from PyQt5 import QtWidgets

class Tab3Action():
    def actionTab3(self):
        bloodType, rhesus, heterozygosity = self.takeDataTab3()
        gametes, rhesus = self.algorithmTab3(bloodType, rhesus, heterozygosity)
        fathersGroups = self.substituteGameteForGroupsTab3(gametes[0], "man")
        mothersGroups = self.substituteGameteForGroupsTab3(gametes[1], "woman")
        print("fathersGroups")
        print(fathersGroups)
        print("mothersGroups")
        print(mothersGroups)

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
