# coding=UTF-8
"""
用字典暴力破解ZIP压缩文件密码
"""
import zipfile
import threading


#  定义一个判断密码是否正确的函数
def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password.encode())
        print("Found Passwd : ", password)
        return password
    except Exception:
        # 异常处理
        pass


def main():
    # 指定要爆破的压缩文件
    zFile = zipfile.ZipFile(input("请输入你要爆破的压缩文件，例：C:\\a.zip\n"))
    # 指定要使用的字典文件
    dictfile = input("请输入要使用的字典文件，输入0则使用默认字典\n")
    if dictfile == '0':
        dictfile = "pwd.txt"
    passFile = open(dictfile)
    for line in passFile.readlines():  # 逐行读取字典文件
        password = line.strip('\n')  # 删除多余的换行
        t = threading.Thread(target=extractFile, args=(zFile, password))  # 创建线程
        t.start()  # 开启线程
        guess = extractFile(zFile, password)  # 尝试每一行读取的密码
        if guess:  # 成功读取
            print('Password = ', password)
            return
        else:
            continue
    print("password not found")


if __name__ == '__main__':
    main()
