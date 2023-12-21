class Expenses:

    def __init__(self, expense_type, incurred_expense, client_expense, un_expense):
        '''
        "param expense_type: 费用类型  {
            Lead SMU (Own Expenses) : LS
            Inter-firm : IF
        }
        :param incurred_expense: 总产生费用
        :param client_expense: 客户费用
        :param un_expense: 未报销费用
        '''
        self.expense_type = expense_type
        self.incurred_expense = incurred_expense
        self.client_expense = client_expense
        self.un_expense = un_expense