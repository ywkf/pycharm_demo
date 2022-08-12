

class Dtd:

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

        '一': '1',
        '二': '2',
        '三': '3',
        '四': '4',
        '五': '5',
        '六': '6',
        '七': '7',
        '八': '8',
        '九': '9',
        '十': '10',
        '十一': '11',
        '十二': '12'

    }

    def date_c_to_date_n(self, date_c):
        num = self.month_dict.get(date_c[0])
        date_n = num + ' 月'
        return date_n


if __name__ == '__main__':
    print(Dtd().date_c_to_date_n('八月'))