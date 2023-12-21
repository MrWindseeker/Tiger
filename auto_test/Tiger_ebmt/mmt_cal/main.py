import Expenses
import Resources
import Summary

# 生成resource信息
rs1 = Resources.Resource(24, 0, 9950, 2887, 4470, rank_type='partner')
rs2 = Resources.Resource(24, 0, 0, 1000, 0, rank_type='contractor')
# 生成Expense信息
exp = Expenses.Expenses(34000, 0, 34000)
# 生成Summary信息
sumry = Summary.Summary(1000000, 10, tax='Incl.Tax')
# 往Summary里添加resource和Expense信息
sumry.add_resource(rs1)
sumry.add_resource(rs2)
sumry.add_expense(exp)
# summary开始计算
sumry.check_resource_expense()

# 打印总览信息
sumry.print_dashbord()
# 打印detail信息
sumry.print_detail()