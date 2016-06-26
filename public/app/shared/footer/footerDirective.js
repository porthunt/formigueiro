app.directive('footerElement', function() {
	return {
		templateUrl: 'app/shared/footer/footerView.html',
		controller: "FooterController",
		restrict: 'AE',
		replace: true
	}
});