var cityArray=['北京','上海','天津','重庆','河北','山西','河南',
'辽宁','吉林','黑龙江','内蒙古','江苏','山东','安徽','浙江','福建','湖北','湖南','广东',
'广西','江西','四川','海南','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆',
'港澳','台湾','钓鱼岛'];


$(function(){
	//城市对应的大盒子
	var cityBoxNode = $('.menu_bottom');
	for(var x in cityArray){
		//获取名字
		var cityName = cityArray[x]
		//创建节点
		var cityNode =$('<font class="city"></font>')
		//给节点添加内容（城市名）
		cityNode.text(cityName)
		cityBoxNode.append(cityNode);
		
	}
	//保存当前选中的城市
	var carrentCityNode =$('.menu_bottom font:first');
	carrentCityNode.css('background-color','red');
	carrentCityNode.css('color','white');
	
	
	//添加事件
		cityBoxNode.on('click','.city',function(){

			//修改名字
			var cityName =$(this).text();
			console.log(cityName)
			$('.menu_top font').text(cityName)
			
			//修改样式
			carrentCityNode.css('background-color','rgba(0,0,0,0)')
			carrentCityNode.css('color','#a0a0a0');
			carrentCityNode = $(this)
			carrentCityNode.css('background-color','red')
			carrentCityNode.css('color','white')
			
			//让盒子消失
			cityBoxNode.fadeOut();
			cityBoxNode.css('display','none')
			
			//
			cityBoxNode.parent().on('mouseover',function(){
				cityBoxNode.css('display','none')
			})
		})
	
});