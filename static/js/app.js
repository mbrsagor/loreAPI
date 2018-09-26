angular.module('MyApp', [])
.controller('AppCtrl', function($scope, $http){
    // Show data template
    $http.get('api/list').then(function(response){
      $scope.dataList = [];
      for (var i = 0; i < response.data.length; i++) {
        var addData  = {};
        addData.id   = response.data[i].id
        addData.name = response.data[i].name
        addData.roll = response.data[i].roll
        $scope.dataList.push(addData)
      }
    });

  // Add data to database
  $scope.addUser = function(){
      $http({
      method : 'post',
      url    : 'api/create/',
      data   : {
        name : $scope.ngname,
        roll : $scope.ngroll,
      },
      headers: { 'Content-Type': 'application/json' }
    }).then(function success(response){
      $scope.dataList.push(response.data);
    });
  }


 // update data to database
 $scope.UpdateUser = function(id){
  $http({
    method  : 'put',
    url     : 'api/update'+id,
    data    : {
      name  : $scope.ngname,
      roll  : $scope.ngroll
    }
  });
}

// Delete data
$scope.delete = function(id){
  $http({
  method : 'delete',
  url    : 'api/delete/'+id,
  headers: { 'Content-Type': 'application/json' }
}).then(function success(response){
  $scope.dataList.splice(response.id, 1);
});
}

});
