

class Summary:

    def __init__(self, contract_value, first_year_revenue, risk_level, tax='Incl.Tax', currency='CNY', working_type='Hours'):
        '''
            contract_value: 预算金额
            first_year_revenue: 首年的回报率
            risk_level: 风险等级百分比
        '''
        self.working_type = working_type
        self.Total_Expense = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.Rate_Per_Day = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.Cost_Sub_TER = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.LT_Margin_percentage = {
            'In': None,
            'Ex': None
        }
        self.LT_Margin = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.Margin_percentage = {
            'In': None,
            'Ex': None
        }
        self.Margin = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.ERP = {
            'In': None,
            'Ex': None
        }
        self.SER = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.NER = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.TER = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.EAF = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.Long_Term_Cost = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.Cost_of_Subcontractors = {
            'In': 0.0,
            'Ex': 0.0
        }
        self.Std_Margin_excl_Partner_Cost_percentage = {
            'In': None,
            'Ex': None
        }
        self.LT_Margin_excl_Partner_Cost_percentage = {
            'In': None,
            'Ex': None
        }
        self.total_nsr_cost = 0.0    # 所有resource的nsr cost总和
        self.resources = []
        self.Technology_expense = []
        self.expense = []

        self.total_expense_incurred = 0.0   # 总已发生的费用
        self.total_expense_client = 0.0 # 总客户费用
        self.total_expense_unexpense = 0.0  # 总未报销费用

        self.LS_expense_incuured = 0.0
        self.LS_expense_client = 0.0
        self.LS_expense_unexpense = 0.0
        self.IF_expense_incuured = 0.0
        self.IF_expense_client = 0.0
        self.IF_expense_unexpense = 0.0
        self.TOP_expense_incuured = 0.0
        self.TOP_expense_client = 0.0
        self.TOP_expense_unexpense = 0.0
        self.VS_expense_incuured = 0.0
        self.VS_expense_client = 0.0
        self.VS_expense_unexpense = 0.0
        self.OLS_expense_incuured = 0.0
        self.OLS_expense_client = 0.0
        self.OLS_expense_unexpense = 0.0



        self.contract_value = contract_value
        self.first_year_revenue = first_year_revenue
        self.tax = tax
        self.currency = currency
        self.risk_level = risk_level/100  # 风险等级百分比
        self.imprest = 0.0  # 备用金
        self.total_working = 0  # 总工时
        self.total_std_cost = 0.0   # 总的std
        self.std_cost = 0.0  # 除contractor和subcontractor所有resource总std
        self.lt_cost = 0.0   # 除contractor和subcontractor所有resource总lt cost
        self.contractor_std = 0.0  # contractor的std
        self.subcontractor_std = 0.0  # subcontractor的std
        self.partner_std = 0.0  # partner的std
        self.partner_lt_cost = 0.0  # partner的lt cost
        self.total_technology_subcontractor = 0.0  # 技术费用Technology的subcontractor总和
        self.total_technology_TOLO = 0.0    # 技术费用(TOther、LOther)
        self.total_technology_TP = 0.0      # 技术费用Pilot Products
        # 以下是每个不同source type的工时
        self.onshore_type_hours = 0.0
        self.GDS_type_hours = 0.0
        self.subcontractors_type_hours = 0.0
        # 以下是每个不同source type的SER
        self.onshore_type_SER = 0.0
        self.GDS_type_SER = 0.0
        # 以下是每个不同rank类型的工时
        self.partner_hours = 0.0
        self.director_hours = 0.0
        self.contractor_hours = 0.0
        self.subcontractor_hours = 0.0
        self.senior_hours = 0.0
        self.manager_hours = 0.0
        self.senior_manager_hours = 0.0
        self.staff_hours = 0.0
        self.intern_hours = 0.0
        self.GDS_hours = 0.0
        self.CBS_hours = 0.0
        # 以下是每个不同rank类型的工时占比
        self.partner_proportion = 0.0
        self.director_proportion = 0.0
        self.contractor_proportion = 0.0
        self.subcontractor_proportion = 0.0
        self.senior_proportion = 0.0
        self.manager_proportion = 0.0
        self.senior_manager_proportion = 0.0
        self.staff_proportion = 0.0
        self.intern_proportion = 0.0
        self.GDS_proportion = 0.0
        self.CBS_proportion = 0.0

        # 以下是不同费用类型的Revenue
        self.TP_type_revenue = 0.0


    def check_resource(self, location='DL'):
        if self.tax == 'Excl.Tax':
            self.TER['In'] = self.contract_value
            self.TER['Ex'] = self.contract_value
        else:
            if location == 'DL':
                self.TER['In'] = round(self.contract_value / (1 + 0.06), 2)
                self.TER['Ex'] = round(self.contract_value / (1 + 0.06), 2)
            elif location == 'HK':
                self.TER['In'] = round(self.contract_value, 2)
                self.TER['Ex'] = round(self.contract_value, 2)
            elif location == 'MG':
                self.TER['In'] = round(self.contract_value / (1 + 0.1), 2)
                self.TER['Ex'] = round(self.contract_value / (1 + 0.1), 2)
        for ex in self.expense:
            self.total_expense_client = self.total_expense_client + ex.client_expense
            self.total_expense_incurred = self.total_expense_incurred + ex.incurred_expense
            self.total_expense_unexpense = self.total_expense_unexpense + ex.un_expense
            if ex.expense_type == 'LS':
                self.LS_expense_client = self.LS_expense_client + ex.client_expense
                self.LS_expense_incuured = self.LS_expense_incuured + ex.incurred_expense
                self.LS_expense_unexpense = self.LS_expense_unexpense + ex.un_expense
            elif ex.expense_type == 'IF':
                self.IF_expense_client = self.IF_expense_client + ex.client_expense
                self.IF_expense_incuured = self.IF_expense_incuured + ex.incurred_expense
                self.IF_expense_unexpense = self.IF_expense_unexpense + ex.un_expense

        self.imprest = self.total_expense_incurred * self.risk_level
        for rs in self.resources:
            self.total_nsr_cost = self.total_nsr_cost + rs.NSR_Cost
            self.SER['Ex'] = self.SER['Ex'] + rs.SER
            self.total_std_cost = self.total_std_cost + rs.Std
            if self.working_type == 'Days':
                working_hours = rs.working_hours * 8
            else:
                working_hours = rs.working_hours
            self.total_working = self.total_working + working_hours
            if rs.rank_type != 'contractor' and rs.rank_type != 'subcontractor':
                self.lt_cost = self.lt_cost + rs.LT_Cost
                self.std_cost = self.std_cost + rs.Std

            # 判断source type
            if rs.source_type == 'EY_Onshore':
                self.onshore_type_hours = self.onshore_type_hours + working_hours
                self.onshore_type_SER = self.onshore_type_SER + rs.SER
            elif rs.source_type == 'GDS':
                self.GDS_type_hours = self.GDS_type_hours + working_hours
                self.GDS_type_SER = self.GDS_type_SER + rs.SER
            elif rs.source_type == 'Subcontractors':
                self.subcontractors_type_hours = self.subcontractors_type_hours + working_hours

            # 判断rank type
            if rs.rank_type == 'partner':
                # 此处统计MMT Rank工时逻辑
                self.partner_hours = self.partner_hours + working_hours
                self.partner_std = self.partner_std + rs.Std
                self.partner_lt_cost = self.partner_lt_cost + rs.LT_Cost
                pass
            if rs.rank_type == 'contractor':
                self.contractor_hours = self.contractor_hours + working_hours
                self.contractor_std = self.contractor_std + rs.Std
            if rs.rank_type == 'subcontractor':
                self.subcontractor_hours = self.subcontractor_hours + working_hours
                self.subcontractor_std = self.subcontractor_std + rs.Std
            if rs.rank_type == 'director':
                self.director_hours = self.director_hours + working_hours
            if rs.rank_type == 'senior':
                self.senior_hours = self.senior_hours + working_hours
            if rs.rank_type == 'manager':
                self.manager_hours = self.manager_hours + working_hours
            if rs.rank_type == 'senior_manager':
                self.senior_manager_hours = self.senior_manager_hours + working_hours
            if rs.rank_type == 'staff':
                self.staff_hours = self.staff_hours + working_hours
            if rs.rank_type == 'intern':
                self.intern_hours = self.intern_hours + working_hours
            if rs.rank_type == 'GDS':
                self.GDS_hours = self.GDS_hours + working_hours
            if rs.rank_type == 'CBS':
                self.CBS_hours = self.CBS_hours + working_hours
        for ex in self.Technology_expense:
            if ex.Category == 'TOP':
                self.TOP_expense_incuured = self.TOP_expense_incuured + ex.total_cost
                self.total_technology_TOLO = self.total_technology_TOLO + ex.total_cost
                self.total_expense_incurred = self.total_expense_incurred + ex.total_cost
                if ex.Recoverable == 'Yes':
                    self.TOP_expense_client = self.TOP_expense_client + ex.total_cost
            elif ex.Category == 'OLS':
                self.OLS_expense_incuured = self.OLS_expense_incuured + ex.total_cost
                self.total_technology_TOLO = self.total_technology_TOLO + ex.total_cost
                self.total_expense_incurred = self.total_expense_incurred + ex.total_cost
                if ex.Recoverable == 'Yes':
                    self.OLS_expense_client = self.OLS_expense_client + ex.total_cost
            elif ex.Category == 'VS':
                self.VS_expense_incuured = self.VS_expense_incuured + ex.total_cost
                self.total_technology_subcontractor = self.total_technology_subcontractor + ex.total_cost
                if ex.Recoverable == 'Yes':
                    self.VS_expense_client = self.VS_expense_client + ex.total_cost
            elif ex.Category == 'TP':
                self.TP_type_revenue = self.TP_type_revenue + ex.Revenue
                self.total_technology_TP = self.total_technology_TP + ex.total_cost
        self.LS_expense_unexpense = round(self.LS_expense_incuured - self.LS_expense_client, 2)
        self.IF_expense_unexpense = round(self.IF_expense_incuured - self.IF_expense_client, 2)
        self.TOP_expense_unexpense = round(self.TOP_expense_incuured - self.TOP_expense_client, 2)
        self.OLS_expense_unexpense = round(self.OLS_expense_incuured - self.OLS_expense_client, 2)
        self.VS_expense_unexpense = round(self.VS_expense_incuured - self.VS_expense_client, 2)

        # 计算每个rank的工时占比
        self.partner_proportion = "{:.2%}".format(self.partner_hours / self.total_working)
        self.contractor_proportion = "{:.2%}".format(self.contractor_hours / self.total_working)
        self.subcontractor_proportion = "{:.2%}".format(self.subcontractor_hours / self.total_working)
        self.senior_proportion = "{:.2%}".format(self.senior_hours / self.total_working)
        self.manager_proportion = "{:.2%}".format(self.manager_hours / self.total_working)
        self.senior_manager_proportion = "{:.2%}".format(self.senior_manager_hours / self.total_working)
        self.GDS_proportion = "{:.2%}".format(self.GDS_hours / self.total_working)
        self.CBS_proportion = "{:.2%}".format(self.CBS_hours / self.total_working)
        self.director_proportion = "{:.2%}".format(self.director_hours / self.total_working)
        self.staff_proportion = "{:.2%}".format(self.staff_hours / self.total_working)
        self.intern_proportion = "{:.2%}".format(self.intern_hours / self.total_working)

        self.Cost_Sub_TER['In'] = round((self.total_technology_subcontractor+self.contractor_std+self.subcontractor_std)
                                        * (1 + self.risk_level) / self.TER['In'], 2)
        self.Cost_Sub_TER['Ex'] = round((self.total_technology_subcontractor+self.contractor_std+self.subcontractor_std)
                                        / self.TER['Ex'], 2)
        self.Total_Expense['In'] = self.total_expense_incurred * (1 + self.risk_level)
        self.Total_Expense['Ex'] = self.total_expense_incurred
        self.NER['In'] = self.TER['In'] - self.Total_Expense['In'] - self.total_technology_subcontractor * (1+self.risk_level)
        self.NER['Ex'] = self.TER['In'] - self.Total_Expense['Ex'] - self.total_technology_subcontractor
        self.Margin_percentage['In'] = "{:.2%}".format(1 - self.std_cost * (1 + self.risk_level) / self.NER['In'])
        self.Margin_percentage['Ex'] = "{:.2%}".format(1 - self.std_cost / self.NER['Ex'])
        self.Margin['In'] = round(self.TER['In'] - self.std_cost * (1 + self.risk_level), 2)
        self.Margin['Ex'] = round(self.TER['Ex'] - self.std_cost, 2)
        self.LT_Margin_percentage['In'] = "{:.2%}".format(1 - self.lt_cost * (1 + self.risk_level) / self.NER['In'])
        self.LT_Margin_percentage['Ex'] = "{:.2%}".format(1 - self.lt_cost / self.NER['Ex'])
        self.LT_Margin['In'] = round(self.NER['In'] - self.std_cost * (1 + self.risk_level), 2)
        self.LT_Margin['Ex'] = round(self.NER['Ex'] - self.std_cost, 2)
        self.SER['In'] = self.SER['Ex'] * (1 + self.risk_level)
        self.EAF['In'] = round(self.NER['In'] / (self.total_nsr_cost * (1 + self.risk_level)) - 1, 2)
        self.EAF['Ex'] = round(self.NER['Ex'] / self.total_nsr_cost - 1, 2)
        self.Long_Term_Cost['In'] = self.lt_cost * (1 + self.risk_level)
        self.Long_Term_Cost['Ex'] = self.lt_cost
        self.Cost_of_Subcontractors['In'] = (self.contractor_std + self.subcontractor_std + self.total_technology_subcontractor) * (1 + self.risk_level)
        self.Cost_of_Subcontractors['Ex'] = (
                    self.contractor_std + self.subcontractor_std + self.total_technology_subcontractor)
        self.Std_Margin_excl_Partner_Cost_percentage['In'] = "{:.2%}".format(1 - (self.std_cost - self.partner_std) * (1 + self.risk_level) / self.NER['In'])
        self.Std_Margin_excl_Partner_Cost_percentage['Ex'] = "{:.2%}".format(1 - (self.std_cost - self.partner_std) / self.NER['Ex'])
        self.LT_Margin_excl_Partner_Cost_percentage['In'] = "{:.2%}".format(
            1 - (self.lt_cost - self.partner_lt_cost) * (1 + self.risk_level) / self.NER['In'])
        self.LT_Margin_excl_Partner_Cost_percentage['Ex'] = "{:.2%}".format(
            1 - (self.lt_cost - self.partner_lt_cost) / self.NER['Ex'])
        if self.SER['In'] != 0:
            self.ERP['In'] = "{:.2%}".format(self.NER['In'] / self.SER['In'])
        if self.SER['Ex'] != 0:
            self.ERP['Ex'] = "{:.2%}".format(self.NER['Ex'] / self.SER['Ex'])
        if self.working_type == 'Days':
            self.Rate_Per_Day['In'] = round(self.NER['In'] / (self.total_working / 8 - self.subcontractor_hours
                                                              / 8 - self.contractor_hours / 8), 2)
            self.Rate_Per_Day['Ex'] = round(self.NER['Ex'] / (
                        self.total_working / 8 - self.subcontractor_hours / 8 - self.contractor_hours / 8), 2)
        else:
            self.Rate_Per_Day['In'] = self.NER['In'] / (
                    self.total_working - self.subcontractor_hours - self.contractor_hours)
            self.Rate_Per_Day['Ex'] = self.NER['Ex'] / (
                    self.total_working - self.subcontractor_hours - self.contractor_hours)


    def add_resource(self, resources):
        self.resources.append(resources)

    def add_expense(self, expense):
        self.expense.append(expense)

    def add_technology_expense(self, Technology_expense):
        self.Technology_expense.append(Technology_expense)

    def print_dashboard(self):
        print('--------------------Dashboard--------------------')
        print(' '.ljust(20), 'TER'.ljust(20), 'NER'.ljust(20), 'SER'.ljust(20), 'ERP%'.ljust(20), 'Margion%'.ljust(20),
              'LT Margin%'.ljust(20), 'Cost of Subcontractors/TER'.ljust(20), 'Rate Per Day'.ljust(20), 'Total Expenses')
        print('In.Contingency'.ljust(20), f"{self.TER['In']}".ljust(20), f"{self.NER['In']}".ljust(20), f"{self.SER['In']}".ljust(20),
              f"{self.ERP['In']}".ljust(20), f"{self.Margin_percentage['In']}".ljust(20), f"{self.LT_Margin_percentage['In']}".ljust(20),
              f"{self.Cost_Sub_TER['In']}".ljust(30), f"{self.Rate_Per_Day['In']}".ljust(20), f"{self.Total_Expense['In']}")
        print('Ex.Contingency'.ljust(20), f"{self.TER['Ex']}".ljust(20), f"{self.NER['Ex']}".ljust(20),
              f"{self.SER['Ex']}".ljust(20), f"{self.ERP['Ex']}".ljust(20), f"{self.Margin_percentage['Ex']}".ljust(20),
              f"{self.LT_Margin_percentage['Ex']}".ljust(20), f"{self.Cost_Sub_TER['Ex']}".ljust(30), f"{self.Rate_Per_Day['Ex']}".ljust(20), f"{self.Total_Expense['Ex']}")
        print('--------------------Dashboard--------------------\n')

    def print_detail(self):
        print('--------------------Financials--------------------')
        print('EY View'.ljust(40), 'In.Contingency'.ljust(30), 'Ex.Contingency')
        print('TER'.ljust(40), f"{self.TER['In']}".ljust(30), f"{self.TER['Ex']}")
        print('NER'.ljust(40), f"{self.NER['In']}".ljust(30), f"{self.NER['Ex']}")
        print('ERP%'.ljust(40), f"{self.ERP['In']}".ljust(30), f"{self.ERP['Ex']}")
        print('SER'.ljust(40), f"{self.SER['In']}".ljust(30), f"{self.SER['Ex']}")
        print('EAF'.ljust(40), f"{self.EAF['In']}".ljust(30), f"{self.EAF['Ex']}")
        print('Standard Cost'.ljust(40), f"{self.std_cost + self.lt_cost * (1+self.risk_level) - self.lt_cost}"
              .ljust(30), self.std_cost)
        print('Long Term Cost'.ljust(40), f"{self.Long_Term_Cost['In']}".ljust(30), f"{self.Long_Term_Cost['Ex']}")
        print('Cost of Subcontractors'.ljust(40), f"{self.Cost_of_Subcontractors['In']}".ljust(30), f"{self.Cost_of_Subcontractors['Ex']}")
        print('Margin%'.ljust(40), f"{self.Margin_percentage['In']}".ljust(30), f"{self.Margin_percentage['Ex']}")

        print('Margin'.ljust(40), f"{self.Margin['In']}".ljust(30), f"{self.Margin['Ex']}")
        print('LT Margin%'.ljust(40), f"{self.LT_Margin_percentage['In']}".ljust(30), f"{self.LT_Margin_percentage['Ex']}")
        print('LT Margin'.ljust(40), f"{self.LT_Margin['In']}".ljust(30), f"{self.LT_Margin['Ex']}")
        print('Standard Margin excl Partner Notional Costs (PNC) %'.ljust(50), f"{self.Std_Margin_excl_Partner_Cost_percentage['In']}".ljust(30), f"{self.Std_Margin_excl_Partner_Cost_percentage['Ex']}")
        print('Long Term Margin excl Partner Notional Costs (PNC) %'.ljust(50), f"{self.LT_Margin_excl_Partner_Cost_percentage['In']}".ljust(30), f"{self.LT_Margin_excl_Partner_Cost_percentage['Ex']}")
        print('Cost of Subcontractors/TER'.ljust(40), f"{round(self.Cost_of_Subcontractors['In']/self.TER['In'], 2)}".ljust(30), f"{round(self.Cost_of_Subcontractors['Ex']/self.TER['Ex'], 2)}")
        print('Total Expenses'.ljust(40), f"{self.Total_Expense['In']}".ljust(30), f"{self.Total_Expense['Ex']}")
        if self.onshore_type_hours == 0:
            print('Rate per Day- EY Onshore'.ljust(40), '0.0'.ljust(30), 0.0)
        else:
            print('Rate per Day- EY Onshore'.ljust(40), f"{round(self.NER['In'] * (self.onshore_type_SER * (1 + self.risk_level) / self.SER['In']) / (self.onshore_type_hours / 8), 2)}".ljust(30), f"{round(self.NER['Ex'] * (self.onshore_type_SER / self.SER['Ex']) / (self.onshore_type_hours / 8), 2)}")
        if self.GDS_type_hours == 0:
            print('Rate per Day- GDS'.ljust(40), '0.0'.ljust(30), 0.0)
        else:
            print('Rate per Day- GDS'.ljust(40), f"{round(self.NER['In'] * (self.GDS_type_SER / self.SER['In']) / (self.GDS_type_hours / 8), 2)}".ljust(30), f"{round(self.NER['Ex'] * (self.GDS_type_SER / self.SER['Ex']) / (self.GDS_type_hours / 8), 2)}")
        print('Rate per Day-Overall'.ljust(40), f"{self.Rate_Per_Day['In']}".ljust(30), f"{self.Rate_Per_Day['Ex']}")
        print('Rate per Hours-Overall'.ljust(40), f"{round(self.Rate_Per_Day['In'] / 8, 2)}".ljust(30), f"{round(self.Rate_Per_Day['Ex'] / 8, 2)}")
        print('Current FYTER(CYTR)'.ljust(40), f"{round(self.TER['In'] * self.first_year_revenue * 0.01, 2)}".ljust(30), f"{round(self.TER['Ex'] * self.first_year_revenue * 0.01, 2)}")
        print('--------------------Financials--------------------\n')

        print('--------------------Impact of Technology - Pilot Products--------------------\n')
        print('Type'.ljust(30), 'Labour'.ljust(30), 'Technology - Pilot Products'.ljust(30), 'Total')
        print('Billings (TER)'.ljust(30), f"{self.TER['In']}".ljust(30), f"{self.TP_type_revenue}".ljust(30),
              f"{round(self.TER['In'] + self.TP_type_revenue, 2)}")
        print('Expenses (CAEs)'.ljust(30), f"{self.Total_Expense['In']}".ljust(30), "0.00".ljust(30),
              f"{self.Total_Expense['In']}")
        print('Revenue (ANSR / NER)'.ljust(30), f"{self.NER['In']}".ljust(30), f"{self.TP_type_revenue}".ljust(30),
              f"{round(self.NER['In'] + self.TP_type_revenue, 2)}")
        print('ST Cost'.ljust(30), f"{round(self.std_cost * (1 + self.risk_level), 2)}".ljust(30),
              f"{round(self.total_technology_TP, 2)}".ljust(30),
              f"{round(self.std_cost * (1 + self.risk_level) + self.total_technology_TP, 2)}")
        print('ST Margin'.ljust(30), f"{round(self.NER['In'] - self.std_cost * (1 + self.risk_level) , 2)}".ljust(30),
              f"{round(self.TP_type_revenue - self.total_technology_TP, 2)}".ljust(30),
              f"{round((self.NER['In'] + self.TP_type_revenue) - (self.std_cost * (1 + self.risk_level) + self.total_technology_TP), 2)}")
        print('ST Margin%'.ljust(30), f"{self.Margin_percentage['In']}".ljust(30),
              f"{'{:.2%}'.format(1 - self.total_technology_TP / self.TP_type_revenue)}".ljust(30),
              f"{'{:.2%}'.format(1 - (self.std_cost * (1 + self.risk_level) + self.total_technology_TP) / (self.NER['In'] + self.TP_type_revenue))}")
        print('LT Cost'.ljust(30), f"{round(self.lt_cost * (1 + self.risk_level), 2)}".ljust(30),
              f"{round(self.total_technology_TP, 2)}".ljust(30),
              f"{round(self.lt_cost * (1 + self.risk_level) + self.total_technology_TP, 2)}")
        print('LT Margin'.ljust(30), f"{round(self.NER['In'] - self.lt_cost * (1 + self.risk_level), 2)}".ljust(30),
              f"{round(self.TP_type_revenue - self.total_technology_TP, 2)}".ljust(30),
              f"{round((self.NER['In'] - self.lt_cost * (1 + self.risk_level)) + (self.TP_type_revenue - self.total_technology_TP), 2)}")
        print('LT Margin%'.ljust(30), f"{self.LT_Margin_percentage['In']}".ljust(30),
              f"{'{:.2%}'.format(1 - self.total_technology_TP / self.TP_type_revenue)}".ljust(30),
              f"{'{:.2%}'.format(1 - (self.lt_cost * (1 + self.risk_level) + self.total_technology_TP) / (self.NER['In'] + self.TP_type_revenue))}")
        print('--------------------Impact of Technology - Pilot Products--------------------\n')

        print('--------------------Effort Summary and Ratios( Incl. Subcontractors)--------------------\n')
        print('Rank'.ljust(30), 'Hours'.ljust(30), 'Percentage')
        print('Partner'.ljust(30), f"{self.partner_hours}".ljust(30), f"{self.partner_proportion}")
        print('Executive Director'.ljust(30), f"{self.director_hours}".ljust(30), f"{self.director_proportion}")
        print('Senior Manager'.ljust(30), f"{self.senior_manager_hours}".ljust(30), f"{self.senior_manager_proportion}")
        print('Manager'.ljust(30), f"{self.manager_hours}".ljust(30), f"{self.manager_proportion}")
        print('Senior'.ljust(30), f"{self.senior_hours}".ljust(30), f"{self.senior_proportion}")
        print('Staff'.ljust(30), f"{self.staff_hours}".ljust(30), f"{self.staff_proportion}")
        print('Intern'.ljust(30), f"{self.intern_hours}".ljust(30), f"{self.intern_proportion}")
        print('Individual Contractor'.ljust(30), f"{self.contractor_hours}".ljust(30), f"{self.contractor_proportion}")
        print('Subcontractor'.ljust(30), f"{self.subcontractor_hours}".ljust(30), f"{self.subcontractor_proportion}")
        print('GDS'.ljust(30), f"{self.GDS_hours}".ljust(30), f"{self.GDS_proportion}")
        print('CBS'.ljust(30), f"{self.CBS_hours}".ljust(30), f"{self.CBS_proportion}")
        print('Total'.ljust(30), f"{self.total_working}".ljust(30), '100.00%\n')
        print('Specifics'.ljust(30), 'Values')
        print('Partner + ED as % of Total Hours'.ljust(30),
              f"{'{:.2%}'.format((self.partner_hours + self.director_hours) / self.total_working)}")
        print('Leverage Ratio'.ljust(30),
              f"{round((self.total_working - self.partner_hours - self.subcontractor_hours) / self.partner_hours, 2)}")
        print('Onshore Efforts %'.ljust(30),
              f"{'{:.2%}'.format(self.onshore_type_hours / self.total_working, 2)}")
        print('Contractor Efforts %'.ljust(30),
              f"{'{:.2%}'.format(self.contractor_hours / self.total_working, 2)}")
        print('Subcontractor Efforts %'.ljust(30),
              f"{'{:.2%}'.format(self.subcontractor_hours / self.total_working, 2)}")
        print('--------------------Effort Summary and Ratios( Incl. Subcontractors)--------------------\n')

        print('--------------------Recovery of Expenses Incurred Through Target Price (Ex.Contingency)--------------------')
        print('Rank'.ljust(30), 'Incurred'.ljust(30), 'Recoverable'.ljust(30), 'Non-Recoverable')
        print('Lead SMU (Own Expenses)'.ljust(30),
              f"{self.LS_expense_incuured}".ljust(30),
              f"{self.LS_expense_client}".ljust(30),
              f"{self.LS_expense_unexpense}")
        print('Inter-firm'.ljust(30),
              f"{self.IF_expense_incuured}".ljust(30),
              f"{self.IF_expense_client}".ljust(30),
              f"{self.IF_expense_unexpense}")
        print('Technology - other products'.ljust(30),
              f"{self.TOP_expense_incuured}".ljust(30),
              f"{self.TOP_expense_client}".ljust(30),
              f"{self.TOP_expense_unexpense}")
        print('Vendor/Subcontractor (FF)'.ljust(30),
              f"{self.VS_expense_incuured}".ljust(30),
              f"{self.VS_expense_client}".ljust(30),
              f"{self.VS_expense_unexpense}")
        print('Other Lump Sums'.ljust(30),
              f"{self.OLS_expense_incuured}".ljust(30),
              f"{self.OLS_expense_client}".ljust(30),
              f"{self.OLS_expense_unexpense}")
        print('Total price'.ljust(30),
              f"{self.LS_expense_incuured + self.TOP_expense_incuured + self.IF_expense_incuured +self.VS_expense_incuured + self.OLS_expense_incuured}".ljust(30),
              f"{self.LS_expense_client + self.TOP_expense_client + self.IF_expense_client +self.VS_expense_client + self.OLS_expense_client}".ljust(30),
              f"{self.LS_expense_unexpense + self.TOP_expense_unexpense + self.IF_expense_unexpense +self.VS_expense_unexpense + self.OLS_expense_unexpense}".ljust(30))
        print(
            '--------------------Recovery of Expenses Incurred Through Target Price (Ex.Contingency)--------------------')