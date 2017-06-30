angular.module('app').controller('FeedCtrl', ['apiService', '$sce', function(apiService, $sce) {
  var FeedCtrl = this;

  FeedCtrl.populateFeed = function() {
    FeedCtrl.errors = '';
    var twitter_username = FeedCtrl.twitter_username;
    if (!twitter_username) {
      FeedCtrl.errors = 'Enter twitter username.';
      return;
    }

    apiService.getFeed(twitter_username).then(function (response) {
      if (response.status == 200) {
        FeedCtrl.feeds = response.data;
      }
    }, function(error) {
         FeedCtrl.errors = "Error occurred while fetching your feed."
    });
  }

  function safeLink(url) {
    return $sce.trustAsResourceUrl(url);
  }

  function getId(url) {
    var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    var match = url.match(regExp);

    if (match && match[2].length == 11) {
        return match[2];
    } else {
        return null;
    }
  }

}]);
