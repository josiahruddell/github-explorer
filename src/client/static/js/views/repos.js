(function(exports){
    'use strict';
    var RepoList = React.createClass({

        render: function(){
            if (this.props.loading){
                return (<h6>Loading...</h6>);
            }

            if (!this.props.valid){
                return (
                    <div>
                        <h6>Could not load any results. Search for another company name.</h6>
                        <em>Hint: try "netflix"</em>
                    </div>
                );
            }

            var rows = this.props.repos.map(function (repo) {
                return (
                    <Repo {...repo} />
                );
            });
            return <div>{rows}</div>;
        }
    });

    var Repo = React.createClass({
        render: function() {
            return (
                <div className="row">
                    <div className="eight columns">
                        <a href={this.props.html_url} target="_blank" title="View on Github">
                            <strong>{this.props.full_name}</strong>
                        </a>
                        <em> ({this.props.language})</em>
                        <p>{this.props.description}&nbsp;</p>
                    </div>
                    <div className="four columns">
                        <button data-owner={this.props.owner_login} data-repo={this.props.name} className="view-commits">View Commits</button>
                    </div>
                </div>
            );
        }
    });

    exports.RepoList = RepoList;
})(window.views || (window.views = {}));