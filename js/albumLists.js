angular.module('albumLists', ['ngAnimate', 'ui.bootstrap'])
	.config(['$interpolateProvider', function($interpolateProvider) {
	  $interpolateProvider.startSymbol('{[');
	  $interpolateProvider.endSymbol(']}');
	}])
	.controller('albumListsController', function ($scope, $log) {
		$scope.options = ['2011','2012','2013','2014']
		$scope.selectedYear = '2014';

		$scope.status = {
			isopen: false
		};

		$scope.toggled = function(open) {
			$log.log('Dropdown is now ', open);
		};

		$scope.selected = function(item) {
			$scope.selectedYear = item
		}

	});