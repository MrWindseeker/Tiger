class Resource:

    # def __init__(self, working_hours, bill_rate, cost_rate, nsr_rate, rank_type=None):
    #     '''
    #
    #     :param working_hours:
    #     :param std_billing_rate:
    #     :param std_cost_rate:
    #     :param net_std_revenue_rate:
    #     :param rank_type: MMT Rank
    #         {
    #             partner、director、contractor、subcontractor、senior、manager、senior_manager、staff
    #             intern、GDS、CBS
    #         }
    #     '''
    #     self.working_hours = working_hours
    #     self.bill_current_rate = bill_rate[0]
    #     self.bill_next_rate = bill_rate[1]
    #     self.bill_nnext_rate = bill_rate[2]
    #     self.bill_manual_rate = bill_rate[3]
    #     self.cost_std_current_rate = cost_rate[0]
    #     self.cost_std_next_rate = cost_rate[1]
    #     self.cost_std_nnext_rate = cost_rate[2]
    #     self.cost_lt_current_rate = cost_rate[3]
    #     self.cost_lt_next_rate = cost_rate[4]
    #     self.cost_lt_nnext_rate = cost_rate[5]
    #     self.nsr_current_rate = nsr_rate[0]
    #     self.nsr_next_rate = nsr_rate[1]
    #     self.nsr_nnext_rate = nsr_rate[2]
    #     self.SER = 0.0
    #     self.Std = 0.0
    #     self.LT_Cost = 0.0
    #     self.NSR_Cost = 0.0
    #     self.Total_Expenses = 0.0
    #     self.rank_type = rank_type
    #     self.current_hours = self.working_hours[0]
    #     self.next_hours = self.working_hours[1]
    #     self.nnext_hours = self.working_hours[2]
    #
    # def check_resource(self):
    #     self.SER = round(self.bill_current_rate * self.current_hours + self.bill_next_rate * self.next_hours + \
    #                self.bill_nnext_rate * self.nnext_hours, 2)
    #     self.Std = round(self.cost_current_rate * self.current_hours + self.cost_next_rate * self.next_hours + \
    #                self.cost_nnext_rate * self.nnext_hours, 2)
    #     self.LT_Cost = round(self.cost_current_rate * self.current_hours + self.cost_next_rate * self.next_hours + \
    #                self.cost_nnext_rate * self.nnext_hours, 2)

    def __init__(self, working_hours, SER, Std, LT_Cost, NSR_Cost, total_expense, rank_type, source_type):
        '''
        rank_type : partner、director、contractor、subcontractor、senior、manager、senior_manager、staff、intern、GDS、CBS
        source_type : EY_Onshore、GDS、Subcontractors
        '''
        self.working_hours = working_hours
        self.total_expense = total_expense
        self.rank_type = rank_type

        self.NSR_Cost = NSR_Cost
        self.SER = SER
        self.Std = Std
        self.LT_Cost = LT_Cost
        self.source_type = source_type


