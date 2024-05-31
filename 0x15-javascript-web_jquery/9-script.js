$(function(){
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data, Status){
		data.code = 'en';
		$('#hello').text(data.hello);
	});
});
