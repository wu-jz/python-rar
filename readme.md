# python-unrar 安装
## 1. windows
1.下载rarlib的库文件，地址：http://www.rarlab.com/rar/UnRARDLL.exe </br>
2.下载安装，默认设置</br>
3.设置环境变量：UNRAR_LIB_PATH  :   C:\Program Files (x86)\UnrarDLL\x64\unrar.dll  (注意：64位在x64文件夹下，将unrar大写改为小写)</br>
4.设置完环境变量后重启Pycharm</br>

## 2. linux
1. 下载地址：http://www.rarlab.com/rar/unrarsrc-5.4.5.tar.gz </br>
2. 下载后解压：(操作如下) </br>
  (1) tar zxvf unrarsrc-5.4.5.tar.gz </br>
  (2) cd unrar/ </br>
  (3) make lib  //编译库文件 </br>
  (4) sudo make install-lib  //生成libunrar.so 文件 </br>
3. 配置环境变量：</br>
  (1) sudo vim /etc/profile 
  (2) export UNRAR_LIB_PATH=/usr/lib/libunrar.so  
  (3) source /etc/profile
  
# 代码说明
通过传入文件物理路径后进行解析，将rar文件解压后过滤出doc/docx文件后根据文件名进行相似度匹配，只存储相似度最高的文件（最终删除临时文件）
