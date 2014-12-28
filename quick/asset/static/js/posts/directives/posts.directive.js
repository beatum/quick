/**
 * Posts
 * @namespace quick.posts.directives
 */
(function () {
  'use strict';

  angular
    .module('quick.posts.directives')
    .directive('posts', posts);

  /**
   * @namespace Posts
   */
  function posts() {
    /**
     * @name directive
     * @desc The directive to be returned
     * @memberOf quick.posts.directives.Posts
     */
    var directive = {
      controller: 'PostsController',
      controllerAs: 'vm',
      restrict: 'E',
      scope: {
        posts: '='
      },
      templateUrl: '/static/templates/posts/posts.html'
    };

    return directive;
  }
})();
