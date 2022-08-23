from asyncore import write
import pandas as pd

if __name__ == '__main__':
    titanic = pd.read_csv('titanic.csv')
    
    mask = titanic.sex == 'male'
    mask2 = titanic.age < 12
    mask3 = titanic.survived == 1
    
    #print(titanic.loc[mask3, ['survived', 'sex', 'age']])
    print(titanic.iloc[5:9, :2])
    
    writer = pd.ExcelWriter('titanic_survived.xlsx')
    
    titanic.loc[mask3, ['survived', 'sex', 'age']].to_excel(writer)
    writer.save()