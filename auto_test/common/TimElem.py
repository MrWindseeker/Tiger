class TimElem:
    # [Look Up]
    # 输入框元素
    Time_Type_input = "//*[text()='Time Type:']/../div[1]/div[1]/div[1]/input"
    Type_input = "//*[text()='Type:']/../div[1]/div[1]/div[1]/input"
    Engagement_input = "//*[text()='Engagement:']/../div[1]/div[1]/div[1]/input"
    Activity_input = "//*[text()='Activity:']/../div[1]/div[1]/div[1]/input"
    Description_input = "//*[text()='Description:']/../div[1]/div[1]/div[1]/input"
    Loc1_input = "//*[text()='Loc1:']/../div[1]/div[1]/div[1]/input"
    Loc2_input = "//*[text()='Loc2:']/../div[1]/div[1]/div[1]/input"
    Task_Type_input = "//*[text()='Task Type:']/../div[1]/div[1]/div[1]/input"
    OT_Approver_EM_input = "//*[text()='OT Approver-EM:']/../div[1]/div[1]/div[1]/input"
    OT_Approver_EP_input = "//*[text()='OT Approver-EP:']/../div[1]/div[1]/div[1]/input"
    Submit_btn = "//*[text()='OK']/.."

    # [home_page]
    Current_Week_Timesheet = "//*[text()='Current Week Timesheet']"

    # [timesheet]
    # 所有icon按钮，使用xpath方式find_elements查找，取最后一个操作
    last_tr_engcode = "//*[@class='iconfont icon-sousuo']"

    add_project = "//*[@class='box current-timesheet']/div[1]/div/div/div/div[2]/span[1]"
    delete_project = "//*[@class='box current-timesheet']/div[1]/div/div/div/div[2]/span[2]"
    select_all = "//*[@class='box current-timesheet']/div[1]/div/div/form/div/div[2]/table/thead/tr/th[1]/div/label/span/input"
    submit_btn2 = "//button[@class= 'el-button el-button--default el-button--mini']"
    Submit_btn1 = "//*[text()='Submit Timesheet']/.."
    Save_btn = "//*[text()='Save Timesheet']/.."
    submit_alert = "//*[@class = 'el-message el-message--success is-center is-closable']/p"