define(function(require, exports, module){
	var Event = require('./addEvent.js');
	var _timer, _move = function(ele, to, from){
		from = from || 0;
		if(Math.abs(to-from)>2){
			ele.style.marginTop = (to-(to-from)/3) + "px";
			/*_timer = setTimeout(function(){
				_move(ele,to);
			},);*/
		}else{
			ele.style.marginTop = to + 'px';
		}
	};
	return{
		index:0,
		visible:5,
		init:function(box){
			var self = this,
			length = box.getElementsByClassName('navdiv').length;

			document.getElementById(self.index+2).style.fontSize = "56px";
			document.getElementById(self.index+1).style.fontSize = "32px";
			document.getElementById(self.index).style.fontSize = '18px';
			document.getElementById(self.index+3).style.fontSize = "32px";
			document.getElementById(self.index+4).style.fontSize = "18px";
			//console.log(length);
			Event.addEvent(box.parentNode,"mousewheel",function(event){
				if(event.delta > 0 && self.index >0){
					self.index --;
				}else if(event.delta < 0 && self.index < length - self.visible){
					self.index ++;
				}else{
					return;
				}
				document.getElementById(self.index+2).style.fontSize = "56px";
				document.getElementById(self.index+1).style.fontSize = "32px";
				document.getElementById(self.index).style.fontSize = '18px';
				document.getElementById(self.index+3).style.fontSize = "32px";
				document.getElementById(self.index+4).style.fontSize = "18px";
				_move(box,-1*self.index*200);
				console.log(self.index);


				event.preventDefault();
			});
		}
	};
});