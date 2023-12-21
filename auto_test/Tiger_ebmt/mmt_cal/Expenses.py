class Expenses:

    def __init__(self, total_expense, client_expense, un_expense):
        '''

        :param total_expense: 总产生费用
        :param client_expense: 客户费用
        :param un_expense: 未报销费用
        '''

        self.total_expense = total_expense
        self.client_expense = client_expense
        self.un_expense = un_expense