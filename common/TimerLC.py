import threading
from bin import generatecase
from common.ReadAndWriteFilesbk import ReadAndWriteFiles
from common import EmailSend
import time
import os
from common.PgSql import deleteOperate
from common.report_screenshot import reportscreenshot
import datetime
import shutil
from common.ReadAndWriteFilesbk import ReadAndWriteFiles
from common import globalB
from common.others import alter_text

class TimerLM(object):
    @staticmethod
    def func():
        print("haha")
        # 如果需要循环调用，就要添加以下方法
        # delePG = deleteOperate()
        a1 = generatecase.Run()
        time.sleep(5)
        # b = ReadAndWriteFiles()
        # test_report = b.path_testreport()
        # report = generatecase.new_report(test_report)

        #替换服务器html,json
        a = ReadAndWriteFiles()
        shutil.copy( os.path.join(a.path_testreport(), "result" + ".json" ),os.path.join(globalB.Gdjango_static_path, "report" + ".json" ) )
        path = shutil.copy( os.path.join(a.path_testreport(), "result" + ".html" ),os.path.join(globalB.Gdjango_templates_path, "report" + ".html" ) )
        #替换服务器脚本
        new_str = '{% load staticfiles %}<script type="text/javascript" src="{% static "report.json" %}" charset="gbk"></script>'
        old_str = '<script type="text/javascript" src="result.json" charset="gbk"></script>'
        alter_text(path, old_str, new_str)

        #截图
        b = reportscreenshot()
        #发邮件
        EmailSend.sendmail(globalB.Gpng)

        # EmailSend.send_email(report)

if __name__ == "__main__":
    b = TimerLM.func()



