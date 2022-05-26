class DirFunc:

    def __init__(self):
        self.misFunciones = {}
    
    def addFunc(self, newFunc, newType):
        self.misFunciones[newFunc] = {
            "tipo" : newType,
            "startDir" : "",
            "numParamsInt" : 0,
            "numParamsFl" : 0,
            "numLocalsInt" : 0,
            "numLocalsFl" : 0,
            "numTempsInt" : 0,
            "numTempsFl" : 0,
            "numTempsBl" : 0,
            "params" : [],
            "vars" : {}
        }
    
    def getFuncType(self, currFunc):
        return self.misFunciones[currFunc][0]
    
    def addVar(self, currFunc, currVars):
        self.misFunciones[currFunc]["vars"] = currVars
    
    def addParams(self, currFunc, currParams):
        self.misFunciones[currFunc]["params"] = currParams
    
    def getParam(self, currFunc, currIdx):
        if currIdx >= len(self.misFunciones[currFunc]["params"]):
            return -1
        return self.misFunciones[currFunc]["params"][currIdx]
    
    def getVarMem(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][1]
    
    def getIDType(self, currFunc, currID):
        return self.misFunciones[currFunc]["vars"][currID][0]
    
    def getVars(self, currFunc):
        return self.misFunciones[currFunc]["vars"]
    
    def setStart(self, currFunc, start):
        self.misFunciones[currFunc]["startDir"] = start
    
    def getStart(self, currFunc):
        return self.misFunciones[currFunc]["startDir"]
    
    def setNumParams(self, currFunc):
        for key in self.misFunciones[currFunc]["params"]:
            if key == "INT":
                self.misFunciones[currFunc]["numParamsInt"] += 1
            elif key == "FLOAT":
                self.misFunciones[currFunc]["numParamsFl"] += 1
    
    def setNumVars(self, currFunc):
        for key in self.misFunciones[currFunc]["vars"]:
            if self.misFunciones[currFunc]["vars"][key][0] == "INT":
                self.misFunciones[currFunc]["numLocalsInt"] += 1
            elif self.misFunciones[currFunc]["vars"][key][0] == "FLOAT":
                self.misFunciones[currFunc]["numLocalsFl"] += 1

    def setNumTemps(self, currFunc, currType):
        if currType == "INT":
            self.misFunciones[currFunc]["numTempsInt"] += 1
        elif currType == "FLOAT":
            self.misFunciones[currFunc]["numTempsFl"] += 1
        elif currType == "BOOL":
            self.misFunciones[currFunc]["numTempsBl"] += 1

    def pr(self):
        for key in self.misFunciones:
            print("----------- FUNCION", key, "-----------")
            print("Tipo:", self.misFunciones[key]["tipo"])
            print("Direccion de inicio:", self.misFunciones[key]["startDir"])
            print("Numero de parametros enteras:", self.misFunciones[key]["numParamsInt"])
            print("Numero de parametros flotantes:", self.misFunciones[key]["numParamsFl"])
            print("Numero de variables locales enteras:", self.misFunciones[key]["numLocalsInt"])
            print("Numero de variables locales flotantes:", self.misFunciones[key]["numLocalsFl"])
            print("Numero de temporales enteras:", self.misFunciones[key]["numTempsInt"])
            print("Numero de temporales flotantes:", self.misFunciones[key]["numTempsFl"])
            print("Numero de temporales booleanas:", self.misFunciones[key]["numTempsBl"])
            print("Parametros:", self.misFunciones[key]["params"])
            print("Variables:", self.misFunciones[key]["vars"])