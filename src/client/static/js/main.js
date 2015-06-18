(function($, React){
    'use strict';
    // application state
    var store = {
        view: 'repos',
        repo: null,
        owner: null,
        orgSearch: null
    };

    var activatePageListeners = function(){
        // don't let the form submit
        $('form').on('submit', false);

        // main search control
        $('#org-name').on('keypress', function(e){
            if(e.which === 13){ // enter
                store.orgSearch = this.value;
                actions.loadRepos();
                e.preventDefault();
            }
        });

        // attach event on document so activation is not required after
        // view update
        $(document).on('click', 'button.view-commits', function(e){
            var d = $(this).data();
            store.repo = d.repo;
            store.owner = d.owner;
            actions.loadCommits();
        });

        $(document).on('click', 'a.back-to-repos', function(e){
           helpers.toggleView();
        });
    };

    var helpers = {
        toggleView: function(load){
            // there are only two views in this application
            if (store.view === 'repos'){
                store.view = 'commits';
                $('#repositories').hide();
                $('#commits').show();
            }
            else{
                store.view = 'repos';
                $('#commits').hide();
                $('#repositories').show();
            }
        },
        _render: function(target, view, data){
            React.render(React.createElement(view, data), target);
        },
        renderReposView: function(data){
            helpers._render($('#repositories').get(0), views.RepoList, data);
            if(store.view !== 'repos')
                helpers.toggleView();
        },
        renderCommitsView: function(data){
            helpers._render($('#commits').get(0), views.CommitList, data);
            if(store.view !== 'commits')
                helpers.toggleView();
        }
    };

    // primary controller functions
    // responsible for getting data
    // and updating the view
    var actions = {
        loadRepos: function(){
            // show loader
            helpers.renderReposView({loading: true});
            $.get('/api/repositories/' + store.orgSearch).done(function(data){
                var valid = true;
                if (!data || !data.length){
                    console.warn('Unexpected format: ', data);
                    valid = false;
                }

                helpers.renderReposView({valid: valid, repos: data});

            }).fail(function(res){
                console.error(res);
                helpers.renderReposView({valid: false});
            });
        },
        loadCommits: function(){
            helpers.renderCommitsView({loading: true});
            $.get('/api/commits/' + store.owner + '/' + store.repo).done(function(data){
                var valid = true;
                if (!data || !data.length){
                    console.warn('Unexpected format: ', data);
                    valid = false;
                }

                helpers.renderCommitsView({valid: valid, commits: data});

            }).fail(function(res){
                console.error(res);
                helpers.renderCommitsView({valid: false});
            });

        }
    };

    // page ready entry point
    $(function(){
        activatePageListeners();
    });

})(this.jQuery, this.React);