app.controller('CampaignController', function($scope, $http, $routeParams){

	$scope.dummyCampaign = {
		piecePrice: 7999.99
	}

	$scope.comments = [
		{
			value: {
				author: "A Retrosaria",
				text: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." 
			}
		}
	];

	$scope.campaignInit = function() {
		$('.parallax').parallax();
		console.log("Parallax");

		$scope.newComment = "";

		// get campaign
		$http.get("http://formigueiro-back.mybluemix.net/api/campaign/id/" + $routeParams.id)
		.success(function(data, status) {

			console.log("Success", data);

			$scope.campaign = data[0];

			//$scope.loadFromBreadcrumb();
		})
		.error(function(data) {
			console.log("Error", data);
		})

		// get total backer
		$http.get("http://formigueiro-back.mybluemix.net/api/campaign/id/" + $routeParams.id + "/total")
		.success(function(data, status) {

			console.log("Success", data);

			$scope.campaignTotal = data;

			//$scope.loadFromBreadcrumb();
		})
		.error(function(data) {
			console.log("Error", data);
		})

		// get backers
		$http.get("http://formigueiro-back.mybluemix.net/api/backer/campaign_id/" + $routeParams.id)
		.success(function(data, status) {

			console.log("Success backer", data);

			// for (var i = 0; i < data.length; i++) {
			// 	data[i] = data[i];
			// }

			$scope.backers = data;

			//$scope.loadFromBreadcrumb();
		})
		.error(function(data) {
			console.log("Error", data);
		})

		// get comments
		$http.get("http://formigueiro-back.mybluemix.net/api/campaign/id/" + $routeParams.id + "/comments")
		.success(function(data, status) {

			console.log("Success comments", data);

			// for (var i = 0; i < data.length; i++) {
			// 	dat2a[i] = data[i];
			// }

			$scope.comments = data;

			//$scope.loadFromBreadcrumb();
		})
		.error(function(data) {
			console.log("Error", data);
		})

		$scope.qtd = 0;
		$scope.qtdPartialTotal = 0;
		$scope.qtdNotDiscountedPartialTotal = 0;
	}

	$scope.qtdMinusButton = function() {
		if ($scope.qtd >= 1) {
			$scope.qtd--;
			$scope.qtdGetPartialTotal();
		}
	}

	$scope.qtdAddButton = function() {
		$scope.qtd++;
		$scope.qtdGetPartialTotal();
	}

	$scope.qtdGetPartialTotal = function() {

		$scope.qtd = parseInt($scope.qtd);

		$scope.qtdNotDiscountedPartialTotal = $scope.campaign.value.original_unit_price * $scope.qtd;

		$scope.qtdNotDiscountedPartialTotal = parseFloat($scope.qtdNotDiscountedPartialTotal.toFixed(2));

		$scope.qtdPartialTotal = $scope.campaign.value.discounted_unit_price * $scope.qtd;

		$scope.qtdPartialTotal = parseFloat($scope.qtdPartialTotal.toFixed(2));

		console.log("$scope.qtdPartialTotal updated", $scope.qtdPartialTotal);

	}

	$scope.calculatePercentage = function() {

		var temp =  Math.floor(($scope.campaignTotal * 100) / $scope.campaign.value.total);

		console.log(temp);

		return temp;

	}

	$scope.joinCampaign = function() {

		console.log("Join Campaign");

		if ($scope.qtd > 0) {
			// get campaign
			$http.put("http://formigueiro-back.mybluemix.net/api/backer/add", {
			    "doc_type": "backer",
			    "campaign_id": $routeParams.id,
			    "company_id": "a7163834a5b1a3095bee3307a975dedc",
			    "unit": $scope.qtd
			})
			.success(function(data, status) {

				console.log("Success", data);
				Materialize.toast('Juntou-se a campanha com sucesso!', 2000)
				$scope.campaignInit();

				//$scope.loadFromBreadcrumb();
			})
			.error(function(data) {
				$scope.toggleLoading(false);
				console.log("Error", data);
			})
		}


	}

	$scope.fillFeel = function(aMood) {

		switch(aMood) {

			case "positive":
				return "sentiment_satisfied"
			break;

			case "neutral":
				return "sentiment_neutral"
			break;

			case "negative":
				return "sentiment_dissatisfied"
			break;

		}

	}

	$scope.addComment = function() {

		console.log("Add Comment");

		$http.put("http://formigueiro-back.mybluemix.net/api/comment/add", {
			"doc_type": "comment",
			"campaign_id": $scope.campaign.id,
			"company_id": "a7163834a5b1a3095bee3307a975dedc",
			"comment": $scope.newComment
		})
		.success(function(data, status) {

			console.log("Success add comment", data);

			Materialize.toast('Adicionou um comentário com sucesso!', 2000)
			$scope.campaignInit();

			$scope.comments = data;

			//$scope.loadFromBreadcrumb();
		})
		.error(function(data) {
			console.log("Error", data);
		})

	}

});