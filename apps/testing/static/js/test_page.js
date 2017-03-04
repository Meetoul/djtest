$(function(){
	var curr = 0;
	var answers = {};
	$.get('get_questions', function(data)
	{
		var questions = data.questions;
		fill(questions[curr]);
		$("#progress").html((curr + 1) + '/' + questions.length)
		$("#ans-btn").click(function(){
			if(!$('[name=answer]:checked').length)
			{
				$("#error").html('You have not answered yet!');
			} else if (curr < questions.length - 1) {
				$("#error").empty();
				processAnswer(questions[curr].id, answers);
				curr++;
				$("#progress").html((curr + 1) + '/' + questions.length)
				fill(questions[curr]);
			} else {
				processAnswer(questions[curr].id, answers);
				$("#question_text").html('You answered all the questions!');
				$("#choices").empty();
				params = $.param({
					answers: JSON.stringify(answers)
				});
				$("#ans-btn").hide();
				$("#result-link").prop("href", "result?" + params);
				$("#result-link").show();
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