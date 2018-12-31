
/*$(document).ready(function(){

	$('canvas').drawLine({
	  layer: true,
  	  name: 'myBox',
	  strokeStyle: '#FFF',
	  x1: 0, y1: 50,
	  x2: 0, y2: 50,
	  x3: 0, y3: 50,
	});

	// Animate layer properties
$('canvas')
.animateLayer('myBox', {

  x1: 0,    y1: 50,
  x2: 0,    y2: 50,
  x3: 800,  y3: 50,


}, 1500, function(layer) {
  // Callback function

});

}); */

$(function(){
	var inputs = $('.input');
	var paras = $('.description-flex-container').find('p');
	$(inputs).click(function(){
		var t = $(this),
				ind = t.index(),
				matchedPara = $(paras).eq(ind);
		
		$(t).add(matchedPara).addClass('active');
		$(inputs).not(t).add($(paras).not(matchedPara)).removeClass('active');
	});
});