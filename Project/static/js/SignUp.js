var login=angular.module('login',['ui.router'])
.controller('loginctrl',function ($scope,$location) {
	// alert("hello");

	$scope.sign=function(){
		$location.path('/sign');

		
	}

	$scope.login=function(){
		$location.path('/login');
	}
})

.config(function($stateProvider,$urlRouterProvider){
	$urlRouterProvider.otherwise('/sign');
	$stateProvider												//Default-page
	.state('sign',{
		url:"/sign",
		templateUrl:'sign.html',
		// controller:'homepage'
	})

	.state('login',{									//Second-page
		url:"/login",
		templateUrl:'login.html',
		// controller:'orderpage'
	})

})	