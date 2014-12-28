(function () {
  'use strict';

  angular
    .module('quick', [
      'quick.config',
      'quick.routes',
      'quick.accounts',
      'quick.authentication',
      'quick.layout',
      'quick.posts',
      'quick.utils'
    ]);

  angular
    .module('quick.config', []);

  angular
    .module('quick.routes', ['ngRoute']);

  angular
    .module('quick')
    .run(run);

  run.$inject = ['$http'];

  /**
   * @name run
   * @desc Update xsrf $http headers to align with Django's defaults
   */
  function run($http) {
    $http.defaults.xsrfHeaderName = 'X-CSRFToken';
    $http.defaults.xsrfCookieName = 'csrftoken';
  }
})();
