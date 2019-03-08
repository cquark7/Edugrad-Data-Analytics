import pandas as pd
# Part I data
from data import exam_data, browser_data, employee_data, sample_data


exam_data = pd.DataFrame(exam_data)

del exam_data['attempts']
# print(exam_data)

browser = pd.DataFrame(browser_data, index=['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror'])

browser.index = ['Iceweasel', 'Safari', 'IE 10', 'Chrome', 'Comodo Dragon']
# print(browser)

employees = pd.DataFrame(employee_data)
# print(employees[employees.Age >= 68])


Army = pd.DataFrame(sample_data)
Army.set_index('Origin', inplace=True)
print(Army)

# df2 = Army.loc[['Georgia', 'Florida', 'California'], ['Regiment', 'Deaths', 'Size']]
# print(df2)
#
# print(Army.iloc[2:9, 3:7])
#
# print(Army.iloc[3:])
#
# print(Army.iloc[:, 4:9])
#
# print(Army[Army.Battles > 5])

# print(Army[(Army.Deaths > 500) | (Army.Deaths < 50)])

# print(Army[~(Army.Regiment == 'Scouts')])

print(Army.loc['Alaska'][2])
