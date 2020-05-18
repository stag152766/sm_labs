import xlrd
import xlsxwriter

path = 'Ishodnye-dannye-po-kapremontu.xlsx'

input_workbook = xlrd.open_workbook(path)
input_worksheet_capex = input_workbook.sheet_by_index(0)
input_worksheet_district = input_workbook.sheet_by_index(1)

# list1
capex = []

# list2
house_id = []
square = []
year = []
elevator = []

for y in range(7, input_worksheet_capex.nrows):
    capex.append(int(input_worksheet_capex.cell_value(y, 1)))

for y in range(1, input_worksheet_district.nrows):
    house_id.append(int(input_worksheet_district.cell_value(y, 0)))
    square.append(int(input_worksheet_district.cell_value(y, 1)))
    year.append(int(input_worksheet_district.cell_value(y, 2)))
    elevator.append(int(input_worksheet_district.cell_value(y, 3)))
"""
print(capex)
print(house_id)
print(square)
print(year)
print(elevator)
"""
t_house = []
t_inc = []
t_exp = []
t_delta = []
t_year = []
income = 0
expense = 0
cost = 5
elevator_cost = 5000000

for t in range(1900, 2050):
    for i in range(len(year)):
        if t >= year[i]:
            age = t - year[i]
            income += square[i] * cost * 12
            if age == 15:
                expense = square[i] * capex[0]
            elif age == 25:
                expense = square[i] * capex[1]
            elif age == 35:
                expense = square[i] * capex[2]
            elif age == 45:
                expense = square[i] * capex[3]
                if elevator[i] == 1:
                    expense += elevator_cost
            elif age == 55:
                expense = square[i] * capex[4]
            elif age == 65:
                expense = square[i] * capex[5]
            elif age == 75:
                expense = square[i] * capex[6]
            elif age == 85:
                expense = square[i] * capex[7]
                if elevator[i] == 1:
                    expense += elevator_cost
            elif age == 95:
                expense = square[i] * capex[8]
            elif age == 105:
                expense = square[i] * capex[9]
            elif age == 115:
                expense = square[i] * capex[10]
                if elevator[i] == 1:
                    expense += elevator_cost
            elif age == 125:
                expense = square[i] * capex[11]
            t_house.append(house_id[i])
    t_year.append(t)
    t_inc.append(income)
    t_exp.append(expense)
    t_delta.append(income-expense)

    income = 0
    expense = 0

print(t_year)
print(t_inc)
print(t_exp)
print(t_delta)

outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

outSheet.write("A1", "Year")
outSheet.write("B1", "Income")
outSheet.write("C1", "Expense")
outSheet.write("D1", "Delta")

for item in range(len(t_year)):
    outSheet.write(item+1, 0, t_year[item])
    outSheet.write(item+1, 1, t_inc[item])
    outSheet.write(item + 1, 2, t_exp[item])
    outSheet.write(item + 1, 3, t_delta[item])

outWorkbook.close()
