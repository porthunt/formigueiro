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

		.when('/campanha/:id', {
			templateUrl: 'app/components/campaign/campaignView.html',
			controller: "CampaignController",
			replace: true,
			reloadOnSearch: false
		})

		.when('/campanhas', {
			templateUrl: 'app/components/campaignList/campaignListView.html',
			controller: "CampaignListController",
			replace: true,
			reloadOnSearch: false
		})

		.when('/', {
			templateUrl: 'app/components/index/indexView.html',
			controller: "IndexController",
			replace: true,
			reloadOnSearch: false
		})

		.when('/entrar', {
			templateUrl: 'app/components/login/logInView.html',
			controller: "LogInController",
			replace: true,
			reloadOnSearch: false
		})


		// DEFAULT
		.otherwise({
			redirectTo: '/',
		});

});