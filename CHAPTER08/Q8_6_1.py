from datetime import datetime
tim = "20180105120130"
dat = datetime.strptime(tim, "%Y%m%d%H%M%S")
print(dat)
print(dat.strftime("%Y%m%d%H%M%S"))
