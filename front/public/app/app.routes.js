app.config(function($routeProvider, $locationProvider, $httpProvider) {

	$routeProvider

		.when('/', {
			templateUrl: 'app/components/index/indexView.html',
			controller: "IndexController",
			replace: true,
			reloadOnSearch: false
		})

		.when('/', {
			templateUrl: 'app/components/index/indexView.html',
			controller: "IndexController",
			replace: true,
			reloadOnSearch: false
		})
		
		// DEFAULT
		.otherwise({
			redirectTo: '/',
		});

});