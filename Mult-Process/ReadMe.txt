程序是用于爬取pente.org的多线程爬虫。
本身用于爬取pente.org的时候由于单线程速度慢，所以在大量目标下效果不理想。
多线程操作不熟悉，可能导致程序中变量冲突，因此在资源充足的条件下选择采用多进程爬虫。
此处多进程不是多开Python，而是选择开启子进程（subprocess）
主进程的pid可以方便地获取，在每个子进程运行的函数里面也可以方便地获取子进程的pid
通过设置步长和进程数，可以有效提高速度。
经过检验，在资源足够使用的条件下，爬虫的效率极大提升。原计划需要超过55小时的任务，此处运行半数条目需要的时间不超过3小时，总提升效率接近十倍。
使用时需要自己填写注册用户名密码
