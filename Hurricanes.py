from sys import platform
import os
#######################################
# Insert other modules to import here
#######################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def categorize(row):
    if row['Name'] == 0:
        return 0
    else:
        return 1

def number_of_hurricanes(df):
    df_by_year = df.groupby(["ReportedYear"], as_index=False)["HurricaneFlag"].sum()
    # df_by_year = df_hurricane.groupby("ReportedYear").agg({'HurricaneFlag': ['sum']})
    # # print(type(df_by_year))
    # print(df_by_year)

    df_by_year.rename(columns = {'ReportedYear': 'Year',
                                 'HurricaneFlag':'TotalHurricanes'}, inplace=True)

    # print(df_by_year)

    df_by_year.plot(x="Year", 
                    y="TotalHurricanes", 
                    marker=".", 
                    kind="line")

    plt.title("Number of Hurricanes by Year That Made Landfall\n1851 - 2021")
    plt.xlabel("Year Reported")
    plt.ylabel("Number of Hurricanes Making Landfall")

    plt.show()

def strength_of_hurricanes(df):
    df_by_year = df.groupby(["ReportedYear"], as_index=False)["MaxWind_mph"].max()
    # df_by_year = df_hurricane.groupby("ReportedYear").agg({'MaxWind_mph': ['sum']})
    # # print(type(df_by_year))
    # print(df_by_year)

    df_by_year.rename(columns = {'ReportedYear': 'Year',
                                 'MaxWind_mph':'MaxStrength'}, inplace=True)

    # print(df_by_year)

    df_by_year.plot(x="Year", 
                    y="MaxStrength", 
                    marker=".", 
                    kind="line")

    plt.title("Maximum Strength of Hurricanes (mph) by Year That Made Landfall\n1851 - 2021")
    plt.xlabel("Year Reported")
    plt.ylabel("Maximum Strength of Hurricanes (mph) Making Landfall")

    plt.show()

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

    df_hurricane['HurricaneFlag'] = df_hurricane.apply(lambda row: categorize(row), axis=1)

    number_of_hurricanes(df_hurricane)

    strength_of_hurricanes(df_hurricane)



################# Main Processing Section ##############################

if __name__ == '__main__':
    main()
