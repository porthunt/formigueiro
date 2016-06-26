app.controller("CampaignListController", function($scope) {

	$scope.campaigns = [
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
		{
			title: "MacBook",
			originalPrice: 7999.99,
			currentPrice: 6999.99,
			lowestPrice: 6000.00,
			image: "macbook.jpeg"
		},
		{
			title: "Harry Potter e a Câmara Secreta",
			originalPrice: 39.99,
			currentPrice: 34.99,
			lowestPrice: 29.98,
			image: "harrypotter.jpg"
		},
		{
			title: "Cuba de Apoio Branca",
			originalPrice: 400.00,
			currentPrice: 370.00,
			lowestPrice: 300.00,
			image: "cuba.jpg"
		},
	];

	$scope.campaignListInit = function() {

		$http.get("/api/campaign/")
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

		var temp = (aCampaign.lowestPrice * 100) / aCampaign.originalPrice;
		temp = (temp - 100) * (-1);
		
		console.log("calculateDiscount", temp);
		return temp.toFixed(2);
	}

});