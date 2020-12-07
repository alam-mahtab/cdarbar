$('.owl-carousel').owlCarousel({

	lazyLoad: true,
	lazyLoadEager: 1,
	loop: false,
	margin: 15,
	dots: false,
	nav: true,
	responsive: {
		0: {
			items: 2,
			nav: false
		},
		600: {
			items: 3,
			nav: false
		},
		1000: {
			items: 4
		},
		1600: {
			items: 5
		}
	}
})