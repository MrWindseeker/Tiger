from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.Conf import ConfigYaml
from utils.EmailUtil import EmailUtil
# 初始化配置文件
conf_read = ConfigYaml()

app = FastAPI()

class EmailRequest(BaseModel):
    subject: Optional[str] = None
    text_cont: Optional[str] = None
    html_cont: Optional[str] = None
    html_img: Optional[List[str]] = None
    attach_file: Optional[List[str]] = None

@app.post("/send_email")
def send_email_api(req: EmailRequest):
    try:
        email_info = conf_read.get_email_info()
        email = EmailUtil(email_info)
        email.send_email(
            subject = req.subject,
            text_cont = req.text_cont,
            html_cont = req.html_cont,
            html_img = req.html_img,
            attach_file = req.attach_file
        )
        return {"message": "邮件发送成功"}
    except Exception as e:
        return {"error": str(e)}