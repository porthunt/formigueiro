app.controller("IndexController", function($scope) {

	$scope.indexInit = function() {
		$('.parallax').parallax();
		console.log("Parallax");
	}

});