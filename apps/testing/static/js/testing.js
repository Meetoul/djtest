$(function(){
	var id = 1
	$("#btn1").click(function(){
		console.log($("input[name=answer]:checked").val())
		$("#btn1").html('Answer')
		id++;
		$.get('question', {'test_id': $("#test_id").text(), 'question_id': id},
            function(data) {
                    if(data == '-1'){
                    	$("#choices").html('')
                    	$("#question_text").html('You answered all the questions')
                    } else {
                    	$("#question_text").html(data.text)
                    	var choices_html = ''
                    	data.choices.forEach(function(entry){
                    		choices_html += '<input type="radio" name="answer" value="' + entry.id + '">'
                    		 + entry.text + '<br>' 
                    	});
                    	$("#choices").html(choices_html)
                    }
            });
	});
});