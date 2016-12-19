var house=angular.module('house',['ui.router'])
.controller('housectrl',function ($scope,$location) {
	// alert("hello");
})

.controller('postctrl',function ($scope,$location) {
	var myHouse=[{"HouseType":'1 BHK',
				  "RentPrice":200,
				  "OwnerName":'James',
				  "Details":'Fully Furnished',
				  "Address":'1140 Oregon Ave',
				  "ContactNum":'9452333334'
				}]
	$scope.HouseType;
	$scope.form=false;
	$scope.confirm=true;
	$scope.final=true;

	$scope.add=function(){
		$scope.form=true;
		$scope.confirm=false;
	}

	$scope.submit=function(){

		$scope.confirm=true;
		$scope.final=false;
		myHouse.push({"HouseType":$scope.HouseType,
					  "RentPrice":$scope.RentPrice,
				      "OwnerName":$scope.OwnerName,
				      "Details":$scope.Details,
				      "Address":$scope.Address,
				      "ContactNum":$scope.ContactNum	});

		console.log(myHouse);
	}

	$scope.back=function(){
		$scope.form=false;
	$scope.confirm=true;

	}

	$scope.newpost=function(){
		$scope.form=false;
		$scope.final=true;
		$scope.HouseType="";
		$scope.RentPrice="";
		$scope.OwnerName="";
		$scope.Details="";
		$scope.Address="";
		$scope.ContactNum="";
	}
})


.controller('findCtrl',function($scope,$http){
	$scope.v="hello";
	$scope.res = [];
	$http.get('http://127.0.0.1:8000/index/house/post')
	.success(function(resp){
		console.log('works')
		$scope.res = resp.genres;
		console.log($scope.res);
	})	
$scope.hi1=function(){

	alert($scope.hi)
}
})
//https://private-a73e-aquentuxsociety.apiary-mock.com/members
//http://127.0.0.1:8000/index/house/post

.config(function($stateProvider,$urlRouterProvider){
	$urlRouterProvider.otherwise('/hm');
	$stateProvider
	.state('hm',{
		url:"/hm",
		templateUrl:"../templates/hm.html",
		// controller:'homepage'
	})												//Default-page
	.state('post',{
		url:"/post",
		templateUrl:'post.html',
		controller:'postctrl'
	})

	.state('find',{									//Second-page
		url:"/find",
		templateUrl:'find.html',
		controller:'findCtrl'
	})

})	