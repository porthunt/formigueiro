app.controller("CampaignListController", function($scope, $http) {

	$scope.campaigns = [];

	$scope.campaignListInit = function() {

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

	$scope.calculateDiscount = function(aCampaign) {

		var temp = (aCampaign.value.discounted_unit_price * 100);
		temp = temp / aCampaign.value.original_unit_price;
		temp = temp - 100;
		temp = temp * (-1);
		
		return Math.floor(temp);
	}

});