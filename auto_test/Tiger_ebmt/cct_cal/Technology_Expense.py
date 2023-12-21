class Technology:

    def __init__(self, Category, Recoverable, Revenue, total_cost):
        '''
            Category: 技术费用类型
                {
                    Technology - Pilot Products: TP,
                    Vendor/Subcontractor (FF) : VS,
                    Technology - Other Products : TOP,
                    Other Lumpsum : OLS
                }
            Recoverable: Yes or No
        '''
        self.Recoverable = Recoverable
        self.Category = Category
        self.total_cost = total_cost
        self.Revenue = Revenue
