$(function(){
	var curr = 0;
	var answers = {}
	$.get('get_questions', function(data)
	{
		var questions = data.questions;
		$("#start-btn").click(function(){
			fill(questions[curr]);
			$("#start-btn").hide();
			$("#ans-btn").show();
		});	
		$("#ans-btn").click(function(){
			if (curr < questions.length - 1){
				processAnswer(questions[curr].id, answers);
				curr++;
				fill(questions[curr]);
			} else {
				processAnswer(questions[curr].id, answers);
				$("#question_text").html('You answered all the questions!');
				$("#choices").html('');
				console.log(answers)
				$.get('get_result', {answers: JSON.stringify(answers)}, function(data){
					alert('Your result is: ' + data.result + '%')
				});
			}
		});
	});
});

function fill(question) {
	$("#question_text").html(question.text);
	var choices_html = '';
	question.choices.forEach(function(choice){
	choices_html += '<input type="radio" name="answer" value="' + choice.id + '">'
            		 + choice.text + '<br>' 
            		});
    $("#choices").html(choices_html)
}

function processAnswer(question_id, answers){
	answers[question_id] = $("input[name=answer]:checked").val();
}