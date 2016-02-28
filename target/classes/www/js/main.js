jQuery(document).ready(function($){

    var atTop = !$(document).scrollTop();
    var timelineBlocks;



	//on scolling, show/animate timeline blocks when enter the viewport
	$(window).on('scroll', function(){
        if($(document).scrollTop() == 0 && !atTop ) {
            // do something
            $("#heading").remove();
            $("header").animate({
                 height:300},{
                complete: function() {
                    $("#headerImage").show()
                }});
            timelineBlocks = $('.cd-timeline-block'),
                offset = 0.8;
            hideBlocks(timelineBlocks, offset);
            atTop = true;
        }
        else if (atTop) {
            //$("header").empty();
            $("#headerImage").hide();
            $("header").animate({height:100});
            if(!$('#heading').length )         // use this if you are using id to check
            {
                $("header").append("<h1 id='heading' style='margin-top:-100px'>Prathyush SP - The Journey</h1>");
            }
            atTop = false;
        }


		(!window.requestAnimationFrame)
			? setTimeout(function(){ showBlocks(timelineBlocks, offset); }, 100)
			: window.requestAnimationFrame(function(){ showBlocks(timelineBlocks, offset); });
	});

	function hideBlocks(blocks, offset) {
		blocks.each(function(){
			( $(this).offset().top > $(window).scrollTop()+$(window).height()*offset ) && $(this).find('.cd-timeline-img, .cd-timeline-content').addClass('is-hidden');
		});
	}

	function showBlocks(blocks, offset) {
		blocks.each(function(){
			( $(this).offset().top <= $(window).scrollTop()+$(window).height()*offset && $(this).find('.cd-timeline-img').hasClass('is-hidden') ) && $(this).find('.cd-timeline-img, .cd-timeline-content').removeClass('is-hidden').addClass('bounce-in');
		});
	}

    var html="";
	$.ajax({
		url: "/get-timeline",
		type: 'GET',
		success: function(data) {
            $("#cd-timeline").empty();
			data = JSON.parse((data));
            $.each(data, function (k,v) {

                html+='<div class="cd-timeline-block">' +
                            '<div class="cd-timeline-img cd-movie"></div>' +
                            '<div class="cd-timeline-content">' +
                                ' <h2>'+ v.title+'</h2>'+
                                '<p>'+ v.description+'</p>'+
                                '<span class="cd-date">'+v.date+'</span>'+
                            '</div>'+
                      '</div>';

            });

            $("#cd-timeline").append(html);
            //timelineBlocks = $('.cd-timeline-block'),
            //    offset = 0.8;
            timelineBlocks = $('.cd-timeline-block'),
                offset = 0.8;
            //hide timeline blocks which are outside the viewport
            hideBlocks(timelineBlocks, offset);
		},
		error: function(data) {
			//console.log(data)
			//alert("Error saving script");
		}
	});


});