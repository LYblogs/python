###Pygame  

Pygame有很多的模块，不同的模块专注于不同的功能：  

|模块名                |功能                |   
|---------------------|--------------------------|
|pygame.cdrom         |访问光驱|  
| pygame.cursors |加载光标|  
|pygame.display|访问显示设备|
|pygame.draw|绘制形状、线和点|
|pygame.event|管理事件|
|pygame.font|使用字体|
|pygame.image|加载和存储图片|
|pygame.joystick|使用游戏手柄或者 类似的东西|
|pygame.key|读取键盘按键|
|pygame.mixer|声音|
| pygame.mouse |鼠标|
| pygame.movie |播放视频|
| pygame.music |播放音频|
|pygame.overlay|访问高级视频叠加|
| pygame.rect |管理矩形区域|
| pygame.sndarray |操作声音数据|
|pygame.sprite|操作移动图像|
|pygame.surface|管理图像和屏幕|
| pygame.surfarray |管理点阵图像数据|
| pygame.time |管理时间和帧信息|
|pygame.transform|缩放和移动图像|    


####disolay模块
下面主要介绍一下display模块的一些常用方法：     
#####1.set_model 生成windows窗口
 
	pygame.display.set_model(resolution, flags, depth)  
	
resolution：可以控制生成的window的大小。传的值：(100,200)这样的  
flags：控制你想要怎样的显示屏，可以赋一下几个全局常量。（这些常量在pygame.locals模块中）    


|||
|----|---|
|FULLSCREEN|控制全屏,0或者1来控制|
|HWSURFACE|控制是否进行硬件加速 |
|RESIZABLE|控制窗口是否可以调节大小 |
|NOFRAME|创建一个没有边框的窗口|

	
depth：不推荐设置    

#####2.get_caption()获得窗口的标题  

	pygame.display.get_caption()  
	
#####3.set_caption(title)设置窗口的标题  

	pygame.display.set_caption(title)  
	
	
####事件  

|事件|产生途径| 参数|   
|-------|--------|-----| 
| QUIT |用户按下关闭按钮| none |
| ATIVEEVENT |Pygame被激活或者隐藏|gain, state|
| KEYDOWN |键盘被按下|unicode, key, mod|
| KEYUP |键盘被放开|key, mod|  
| MOUSEMOTION |鼠标移动|pos, rel, buttons|
|MOUSEBUTTONDOWN|鼠标按下|pos, button|
| MOUSEBUTTONUP |鼠标放开|pos, button|
| USEREVENT |触发了一个用户事件| code |



	



	



  
 
		
