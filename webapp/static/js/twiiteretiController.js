angular.module('twitteretiApp', [])
  .controller('twitteretiCtrl', ['$scope', '$http', twitteretiCtrl]);

function twitteretiCtrl ($scope, $http, $sce) {
    $scope.init = function(){
    $http.get('/twittereti/info').success(function(data){
        $scope.data = JSON.parse(data);
        });
   }

}



