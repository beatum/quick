(function () {
  'use strict';

  angular
    .module('quick.authentication.interceptors')
    .service('AuthInterceptor', AuthInterceptor);

  AuthInterceptor.$inject = ['$injector', '$location', '$q'];

  function AuthInterceptor($injector, $location, $q) {
    var AuthInterceptor = {
      request: request,
      responseError: responseError
    };

    return AuthInterceptor;

    function request(config) {
      var Authentication = $injector.get('Authentication');
      var token = Authentication.getToken();

      if (token) {
        config.headers['Authorization'] = 'JWT ' + token;
      }

      return config;
    }

    function responseError(response) {
      if (response.status === 403) {
        if (response.data.detial === 'Signature has expired.') {
          $location.path('/login');
        }
      }

      return $q.reject(response);
    }
  }
})();