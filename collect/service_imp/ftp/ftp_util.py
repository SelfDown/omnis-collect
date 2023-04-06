# -*- coding: utf-8 -*-
"""
ftp 操作

:param param1: this is a first param
:param param2: this is a second param
:returns: this is a description of what is returned
:raises keyError: raises an exception
@author： jhuang
@time：27/02/2018
"""
import time
from ftplib import FTP


def get_FileSize(filePath):
    import os
    # filePath = unicode(filePath, 'utf8')
    fsize = os.path.getsize(filePath)
    # fsize = fsize / float(1024)
    return round(fsize, 2)


class FtpUploadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize):
        self.totalSize = totalSize

    def handle(self, block):
        upload_size = float(self.sizeWritten + len(block))
        value = upload_size / self.totalSize * 100
        text = format(upload_size / self.totalSize * 100, '.2f') + '%'
        self.sizeWritten = upload_size
        print text


class FtpUtil(object):
    def __init__(self, set_debuglevel=0):
        self.host = None
        self.username = None
        self.password = None
        self.ftp_con = None
        self.set_debuglevel = set_debuglevel
        self.bufsize = 1024

        self.sizeWritten = 0
        self.totalSize = 0
        self.lastShownPercent = 0
        self.percentage = ''
        self.time1 = None
        self.count_tmp = 0
        self.speed = 0
        self.status = ""
        self.small = False
        self.action = "正在上传"

    def connect(self, host, username, password, port=21):
        self.ftp_con = FTP()
        self.ftp_con.set_debuglevel(self.set_debuglevel)  # 打开调试级别2，显示详细信息
        self.ftp_con.connect(host, port)  # 连接
        self.ftp_con.login(username, password)  # 登录，如果匿名登录则用空串代替即可

    def upload(self, remote_path, local_path):
        fp = open(local_path, 'rb')
        self.ftp_con.set_debuglevel(self.set_debuglevel)
        # totalSize = get_FileSize(localpath)
        # uploadTracker = FtpUploadTracker(int(totalSize))
        # self.ftp_con.storbinary('STOR ' + remotepath, fp, self.bufsize, uploadTracker.handle)  # 上传文件
        self.totalSize = get_FileSize(local_path)
        self.time1 = time.time()
        self.action = "正在上传"
        self.ftp_con.storbinary('STOR ' + remote_path, fp, self.bufsize, self.handle)
        fp.close()

    def download(self, remote_path, local_path):
        self.ftp_con.set_debuglevel(self.set_debuglevel)
        self.ftp_con.voidcmd('TYPE I')
        self.totalSize = self.ftp_con.size(remote_path)
        # self.ftp_con.voidcmd('TYPE a')
        self.time1 = time.time()
        self.action = "正在下载"
        fp = open(local_path, 'wb')

        def file_write(data):
            fp.write(data)
            self.handle(data)

        self.ftp_con.retrbinary('RETR ' + remote_path, file_write, self.bufsize, )
        # self.ftp_con.retrbinary('RETR ' + remotepath, fp.write, self.bufsize)
        fp.close()

    def delete(self, filename):
        res = self.ftp_con.delete(filename)
        return res

    def mkd(self, filename):
        res = self.ftp_con.mkd(filename)
        return res

    def ftp_makedirs_cwd(self,path, first_call=True):
        """设置“FTP”中给出的FTP连接的当前目录
    参数(如ftplib)。)，不存在创建所有父目录
    。ftplib对象必须已经连接并登录
        """

        ftp=self.ftp_con
        try:
            ftp.cwd(path)
        except Exception as e:
            import os
            self.ftp_makedirs_cwd(os.path.dirname(path), False)
            ftp.mkd(path)
            if first_call:
                ftp.cwd(path)

    def handle(self, block):
        upload_size = float(self.sizeWritten + len(block))
        # value = upload_size / self.totalSize * 100
        text = format(upload_size / self.totalSize * 100, '.2f')
        self.sizeWritten = upload_size
        # print text
        self.percentage = text
        cal_time = 2
        if self.totalSize < 1024 * 1024 * 5:
            self.small = True
            cal_time = 0.1
            unit = "KB"
            unit_total = 1024
        else:
            cal_time = 1
            unit = "M"
            unit_total = 1024 * 1024

        # if time.time() - self.time1 > cal_time:  # 计算网速
        #     from backend.utils.http_util import formatFloat
        #     self.speed = formatFloat(float(self.sizeWritten - self.count_tmp) / unit_total / cal_time)
        #     self.count_tmp = self.sizeWritten
        #     self.time1 = time.time()
        #
        #     self.status = " %s %s(%s)/%s(%s) 进度 %s %% 网速 %s (%s/s)" % (self.action,
        #                                                                self.sizeWritten / unit_total,
        #                                                                unit,
        #                                                                self.totalSize / unit_total,
        #                                                                unit,
        #                                                                self.percentage,
        #                                                                self.speed,
        #                                                                unit
        #                                                                )

    def quit(self):
        """
        退出FTP连接

        :param param1: this is a first param
        :param param2: this is a second param
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        @author： jhuang
        @time：27/02/2018
        """
        self.ftp_con.quit()
