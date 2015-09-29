function highlight(evt){
			targetTag = $(evt.currentTarget).data().id;
			targetClass = '.all-'+targetTag;
			$("*").css('background-color', "");
			$(targetClass).css('background-color', '#59CDFF');
			$(this).css('background-color', '#59CDFF');
			$(this).next().css('background-color', '#59CDFF');
		}

$('.tag').click(highlight);