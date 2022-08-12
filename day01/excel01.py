import operator
from dataclasses import replace
import time

import xlrd
from xlrd import xldate_as_datetime


def date_t(dated):
    for i in dated:
        if len(i.strip()) != 0:
            # print('i: ', i)
            return i


month_dict = {
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九',
    '10': '十',
    '11': '十一',
    '12': '十二',
}


def excel_tag():

    excel1 = xlrd.open_workbook('./2022.8.1--2022.8.7 .xlsx')
    table1 = excel1.sheet_by_index(6)

    # print(table1.row(1)[2].value)
    # print(table1.cell_value(1, 2))
    # print(table1.cell_value(6, 3))
    print(table1.row_values(3))
    # print(table1.cell_value(3, 2))
    da = xlrd.xldate.xldate_as_datetime(table1.row_values(3)[4], "%H/%M/%S")
    # da.strftime("%X")
    da1 = str(da)[-8:]
    print(da1)


    dated0 = table1.row_values(1)
    # print('dated0', dated0)
    dated = date_t(dated0).strip()
    # dated = table1.cell_value(1, 2)
    print('dated: ', dated)
    dated1 = dated.split()[1].split('月')
    y = dated1[0].split('年')[0].strip()
    m = dated1[0].split('年')[1]
    d = dated1[1].split('日')[0]
    w = dated[-1]
    M = month_dict.get(m) + '月'
    D = d
    if len(m) == 1:
        m = '0' + m
    if len(d) == 1:
        d = '0' + d

    # print(m, d)

    list1 = []
    rows = table1.nrows
    nums = 0
    for i in range(rows):
        col = table1.row_values(i)
        if i >= 3 and len(col[3].strip()) != 0 and col[5].strip() != '140ST1#':
            dateH = xldate_as_datetime(col[4], 0).strftime('%H')
            dateM = xldate_as_datetime(col[4], 0).strftime('%M')
            dateS = xldate_as_datetime(col[4], 0).strftime('%S')
            # print(dateH, ":", dateM, ":", dateS, sep='')
            num = ''
            num1 = str(col[0]).split('.0')[0]
            if len(num1) == 1:
                num1 = '0' + num1
            num = m + d + num1
            tag = num + col[3].strip()
            tag = tag.replace(' ', '')
            time = dateH + ':' + dateM + ':' + dateS

            date = y + '-' + m + '-' + d

            time1 = xlrd.xldate.xldate_as_datetime(col[4], '%X')
            time2 = str(time1)[-8:]


            tag_name = tag[6:]
            if operator.contains(tag_name, '好剧'):
                tag_name = tag_name[:7]
            elif operator.contains(tag_name, '剧场'):
                tag_name = tag_name[:8]
            copy_name = '000000' + tag_name

            # if w == '三' and i == 3:
            #     tag = num + col[3].strip().replace('                  ', ' ')
            #     copy_name = '000000法治测试卡 *（1）'
            #     # time = '05:35:00'
            # if w == '三' and i == 4:
            #     tag = num + col[3].strip().replace('                  ', ' ')
            #     copy_name = '000000法治测试卡 *（2）'
            # if i == 35:
            #     copy_name = '000000法治黄金剧场-03'
            # if w == '日' and i == 35:
            #     copy_name = '000000法治黄金剧场-3（周日）'

            if w == '三':
                if i == 3:
                    tag = num + col[3].strip().replace('                  ', ' ')
                    copy_name = '000000法治测试卡 *（1）'
                    # time = '05:35:00'
                if i == 4:
                    tag = num + col[3].strip().replace('                  ', ' ')
                    copy_name = '000000法治测试卡 *（2）'
                if i == 30:
                    copy_name = '000000法治黄金剧场-03'
            if w != '三' and i == 35:
                copy_name = '000000法治黄金剧场-03'
                if w == '日' and i == 35:
                    copy_name = '000000法治黄金剧场-3（周日）'



            # time = '00:00:00'
            list1.append({'tag': tag, 'time': time2, 'copy_name': copy_name, 'month': M, 'day': D, 'date': date})
            nums += 1

    print(nums)
    return list1

