import inspect #CHECK DATACODE
import GUI_YT_DOWLOAD

#CONTAR FUNCIONES Y RETORNAR NUMERO
def count_functions(module):

    function_list = inspect.getmembers(module, inspect.isfunction)
    number = len(function_list)

    return number

#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster(defNumber):

    #PROJECT-DATA
    proyectName = "YT-DOWNLOAD"
    developer = "MAURO PEPA"
    proyectVersion = "1.2"

    developerCretis = "\n"+proyectName+ " - BY "+developer+" - V"+proyectVersion+"."+defNumber
    print(developerCretis)

    LongNumberStick = "-"*len(developerCretis)
    print(LongNumberStick)

def printCredits():

    #MODULES PROYECTS
    defNumber = count_functions(GUI_YT_DOWLOAD)

    printCodeMaster(str(defNumber))

if __name__ == '__main__':
    printCredits()