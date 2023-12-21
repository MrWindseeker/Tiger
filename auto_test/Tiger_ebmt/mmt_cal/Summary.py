class Summary:

    def __init__(self, contract_value, first_year_revenue,  tax='Excl.Tax', currency='CNY'):
        '''
        :param contract_value:预算金额
        :param first_year_revenue:预计收入第一年所占百分比
        :param tax:是否含税 Incl.Tax含税； Excl.Tax不含税
        :param currency:货币类型
        '''
        self.tax = tax
        self.contract_value = contract_value
        self.currency = currency
        self.first_year_revenue = first_year_revenue
        self.Fee = None
        self.ERP = None
        self.TER = None
        self.NER = None
        self.SER = None
        self.margin1 = 0  # margin百分比
        self.margin2 = 0  # margin
        self.total_expense = None  # 总费用
        self.total_hours = 0  # 总工时
        self.Current_FY_TER = None
        self.resources = []  # 总资源list
        self.expense = None  # 费用类对象
        self.std_cost = None  # 每条资源的std和
        self.EAF = None
        self.NSR = None
        self.total_un_expense = None
        self.partner_leverage = 0
        self.contractor_expense = 0  # contractor的总费用
        self.subcontractor_expense = 0  # subcontractor的总费用
        # 以下是每个不同rank类型的工时
        self.partner_hours = 0
        self.director_hours = 0
        self.contractor_hours = 0
        self.subcontractor_hours = 0
        self.senior_hours = 0
        self.manager_hours = 0
        self.senior_manager_hours = 0
        self.staff_hours = 0
        self.intern_hours = 0
        self.GDS_hours = 0
        self.CBS_hours = 0
        # 以下是每个不同rank类型的工时占比
        self.partner_director_proportion = 0
        self.contractor_proportion = 0
        self.subcontractor_proportion = 0
        self.senior_proportion = 0
        self.manager_proportion = 0
        self.senior_manager_proportion = 0
        self.staff_proportion = 0
        self.intern_proportion = 0
        self.GDS_proportion = 0
        self.CBS_proportion = 0
        # 以下是每个不同rank类型的SER总费用
        self.partner_SER_expense = 0
        self.director_SER_expense = 0
        self.contractor_SER_expense = 0
        self.subcontractor_SER_expense = 0
        self.senior_SER_expense = 0
        self.manager_SER_expense = 0
        self.senior_manager_SER_expense = 0
        self.staff_SER_expense = 0
        self.intern_SER_expense = 0
        self.GDS_SER_expense = 0
        self.CBS_SER_expense = 0
        # 以下是每个不同rank类型的Fee Billed
        self.partner_Fee_Billed = 0
        self.director_Fee_Billed = 0
        self.contractor_Fee_Billed = 0
        self.subcontractor_Fee_Billed = 0
        self.senior_Fee_Billed = 0
        self.manager_Fee_Billed = 0
        self.senior_manager_Fee_Billed = 0
        self.staff_Fee_Billed = 0
        self.intern_Fee_Billed = 0
        self.GDS_Fee_Billed = 0
        self.CBS_Fee_Billed = 0
        self.total_Fee_Billed = 0
        # 以下是每个不同rank类型的Cost
        self.partner_Cost = 0
        self.director_Cost = 0
        self.contractor_Cost = 0
        self.subcontractor_Cost = 0
        self.senior_Cost = 0
        self.manager_Cost = 0
        self.senior_manager_Cost = 0
        self.staff_Cost = 0
        self.intern_Cost = 0
        self.GDS_Cost = 0
        self.CBS_Cost = 0
        self.total_Cost = 0
        # 以下是每个不同rank类型的Client Bill Rate Per Hour
        self.partner_Client = 0
        self.director_Client = 0
        self.contractor_Client = 0
        self.subcontractor_Client = 0
        self.senior_Client = 0
        self.manager_Client = 0
        self.senior_manager_Client = 0
        self.staff_Client = 0
        self.intern_Client = 0
        self.GDS_Client = 0
        self.CBS_Client = 0
        self.total_Client = 0
        # Summary Margin Analysis
        self.Summary_Margin_Analysis = {
            "+10": {"Fee": 0, "Margin Amount": 0, "Margin%": ""},
            "+5": {"Fee": 0, "Margin Amount": 0, "Margin%": ""},
            "Current Plan": {"Fee": 0, "Margin Amount": 0, "Margin%": ""},
            "-5": {"Fee": 0, "Margin Amount": 0, "Margin%": ""},
            "-10": {"Fee": 0, "Margin Amount": 0, "Margin%": ""},
        }

    def check_resource_expense(self, location='DL'):
        if self.tax == 'Incl.Tax':
            self.Fee = self.contract_value
        else:
            if location == 'DL':
                self.Fee = round(self.contract_value / (1 + 0.06), 2)
            elif location == 'HK':
                self.Fee = round(self.contract_value, 2)
            elif location == 'MG':
                self.Fee = round(self.contract_value / (1 + 0.1), 2)
        ser = 0
        total_std_cost = 0
        total_nsr = 0
        for rs in self.resources:
            ser = ser + rs.SER
            self.total_hours = self.total_hours + rs.working_hours + rs.ot_hours
            total_nsr = total_nsr + rs.NSR
            if rs.rank_type != 'contractor' and rs.rank_type != 'subcontractor':
                total_std_cost = total_std_cost+rs.std_cost
            if rs.rank_type == 'partner':
                self.partner_hours = self.partner_hours+rs.working_hours+rs.ot_hours
                self.partner_SER_expense = self.partner_SER_expense + rs.SER
                self.partner_Cost = round(self.partner_Cost + rs.std_cost, 2)
            if rs.rank_type == 'director':
                self.director_hours = self.director_hours+rs.working_hours+rs.ot_hours
                self.director_SER_expense = self.director_SER_expense + rs.SER
                self.director_Cost = round(self.director_Cost + rs.std_cost, 2)
            if rs.rank_type == 'contractor':
                self.contractor_expense = self.contractor_expense+(rs.working_hours+rs.ot_hours)*rs.std_cost_rate
                self.contractor_hours = self.contractor_hours+(rs.working_hours+rs.ot_hours)
                self.contractor_SER_expense = self.contractor_SER_expense + rs.SER
                self.contractor_Cost = round(self.contractor_Cost + rs.std_cost, 2)
            if rs.rank_type == 'subcontractor':
                self.subcontractor_expense = self.subcontractor_expense+(rs.working_hours+rs.ot_hours)*rs.std_cost_rate
                self.subcontractor_hours = self.subcontractor_hours + (rs.working_hours + rs.ot_hours)
                self.subcontractor_SER_expense = self.subcontractor_SER_expense + rs.SER
                self.subcontractor_Cost = round(self.subcontractor_Cost + rs.std_cost, 2)
            if rs.rank_type == 'senior':
                self.senior_hours = self.senior_hours + (rs.working_hours + rs.ot_hours)
                self.senior_SER_expense = self.senior_SER_expense + rs.SER
                self.senior_Cost = round(self.senior_Cost + rs.std_cost, 2)
            if rs.rank_type == 'manager':
                self.manager_hours = self.manager_hours + (rs.working_hours + rs.ot_hours)
                self.manager_SER_expense = self.manager_SER_expense + rs.SER
                self.manager_Cost = round(self.manager_Cost + rs.std_cost, 2)
            if rs.rank_type == 'senior_manager':
                self.senior_manager_hours = self.senior_manager_hours + (rs.working_hours + rs.ot_hours)
                self.senior_manager_SER_expense = self.senior_manager_SER_expense + rs.SER
                self.senior_manager_Cost = round(self.senior_manager_Cost + rs.std_cost, 2)
            if rs.rank_type == 'staff':
                self.staff_hours = self.staff_hours + (rs.working_hours + rs.ot_hours)
                self.staff_SER_expense = self.staff_SER_expense + rs.SER
                self.staff_Cost = round(self.staff_Cost + rs.std_cost, 2)
            if rs.rank_type == 'intern':
                self.intern_hours = self.intern_hours + (rs.working_hours + rs.ot_hours)
                self.intern_SER_expense = self.intern_SER_expense + rs.SER
                self.intern_Cost = round(self.intern_Cost + rs.std_cost, 2)
            if rs.rank_type == 'GDS':
                self.GDS_hours = self.GDS_hours + (rs.working_hours + rs.ot_hours)
                self.GDS_SER_expense = self.GDS_SER_expense + rs.SER
                self.GDS_Cost = round(self.GDS_Cost + rs.std_cost, 2)
            if rs.rank_type == 'CBS':
                self.CBS_hours = self.CBS_hours + (rs.working_hours + rs.ot_hours)
                self.CBS_SER_expense = self.CBS_SER_expense + rs.SER
                self.CBS_Cost = round(self.CBS_Cost + rs.std_cost, 2)
        self.total_expense = round(self.expense.total_expense, 2)
        if self.partner_hours != 0:
            self.partner_leverage = round(((self.total_hours-self.partner_hours)/self.partner_hours), 2)
        self.NSR = round(total_nsr, 2)
        self.std_cost = round(total_std_cost, 2)
        self.SER = round(ser, 2)
        self.TER = round(self.Fee + self.expense.client_expense, 2)
        self.NER = round(self.TER - self.expense.total_expense, 2)
        self.ERP = "{:.2%}".format(self.NER/self.SER)
        self.margin2 = round(self.NER - self.std_cost, 2)
        self.margin1 = "{:.2%}".format(self.margin2/self.NER)
        self.Current_FY_TER = round(self.TER * self.first_year_revenue * 0.01, 2)
        self.EAF = "{:.2%}".format(self.NER/self.NSR-1)
        self.total_un_expense = round(self.expense.un_expense, 2)

        # MMT Rank工时占比
        self.partner_director_proportion = "{:.2%}".format((self.partner_hours + self.director_hours)/self.total_hours)
        self.contractor_proportion = "{:.2%}".format(self.contractor_hours / self.total_hours)
        self.subcontractor_proportion = "{:.2%}".format(self.subcontractor_hours / self.total_hours)
        self.senior_proportion = "{:.2%}".format(self.senior_hours / self.total_hours)
        self.manager_proportion = "{:.2%}".format(self.manager_hours / self.total_hours)
        self.senior_manager_proportion = "{:.2%}".format(self.senior_manager_hours / self.total_hours)
        self.staff_proportion = "{:.2%}".format(self.staff_hours / self.total_hours)
        self.intern_proportion = "{:.2%}".format(self.intern_hours / self.total_hours)
        self.GDS_proportion = "{:.2%}".format(self.GDS_hours / self.total_hours)
        self.CBS_proportion = "{:.2%}".format(self.CBS_hours / self.total_hours)

        # Break Down By Rank
        if self.SER != 0:
            self.partner_Fee_Billed = round(self.partner_SER_expense / self.SER * self.Fee, 2)
            self.director_Fee_Billed = round(self.director_SER_expense / self.SER * self.Fee, 2)
            self.contractor_Fee_Billed = round(self.contractor_SER_expense / self.SER * self.Fee, 2)
            self.subcontractor_Fee_Billed = round(self.subcontractor_SER_expense / self.SER * self.Fee, 2)
            self.senior_Fee_Billed = round(self.senior_SER_expense / self.SER * self.Fee, 2)
            self.manager_Fee_Billed = round(self.manager_SER_expense / self.SER * self.Fee, 2)
            self.senior_manager_Fee_Billed = round(self.senior_manager_SER_expense / self.SER * self.Fee, 2)
            self.staff_Fee_Billed = round(self.staff_SER_expense / self.SER * self.Fee, 2)
            self.intern_Fee_Billed = round(self.intern_SER_expense / self.SER * self.Fee, 2)
            self.GDS_Fee_Billed = round(self.GDS_SER_expense / self.SER * self.Fee, 2)
            self.CBS_Fee_Billed = round(self.CBS_SER_expense / self.SER * self.Fee, 2)
        if self.partner_hours != 0:
            self.partner_Client = round(self.partner_Fee_Billed/self.partner_hours, 2)
        if self.director_hours != 0:
            self.director_Client = round(self.director_Fee_Billed/self.director_hours, 2)
        if self.contractor_hours != 0:
            self.contractor_Client = round(self.contractor_Fee_Billed/self.contractor_hours, 2)
        if self.subcontractor_hours != 0:
            self.subcontractor_Client = round(self.subcontractor_Fee_Billed/self.subcontractor_hours, 2)
        if self.senior_hours != 0:
            self.senior_Client = round(self.senior_Fee_Billed/self.senior_hours ,2)
        if self.manager_hours != 0:
            self.manager_Client = round(self.manager_Fee_Billed/self.manager_hours, 2)
        if self.senior_manager_hours != 0:
            self.senior_manager_Client = round(self.senior_manager_Fee_Billed/self.senior_manager_hours, 2)
        if self.intern_hours != 0:
            self.intern_Client = round(self.intern_Fee_Billed/self.intern_hours, 2)
        if self.staff_hours != 0:
            self.staff_Client = round(self.staff_Fee_Billed/self.staff_hours, 2)
        if self.GDS_hours != 0:
            self.GDS_Client = round(self.GDS_Fee_Billed/self.GDS_hours, 2)
        if self.CBS_hours != 0:
            self.CBS_Client = round(self.CBS_Fee_Billed/self.CBS_hours, 2)
        self.total_Fee_Billed = self.partner_Fee_Billed + self.director_Fee_Billed + self.contractor_Fee_Billed + \
            self.subcontractor_Fee_Billed + self.senior_Fee_Billed + self.manager_Fee_Billed + \
            self.senior_manager_Fee_Billed + self.staff_Fee_Billed + self.intern_Fee_Billed + \
            self.GDS_Fee_Billed + self.CBS_Fee_Billed
        self.total_Cost = self.partner_Cost + self.director_Cost + self.contractor_Cost + \
            self.subcontractor_Cost + self.senior_Cost + self.manager_Cost + \
            self.senior_manager_Cost + self.staff_Cost + self.intern_Cost + \
            self.GDS_Cost + self.CBS_Cost
        self.total_Client = self.partner_Client + self.director_Client + self.contractor_Client + \
            self.subcontractor_Client + self.senior_Client + self.manager_Client + \
            self.senior_manager_Client + self.staff_Client + self.intern_Client + \
            self.GDS_Client + self.CBS_Client

        # Summary Margin Analysis
        Current_Plan_Margin = round(self.margin2/self.NER, 4)
        margin_proportion1 = Current_Plan_Margin+0.1
        margin_proportion2 = Current_Plan_Margin + 0.05
        margin_proportion3 = Current_Plan_Margin - 0.05
        margin_proportion4 = Current_Plan_Margin - 0.1

        if margin_proportion1 < 1:
            self.Summary_Margin_Analysis['+10']['Fee'] = round(self.std_cost / (1-margin_proportion1) + self.total_un_expense, 2)
            self.Summary_Margin_Analysis['+10']['Margin Amount'] = round(self.std_cost / (1 - margin_proportion1) - self.std_cost, 2)
        self.Summary_Margin_Analysis['+10']['Margin%'] = "{:.2%}".format(margin_proportion1)

        if margin_proportion2 < 1:
            self.Summary_Margin_Analysis['+5']['Fee'] = round(
                self.std_cost / (1 - margin_proportion2) + self.total_un_expense, 2)
            self.Summary_Margin_Analysis['+5']['Margin Amount'] = round(
                self.std_cost / (1 - margin_proportion2) - self.std_cost, 2)
        self.Summary_Margin_Analysis['+5']['Margin%'] = "{:.2%}".format(margin_proportion2)

        if Current_Plan_Margin < 1:
            self.Summary_Margin_Analysis['Current Plan']['Fee'] = self.Fee
            self.Summary_Margin_Analysis['Current Plan']['Margin Amount'] = self.margin2
        self.Summary_Margin_Analysis['Current Plan']['Margin%'] = self.margin1

        if margin_proportion3 < 1:
            self.Summary_Margin_Analysis['-5']['Fee'] = round(
                self.std_cost / (1 - margin_proportion3) + self.total_un_expense, 2)
            self.Summary_Margin_Analysis['-5']['Margin Amount'] = round(
                self.std_cost / (1 - margin_proportion3) - self.std_cost, 2)
        self.Summary_Margin_Analysis['-5']['Margin%'] = "{:.2%}".format(margin_proportion3)

        if margin_proportion4 < 1:
            self.Summary_Margin_Analysis['-10']['Fee'] = round(
                self.std_cost / (1 - margin_proportion4) + self.total_un_expense, 2)
            self.Summary_Margin_Analysis['-10']['Margin Amount'] = round(
                self.std_cost / (1 - margin_proportion4) - self.std_cost, 2)
        self.Summary_Margin_Analysis['-10']['Margin%'] = "{:.2%}".format(margin_proportion4)

    def add_resource(self, resource):
        self.resources.append(resource)

    def add_expense(self, expense):
        self.expense = expense

    def print_dashbord(self):
        # print('--------------Summary---------------')
        print('Summary'.center(40, '-'))
        print(f'Fee({self.currency}): {self.Fee}', '-----', f'SER: {self.SER}')
        print(f'ERP: {self.ERP}', '-----', f'TER: {self.TER}')
        print(f'Margin%: {self.margin1}', '-----', f'NER: {self.NER}')
        print(f'Margin: {self.margin2}', '-----', f'Current FY TER: {self.Current_FY_TER}')
        print(f'Total Expense: {self.total_expense}', '-----', f'Total Hours: {self.total_hours}')
        print(f'Partner&Executive Director : {self.partner_director_proportion}', '-----', f'Senior: {self.senior_proportion}')
        print(f'Senior Manager: {self.senior_manager_proportion}', '-----', f'Staff : {self.staff_proportion}')
        print(f'Manager: {self.manager_proportion}', '-----', f'Intern : {self.intern_proportion}')
        print(f'Contractor: {self.contractor_proportion}', '-----', f'GDS : {self.GDS_proportion}')
        print(f'Subcontractor: {self.subcontractor_proportion}', '-----', f'CBS : {self.CBS_proportion}')
        # print('--------------Summary---------------\n')
        print('Summary'.center(40, '-'))
        print('\n')

    def print_detail(self):
        print('--------------Summary Information---------------')
        print(f'Total Engagement Revenue(TER): {self.TER}')
        print(f'Net Engagement Revenue(NER): {self.NER}')
        print(f'Standard Cost: {self.std_cost}')
        print(f'Engagement Margin: {self.margin2}')
        print(f'Engagement Margin%: {self.margin1}')
        print(f'Total Engagement Hours: {self.total_hours}')
        print(f'Partner Leverage: {self.partner_leverage}')
        print(f'Standard Engagement Revenue(SER): {self.SER}')
        print(f'Estimated Realization Percent(ERP): {self.ERP}')
        print(f'Engagement Adjusted Factor(EAF): {self.EAF}')
        print(f'Contractor: {self.contractor_hours}')
        print(f'Subcontractor: {self.subcontractor_hours}')
        print(f'Total Expense: {self.total_expense}')
        print(f'Total Unrecovered Expenses: {self.total_un_expense}')
        print(f'Current FYTER(CYTR): {self.Current_FY_TER}')
        print('--------------Summary Information---------------\n')
        print('--------------Break Down By Rank----------------')
        print(f'Partner: {self.partner_Client}---{self.partner_Fee_Billed}---{self.partner_Cost}')
        print(f'Executive Director: {self.director_Client}---{self.director_Fee_Billed}---{self.director_Cost}')
        print(f'Senior Manager: {self.senior_manager_Client}---{self.senior_manager_Fee_Billed}---{self.senior_manager_Cost}')
        print(f'Manager: {self.manager_Client}---{self.manager_Fee_Billed}---{self.manager_Cost}')
        print(f'Senior: {self.senior_Client}---{self.senior_Fee_Billed}---{self.senior_Cost}')
        print(f'Staff/Assistant: {self.staff_Client}---{self.staff_Fee_Billed}---{self.staff_Cost}')
        print(f'Intern: {self.intern_Client}---{self.intern_Fee_Billed}---{self.intern_Cost}')
        print(f'Contractor: {self.contractor_Client}---{self.contractor_Fee_Billed}---{self.contractor_Cost}')
        print(f'Subcontractor: {self.subcontractor_Client}---{self.subcontractor_Fee_Billed}---{self.subcontractor_Cost}')
        print(f'GDS: {self.GDS_Client}---{self.GDS_Fee_Billed}---{self.GDS_Cost}')
        print(f'CBS: {self.CBS_Client}---{self.CBS_Fee_Billed}---{self.CBS_Cost}')
        print(f'Total: {self.total_Client}---{self.total_Fee_Billed}---{self.total_Cost}')
        print('--------------Break Down By Rank----------------\n')

        print('--------------Summary Margin Analysis--------------')
        print(f'+10: {self.Summary_Margin_Analysis["+10"]["Fee"]}, '
              f'{self.Summary_Margin_Analysis["+10"]["Margin Amount"]}, '
              f'{self.Summary_Margin_Analysis["+10"]["Margin%"]}')

        print(f'+5: {self.Summary_Margin_Analysis["+5"]["Fee"]}, '
              f'{self.Summary_Margin_Analysis["+5"]["Margin Amount"]}, '
              f'{self.Summary_Margin_Analysis["+5"]["Margin%"]}')

        print(f'Current Plan: {self.Summary_Margin_Analysis["Current Plan"]["Fee"]}, '
              f'{self.Summary_Margin_Analysis["Current Plan"]["Margin Amount"]}, '
              f'{self.Summary_Margin_Analysis["Current Plan"]["Margin%"]}')

        print(f'-5: {self.Summary_Margin_Analysis["-5"]["Fee"]}, '
              f'{self.Summary_Margin_Analysis["-5"]["Margin Amount"]}, '
              f'{self.Summary_Margin_Analysis["-5"]["Margin%"]}')

        print(f'-10: {self.Summary_Margin_Analysis["-10"]["Fee"]}, '
              f'{self.Summary_Margin_Analysis["-10"]["Margin Amount"]}, '
              f'{self.Summary_Margin_Analysis["-10"]["Margin%"]}')

        print('--------------Summary Margin Analysis--------------\n')















