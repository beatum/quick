(function () {
  'use strict';

  angular
    .module('quick.posts', [
      'quick.posts.controllers',
      'quick.posts.directives',
      'quick.posts.services'
    ]);

  angular
    .module('quick.posts.controllers', []);

  angular
    .module('quick.posts.directives', ['ngDialog']);

  angular
    .module('quick.posts.services', []);
})();
