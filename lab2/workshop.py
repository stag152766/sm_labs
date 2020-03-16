# from openpyxl import load_workbook
#
# wb = load_workbook('TT.xlsx')
# sheet = wb.get_sheet_by_name('TT')
#
# U1 = U2 = U3 = U4 = U5 = U6 = 0
# N = [[], [], [], [], [], []]
# T = [[], [], [], [], [], []]
# n = 100 + 1
# m = 6
#
# for i in range(6):
#     T[i].append(0)
#     N[i].append(0)
#
# for i in range(1, n):
#     N[0].append(T[0][i - 1])
#     Ui1 = sheet.cell(i + 1, 1).value
#     T[0].append(N[0][i] + int(Ui1))
#
# for j in range(1, m):
#     N[j].append(T[j - 1][1])
#     U1j = sheet.cell(2, j + 1).value
#     T[j].append(N[j][1] + int(U1j))
#
# for i in range(2, n):
#     for j in range(1, m):
#         N[j].append(max(T[j][i - 1], T[j - 1][i]))
#         U = sheet.cell(i, j).value
#         T[j].append(N[j][i] + int(U))
# #print(T[-1][-1])
#
# for i in range(len(N)):
#     current_row = N[i]
#     for j in current_row:
#         print("%7s" % (j), end="\t\t")
#     print('\r')