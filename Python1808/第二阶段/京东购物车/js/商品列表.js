$(function(){
	//请求商品数据
	$.get('http://rap2api.taobao.org/app/mock/121189/goods',function(re){
		var goodsArray = re['goods']
		console.log(goodsArray)
		for(var x in goodsArray){
			var goods =goodsArray[x];
			//创建标签
			var trNode =$('<tr></tr>')
			//全选
			trNode.append($('<td><input type="checkbox"/></td>'));
			//商品
			trNode.append($('<td><img id="img0" src="'+goods['img']+'"/><font id="font0">'+goods['desc']+'</font></td>'))
			//单价
			trNode.append($('<td>'+'￥'+goods['price']+'</td>'))
			//数量
			trNode.append($('<td><button>-</button><input type="text" value="'+goods['num']+'"/>'+'<button>+</button>'+'</td>'))
			//小计
			var toal = Number(goods['price'])*Number(goods['num'])
			trNode.append($('<td>'+'￥'+toal+'</td>'))
			//删除
			trNode.append($('<td><button>删除</button></td>'))
			
			$('#goods').append(trNode)
		}
	})
	
	
	
})