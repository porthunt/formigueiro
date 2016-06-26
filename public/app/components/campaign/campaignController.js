app.controller('CampaignController', function($scope){

	$scope.dummyCampaign = {
		piecePrice: 7999.99
	}
	
	$scope.campaignInit = function() {
		$('.parallax').parallax();
		console.log("Parallax");

		$scope.qtd = 0;
		$scope.qtdPartialTotal = 0;
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

		$scope.qtdPartialTotal = $scope.dummyCampaign.piecePrice * $scope.qtd;

		$scope.qtdPartialTotal = parseFloat($scope.qtdPartialTotal.toFixed(2));

		console.log("$scope.qtdPartialTotal updated", $scope.qtdPartialTotal);

	}

});