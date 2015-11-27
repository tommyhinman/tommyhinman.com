angular.module('albumLists', ['ngAnimate', 'ui.bootstrap'])
	.config(['$interpolateProvider', function($interpolateProvider) {
	  $interpolateProvider.startSymbol('{[');
	  $interpolateProvider.endSymbol(']}');
	}])
	.controller('albumListsController', function ($scope, $log, $location) {
		$scope.options = ['2011','2012','2013','2014']
		if($location.path()) {
			$scope.selectedYear = $location.path().replace('/','');
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
		}

	});