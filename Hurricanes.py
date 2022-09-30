from sys import platform
import os
#######################################
# Insert other modules to import here
#######################################

import pandas as pd
import numpy as np

def clear_console():
    if os.name in ('nt','dos'):
        command = 'cls'
    else:
        command = 'clear'

    os.system(command)

def load_file_to_df(filename):
    df = pd.read_excel(filename, sheet_name="RawData")
    #Year, Month, StatesAffectedWithCategory, HighestCategory, CentralPressure_mb, MaxWind_kt, Name

    df.rename( columns={"Year": "ReportedYear",
                        "Month": "ReportedMonth"}, inplace=True)

    return df 

def main():

    currentDirectory = os.getcwd()

    if platform == "darwin":
        os_platform = "Mac"
        excelFile = currentDirectory + "/HurricaneData.xlsx"
        os.chdir(currentDirectory)
        clear_console()
    else:
        os_platform = "Windows"
        excelFile = currentDirectory + "\\HurricaneData.xlsx"
        os.chdir(currentDirectory)
        clear_console()

    df_hurricane = load_file_to_df(excelFile)


################# Main Processing Section ##############################

if __name__ == '__main__':
    main()
