(function () {
    'use strict';
    angular.module('CarHouMonApp', [])
        .controller('CarHouMonController', ['$scope', '$http', '$log', '$timeout', function($scope, $http, $log, $timeout) {
            $log.log('test');
            var current_levels = function() {
                $http.get('/current_levels')
                    .success(function(data, status) {
                        $scope.levels = data;
                        // $log.log(data);
                        $timeout(current_levels, 5000);
                    })
                    .error(function(data, status) {
                        $scope.levels = {error: {is_on: status}};
                        $timeout(current_levels, 5000);
                    });
            };
            current_levels();
        }]);
}());
