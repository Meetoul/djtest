$(function(){
	$('#questions-form').submit(function() {
		if($('div.question:not(:has(:radio:checked))').length){
			alert('Answer all questions please!');
			return false;
		}
		return true;
	});
});