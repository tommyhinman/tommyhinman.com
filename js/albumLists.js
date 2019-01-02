angular.module('albumLists', ['ngAnimate', 'ui.bootstrap'])
	.config(['$interpolateProvider', function($interpolateProvider) {
	  $interpolateProvider.startSymbol('{[');
	  $interpolateProvider.endSymbol(']}');
	}])
	.controller('albumListsController', function ($scope, $log, $location) {
		$scope.options = ['2011','2012','2013','2014','2015','2016','2017','2018']
		if($location.path() != '') {
			$scope.selectedYear = $location.path().replace('/','');
		} else {
			$scope.selectedYear = '2018';
		}
		
		$scope.status = {
			isopen: false
		};

		$scope.toggled = function(open) {
			$log.log('Dropdown is now ', open);

		};

		$scope.selected = function(item) {
			$scope.selectedYear = item;
			$location.path(item);
			loadImagesForYear($scope.selectedYear);
		}

		loadImagesForYear($scope.selectedYear);
	});

	function loadImagesForYear(year) {
		$("#albumList" + year).find(".album-art").each(function() {
			$(this).attr("src", $(this).attr("ng-slow-src"));
		} )
	}