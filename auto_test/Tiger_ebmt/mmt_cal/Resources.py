class Resource:

    def __init__(self, working_hours, ot_hours, std_billing_rate, std_cost_rate, net_std_revenue_rate, rank_type=None):
        '''

        :param working_hours:
        :param ot_hours:
        :param std_billing_rate:
        :param std_cost_rate:
        :param net_std_revenue_rate:
        :param rank_type: MMT Rank
            {
                partner、contractor、subcontractor、senior、manager、senior_manager、staff
                intern、GDS、CBS
            }
        '''
        self.working_hours = working_hours
        self.ot_hours = ot_hours
        self.std_billing_rate = std_billing_rate
        self.std_cost_rate = std_cost_rate
        self.net_std_revenue_rate = net_std_revenue_rate
        self.SER = self.std_billing_rate * (self.working_hours + self.ot_hours)
        self.std_cost = self.std_cost_rate * (self.working_hours + self.ot_hours)
        self.NSR = self.net_std_revenue_rate * (self.working_hours + self.ot_hours)
        self.rank_type = rank_type

