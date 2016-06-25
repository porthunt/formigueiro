app.config(function($routeProvider, $locationProvider, $httpProvider) {

	$routeProvider

		.when('/', {
			templateUrl: 'app/components/index/indexView.html',
			controller: "IndexController",
			replace: true,
			reloadOnSearch: false
		})

		.when('/cadastro', {
			templateUrl: 'app/components/signup/signUpView.html',
			controller: "SignUpController",
			replace: true,
			reloadOnSearch: false
		})
		.when('/campanha', {
			templateUrl: 'app/components/campaign/campaignView.html',
			controller: "CampaignController",
			replace: true,
			reloadOnSearch: false
		})
		
		// DEFAULT
		.otherwise({
			redirectTo: '/',
		});

});