App性能测试：
研究但不仅限于研究启动时间、内存、CPU、流量、电量（功耗）。

获取App包名和Activity：
打开App里输入adb命令获取（windows用findstr）
Package name：adb shell dumpsys window w | grep \/ | grep name=
Activity： adb shell dumpsys activity | grep mFocusedActivity
