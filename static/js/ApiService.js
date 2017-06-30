angular.module('app').factory('apiService', ['$http', function($http) {

  var urlBase = '/api'

  // this is service object with list of methods that will be used by controller
  var service = {
    getFeed: getFeed
  };

  function getFeed(twitter_username) {
    return $http.get(urlBase + '/feed/' + twitter_username)
  }

  return service

}])
