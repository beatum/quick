(function () {
  'use strict';

  angular
    .module('quick.authentication', [
      'quick.authentication.controllers',
      'quick.authentication.services'
    ]);

  angular
    .module('quick.authentication.controllers', []);

  angular
    .module('quick.authentication.services', ['ngCookies']);
})();
