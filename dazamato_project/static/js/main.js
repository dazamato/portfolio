(function($) {

	$(window).on('load',function() {
        $('.images-preloader').fadeOut();
    });

    // --------------------------------------------------
    // Back To Top
    // --------------------------------------------------
    var offset = 450;
    var duration = 1000;
    var upToTop = $("#back-to-top");
    upToTop.hide();
    $(window).on('scroll', function() {
        if ($(this).scrollTop() > offset) {
            upToTop.fadeIn(duration);
        } else {
            upToTop.fadeOut(duration);
        }
    });
    upToTop.on('click', function(event) {
        event.preventDefault();
        $('html, body').animate({ scrollTop: 0 }, duration);
        return false;
    });

    $(".scroll-slider1").on('click', function() {
        $([document.documentElement, document.body]).animate({
            scrollTop: $("#featured-home2").offset().top
        }, 1000);
    });

    //   Search box
    $('body').on('click', function(event) {
        $(this).find('.header-bottom .search-box form input').fadeOut();
    });
    $('.header-bottom .search-box form .search-icon').on('click', function(event) {
        $(this).parent().find('input').fadeToggle();
        event.stopPropagation(); //ko tính click body
    });
    $('.header-bottom .search-box form input').on('click', function(event) {
        $(this).fadeIn();
        event.stopPropagation();
    });

    try {
        //form search header
        $('body').on('click', function(event) {
            $(this).find('.header-top-mobile .search-box form input').fadeOut();
        });
        $('.header-top-mobile .search-box form .search-icon').on('click', function(event) {
            $(this).parent().find('input').fadeToggle();
            $(this).parent().parent().toggleClass('search-widget-open');
            event.stopPropagation(); //ko tính click body
        });
        $('.header-top-mobile .search-box form input').on('click', function(event) {
            $(this).fadeIn();
            event.stopPropagation();
        });
    } catch(err) {
        console.log(err)
    }

    /*Hamburger Button*/
    $('.hamburger').on("click", function() {
        $(this).toggleClass("is-active");
        $('.au-nav-mobile').slideToggle(200, 'linear');
    });

    // Navbar menu dropdown
    $('.au-navbar-menu li .arrow').on('click', function(e) {
        $(this).siblings('.sub-menu').slideToggle(200, 'linear');
        $(this).toggleClass('clicked');
        e.stopPropagation();
    });

    $('#au_rev_slider').show().revolution({
        responsiveLevels: [1200, 992, 768, 480],
        gridwidth: [1200, 992, 768, 480],
        sliderLayout: 'fullwidth',
        gridheight: [650, 550, 350, 350],
        delay: 5000,
        spinner: 'spinner0',
        /* basic navigation arrows and bullets */
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'gyges',
                hide_onleave: false,
                hide_onmobile: true,
                hide_under: 768,
            },

            bullets: {
                enable: false,
                style: 'hermes',
                hide_onleave: false,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 20,
                space: 5
            }
        }
    });
    $('#au_rev_slider2').show().revolution({
        responsiveLevels: [1200, 992, 768, 480],
        gridwidth: [1200, 992, 768, 480],
        autoHeight: 'on',
        sliderLayout: 'fullscreen',
        delay: 5000,
        spinner: 'spinner0',
        /* basic navigation arrows and bullets */
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'gyges',
                hide_onleave: false,
                hide_onmobile: true,
                hide_under: 768,
            },

            bullets: {
                enable: false,
                style: 'hermes',
                hide_onleave: false,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 20,
                space: 5
            }
        }
    });

    $('#au_rev_slider3').show().revolution({
        responsiveLevels: [1200, 992, 768, 480],
        gridwidth: [1200, 992, 768, 480],
        sliderLayout: 'fullwidth',
        gridheight: [850, 750, 650, 550],
        delay: 5000,
        spinner: 'spinner0',
        /* basic navigation arrows and bullets */
        navigation: {
            onHoverStop: "off",
            arrows: {
                enable: true,
                style: 'gyges',
                hide_onleave: false,
                hide_onmobile: true,
                hide_under: 768,
                left: {
                    container: 'slider',
                    h_align: 'left',
                    v_align: 'center',
                    h_offset: 30,
                    v_offset: -75
                },
         
                right: {
                    container: 'slider',
                    h_align: 'right',
                    v_align: 'center',
                    h_offset: 30,
                    v_offset: -75
                },
            },


            bullets: {
                enable: false,
                style: 'hermes',
                hide_onleave: false,
                h_align: "center",
                v_align: "bottom",
                h_offset: 0,
                v_offset: 20,
                space: 5
            }
        }
    });


    // fixed navbar when scroll
    var navbarFix = $("#js-navbar-fixed");
    var headerOffset = navbarFix.offset().top + 1;
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > headerOffset) {
            navbarFix.addClass('fixed');
        } else {
            navbarFix.removeClass("fixed");
        }
    });

    $('.testimonials-content').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        dots: true,
        touchMove : true,
        focusOnSelect: true,
        responsive: [
            {
              breakpoint: 768,
              settings: {
                arrows: true,
                dots: false,
              }
            },
        ]
    });

    $('.partner-content').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        responsive: [
            {
                breakpoint: 992,
                settings: {
                  arrows: false,
                  centerMode: true,
                  centerPadding: '10px',
                  slidesToShow: 3
                }
            },
            {
              breakpoint: 768,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 1
              }
            }
        ]
    });

    $('.home2-blog-content .row').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: true,
        dots: false,
        responsive: [
            {
              breakpoint: 768,
              settings: {
                arrows: true,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 2
              }
            },
            {
              breakpoint: 480,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 1
              }
            }
        ]
    });
    $('.home3-testimonials-content .row').slick({
        slidesToShow: 2,
        slidesToScroll: 2,
        arrows: false,
        dots: true,
        responsive: [
            {
              breakpoint: 768,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 1
              }
            },
            {
              breakpoint: 480,
              settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 1
              }
            }
        ]
    });
    $('.aboutus-testimonials-content').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: true
    });
    $('.aboutus-testimonials2-content .row').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        arrows: false,
        dots: false,
        autoplay: true,
        responsive: [
            {
              breakpoint: 992,
              settings: {
                arrows: false,
                dots: true,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 2
              }
            },
            {
              breakpoint: 575,
              settings: {
                arrows: false,
                dots: true,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 1
              }
            }
        ]
    });
    $('.featured-course-slider .row').slick({
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: true,
        dots: false,
        autoplay: true,
        responsive: [
            {
              breakpoint: 992,
              settings: {
                arrows: false,
                dots: true,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 2
              }
            },
            {
              breakpoint: 575,
              settings: {
                arrows: false,
                dots: true,
                centerMode: true,
                centerPadding: '10px',
                slidesToShow: 1
              }
            }
        ]
    });
    

    /*==================================================================
    [ Play video 01 ]*/
    $.fn.bmdIframe = function( options ) {
        var self = this;
        var settings = $.extend({
            classBtn: '.bmd-modalButton',
            defaultW: 640,
            defaultH: 360
        }, options );
      
        $(settings.classBtn).on('click', function(e) {
          var allowFullscreen = $(this).attr('data-bmdVideoFullscreen') || false;
          
          var dataVideo = {
            'src': $(this).attr('data-bmdSrc') + "?autoplay=1",
            'height': $(this).attr('data-bmdHeight') || settings.defaultH,
            'width': $(this).attr('data-bmdWidth') || settings.defaultW
          };
          
          if ( allowFullscreen ) dataVideo.allowfullscreen = "";
          
          // stampiamo i nostri dati nell'iframe
          $(self).find("iframe").attr(dataVideo);
        });
      
        // se si chiude la modale resettiamo i dati dell'iframe per impedire ad un video di continuare a riprodursi anche quando la modale è chiusa
        this.on('hidden.bs.modal', function(){
          $(this).find('iframe').html("").attr("src", "");
        });
      
        return this;
    };
    jQuery("#modal-video-01").bmdIframe();
	// video popup

    // Video
	$('.vimeo a,.youtube a').on('click',function (e) {
		e.preventDefault();
		var videoLink = $(this).attr('href');
		var classeV = $(this).parent();
		var PlaceV = $(this).parent();
		if ($(this).parent().hasClass('youtube')) {
			$(this).parent().wrapAll('<div class="video-wrapper">');
			$(PlaceV).html('<iframe frameborder="0" height="333" src="' + videoLink + '?autoplay=1&showinfo=0" title="YouTube video player" width="100%"></iframe>');
		} else {
			$(this).parent().wrapAll('<div class="video-wrapper">');
			$(PlaceV).html('<iframe src="' + videoLink + '?title=0&amp;byline=0&amp;portrait=0&amp;autoplay=1&amp;color=cfa144" width="100%" height="300" frameborder="0"></iframe>');
		}
    });

    var executed = false;
    var waypointSelector = $('.js-waypoint');
    if (waypointSelector) {
        waypointSelector.waypoint(function () {
            if (!executed) {
                executed = true;
                /*progress bar*/
                $('.au-progress-1 .au-progress-bar').progressbar({
                    update: function (current_percentage, $this) {
                        $this.find("span").html(current_percentage + '%');
                    }
                });

                

            }
        }, {offset: 'bottom-in-view'});
    }

    var jsTabPro = $('#review');
   
        if (jsTabPro.find('active')) {
            /*progress bar*/
            $('.au-progress-2 .au-progress-bar').progressbar({
                transition_delay: 1500
            });
        }
    /*Couter up*/
    var counterUp = $(".counterUp");
    if (counterUp) {
        counterUp.counterUp({
            delay: 10,
            time: 1000
        });
    }

    $(window).on('load', function () {
        var $grid_item = $('.grid').isotope({
            itemSelector: '.element-item',
            layoutMode: 'fitRows'
        });
        // bind filter button click
        $('.filter-featured-course li span').on('click', function() {
            var filterValue = $(this).attr('data-filter');
            $grid_item.isotope({ filter: filterValue });
        });
        // change is-checked class on buttons
        $('.filter-featured-course li span').on('click',function() {
            $('.filter-featured-course li').find('.is-checked').removeClass("is-checked");
            $(this).addClass("is-checked");
        });
    });

    $(window).on('load', function () {
        var $grid_item = $('.events-grid .row').isotope({
            itemSelector: '.item',
            layoutMode: 'fitRows'
        });
        // bind filter button click
        $('.filter-events li span').on('click', function() {
            var filterValue = $(this).attr('data-filter');
            $grid_item.isotope({ filter: filterValue });
        });
        // change is-checked class on buttons
        $('.filter-events li span').on('click',function() {
            $('.filter-events li').find('.is-checked').removeClass("is-checked");
            $(this).addClass("is-checked");
        });
    });

    $(window).on('load', function () {
        var $grid_item = $('.gallery-grid .row').isotope({
            itemSelector: '.gallery-item',
            layoutMode: 'fitRows'
        });
        // bind filter button click
        $('.filter-gallery li span').on('click', function() {
            var filterValue = $(this).attr('data-filter');
            $grid_item.isotope({ filter: filterValue });
        });
        // change is-checked class on buttons
        $('.filter-gallery li span').on('click',function() {
            $('.filter-gallery li').find('.is-checked').removeClass("is-checked");
            $(this).addClass("is-checked");
        });
    });

    $(window).on('load', function () {
        var $grid = $('.gallery-mansory').masonry({
            itemSelector: '.grid-item',
            percentPosition: true,
            columnWidth: '.grid-sizer',
        });
        // layout Masonry after each image loads
        $grid.imagesLoaded().progress(function() {
            $grid.masonry();
        });
        // bind filter button click
        $('.filter-gallery li span').on('click', function() {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({ filter: filterValue });
        });
        // change is-checked class on buttons
        $('.filter-gallery li span').on('click',function() {
            $('.filter-gallery li').find('.is-checked').removeClass("is-checked");
            $(this).addClass("is-checked");
        });
    });

    $('.fqa-content ul li').on('click', function() {
        $('.fqa-content ul').find('.active').removeClass("active");
        $(this).addClass("active");
    });

    $('.single-course-content .curriculum-content  li').on('click', function() {
        $('.single-course-content .curriculum-content').find('.active').removeClass("active");
        $(this).addClass("active");
    });
    $('.grouped_elements').fancybox({
		'transitionIn'	:	'fade',
		'transitionOut'	:	'fade',
		'speedIn'		:	600, 
		'speedOut'		:	600, 
        'overlayShow'	:	false,
        'width'         : 870,
        'autoDimensions' : false,
        'centerOnScroll' : true,
    });
    $('.grouped_elements2').fancybox({
		'transitionIn'	:	'fade',
		'transitionOut'	:	'fade',
		'speedIn'		:	600, 
		'speedOut'		:	600, 
        'overlayShow'	:	false,
        'width'         : 870,
        'autoDimensions' : false,
        'centerOnScroll' : true,
    })

})(jQuery);
