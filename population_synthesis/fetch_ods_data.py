import pandas as pd
import ezodf

doc = ezodf.opendoc('Bevölkerung_2019_Zentroidkoordinaten.ods')

# convert the first sheet to a pandas.DataFrame
sheet = doc.sheets[0]
df_dict = {}
col_index = 0
for i, row in enumerate(sheet.rows()):
    # row is a list of cells
    # assume the header is on the first row
    if i == 0:
        # columns as lists in a dictionary
        df_dict = {cell.value: [] for cell in row}
        # create index for the column headers
        col_index = {j: cell.value for j, cell in enumerate(row)}
        continue
    for j, cell in enumerate(row):
        # use header instead of column index
        df_dict[col_index[j]].append(cell.value)
# and convert to a DataFrame
df = pd.DataFrame(df_dict)


def get_district_coordinate(district):
    x_coord_column = 2
    y_coord_column = 3
    row = district
    x = df.iloc[row, x_coord_column]
    y = df.iloc[row, y_coord_column]
    return [x, y]
