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

.controller('regCtrl',function($scope){
	$scope.reg = function(){
		alert("erj");
	}
})

.config(function($stateProvider,$urlRouterProvider){
	$urlRouterProvider.otherwise('/sign');
	$stateProvider												//Default-page
	.state('sign',{
		url:"/sign",
		templateUrl:'../templates/sign.html',
		controller:'regCtrl'
	})

	.state('login',{									//Second-page
		url:"/login",
		templateUrl:'../templates/login.html',
		// controller:'orderpage'
	})

})	