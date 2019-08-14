一. 安装unrar
1. windows
下载rarlib的库文件，地址：http://www.rarlab.com/rar/UnRARDLL.exe（压缩包中已经下载完，直接使用即可）
下载安装，默认设置
设置环境变量：UNRAR_LIB_PATH  :   C:\Program Files (x86)\UnrarDLL\x64\unrar.dll  (注意：64位在x64文件夹下，将unrar大写改为小写)
设置完环境变量后重启Pycharm

2. Linux
下载地址：http://www.rarlab.com/rar/unrarsrc-5.4.5.tar.gz （压缩包中已经下载完，直接使用即可）
下载后解压：
wu@ubuntu:~$ tar zxvf unrarsrc-5.4.5.tar.gz
wu@ubuntu:~$ cd unrar/
wu@ubuntu:~/unrar$ ls
wu@ubuntu:~/unrar$ make lib  //编译库文件
wu@ubuntu:~/unrar$ sudo make install-lib  //生成libunrar.so 文件
配置环境变量：
sudo vim /etc/profile  添加：export UNRAR_LIB_PATH=/usr/lib/libunrar.so  生效：source /etc/profile


二：代码说明：
通过传入文件物理路径后进行解析，将rar文件解压后过滤出doc/docx文件后根据文件名进行相似度匹配，只存储相似度最高的文件（最终删除临时文件）
