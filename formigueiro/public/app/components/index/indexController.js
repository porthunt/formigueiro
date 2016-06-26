app.controller("IndexController", function($scope, $http) {

	$scope.indexInit = function() {
		$('.parallax').parallax();
		console.log("Parallax");

		$http.get("http://formigueiro-back.mybluemix.net/api/campaign")
		.success(function(data, status) {

			console.log("Success", data);

			$scope.campaigns = data;

			//$scope.loadFromBreadcrumb();
		})
		.error(function(data) {
			$scope.toggleLoading(false);
			console.log("Error", data);
		})
	}

});