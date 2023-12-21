import Resources
import Expenses
import Summary
import Technology_Expense

# C23000943V1 测试数据

# 初始化 resource数据
rs1 = Resources.Resource(6, 477600, 138576, 138576, 214560, 8500, rank_type='partner', source_type='EY_Onshore')
rs2 = Resources.Resource(6, 71520, 10464, 10464, 16608, 0, rank_type='senior', source_type='EY_Onshore')
rs3 = Resources.Resource(6, 0, 12000, 0, 0, 0, rank_type='subcontractor', source_type='Subcontractors')
rs4 = Resources.Resource(6, 12000, 1200, 1200, 5856, 0, rank_type='intern', source_type='EY_Onshore')
rs5 = Resources.Resource(6, 71520, 10464, 10464, 16608, 0, rank_type='senior', source_type='EY_Onshore')

# 初始化技术费用数据
t_expense1 = Technology_Expense.Technology('TP', 'Yes', 12, 111000)
t_expense2 = Technology_Expense.Technology('VS', 'No', 0,  200000)
t_expense3 = Technology_Expense.Technology('OLS', 'Yes', 0,  300000)
t_expense4 = Technology_Expense.Technology('TOP', 'No', 0,  200000)
t_expense5 = Technology_Expense.Technology('TOP', 'Yes', 0,  50000)
t_expense6 = Technology_Expense.Technology('VS', 'Yes', 0,  70000)

# 初始化费用数据
expense1 = Expenses.Expenses('LS', 24250, 2000, 22250)
expense2 = Expenses.Expenses('IF', 0, 0, 0)

# 初始化summary 传入合同金额，回报率，风险值，计时单位
smary = Summary.Summary(10000000, 10, 5, working_type='Days')

# 把所有的resource、费用、技术费用都添加到summary中
smary.add_resource(rs1)
smary.add_resource(rs2)
smary.add_resource(rs3)
smary.add_resource(rs4)
smary.add_resource(rs5)
smary.add_expense(expense1)
smary.add_expense(expense2)
smary.add_technology_expense(t_expense1)
smary.add_technology_expense(t_expense2)
smary.add_technology_expense(t_expense3)
smary.add_technology_expense(t_expense4)
smary.add_technology_expense(t_expense5)
smary.add_technology_expense(t_expense6)

# 计算summary
smary.check_resource()

# 打印
smary.print_dashboard()
smary.print_detail()
