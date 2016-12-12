var house=angular.module('house',['ui.router'])
.controller('housectrl',function ($scope,$location) {
	// alert("hello");

	$scope.sign=function(){
		$location.path('/post');

		
	}

	$scope.login=function(){
		$location.path('/find');
	}
})

.config(function($stateProvider,$urlRouterProvider){
	$urlRouterProvider.otherwise('/hm');
	$stateProvider
	.state('hm',{
		url:"/hm",
		templateUrl:'hm.html',
		// controller:'homepage'
	})												//Default-page
	.state('post',{
		url:"/post",
		templateUrl:'post.html',
		// controller:'homepage'
	})

	.state('find',{									//Second-page
		url:"/find",
		templateUrl:'find.html',
		// controller:'orderpage'
	})

})	