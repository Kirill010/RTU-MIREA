def process_cell(cell):
    if cell is None:
        return None
    if '/' in cell:
        parts = cell.split('/')
        return parts[2]
    if '(' in cell:
        parts = cell.split('(')
        parts1 = parts[1].split(')')
        return (parts[0].strip() + ' ' + parts1[0].strip()
                + ' ' + parts1[1].strip())
    if '[at]' in cell:
        parts = cell.split('[at]')
        return parts[0]
    else:
        cell = cell[:-5]
    return cell


def remove_none(x):
    transformed_table = []
    for col_idx in range(len(x[0])):
        new_row = []
        for row_idx in range(len(x)):
            if x[row_idx][col_idx] is None:
                continue
            new_row.append(process_cell(x[row_idx][col_idx]))
        transformed_table.append(new_row)
    return transformed_table


def remove_duplicates(x):
    output = []
    control = set()
    for row in x:
        if row[0] in control:
            continue
        control.add(row[0])
        output.append(row)
    return output


def main(x):
    res = remove_none(x)
    res = remove_duplicates(res)
    return res


result = main([['Рорев Д.Ч.', 'rorev46[at]rambler.ru', '11/11/1999', '11/11/1999', '+7 (528) 665-02-46'],
               [None, None, None, None, None],
               ['Бадян Н.С.', 'badan87[at]mail.ru', '01/10/2000', '01/10/2000', '+7 (162) 815-69-35'],
               [None, None, None, None, None],
               ['Тизов З.Ш.', 'tizov38[at]yandex.ru', '24/03/2003', '24/03/2003', '+7 (183) 977-01-24']])
print(result)
