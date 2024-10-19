
class TranslateNotFoundError(Exception):
    pass
class trstr:
    lg = "En"
    def __init__(self,trs:dict={"En":"Hello","Ru":"Привет"}):
        if type(trs) != dict:
            raise ValueError("Trs must be type dict!")
        self.trs = trs
    def __str__(self):
        try:
            return self.trs[trstr.lg]
        except:
            TranslateNotFoundError("Translate not found in dict translations! ")

            
