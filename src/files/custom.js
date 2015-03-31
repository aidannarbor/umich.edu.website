jQuery(window).load(function() {

  jQuery('#slidebox').flexslider({
        animation: "fade",
        directionNav:true,
        controlNav:false,
  	pauseOnAction: true,
  	pauseOnHover: true
      });
    
    
    jQuery('#topmenu').mobileMenu({
			prependTo:'.mobilenavi'
			});	
	
    
});


