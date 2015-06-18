(function(exports){
    'use strict';
    var CommitList = React.createClass({

        render: function(){
            if (this.props.loading){
                return (<h6>Loading...</h6>);
            }

            if (!this.props.valid){
                return (
                    <div>
                        <p><a className="back-to-repos" href="javascript:;" title="Back to Repos">Go Back</a></p>
                        <h6>Could not load any results.</h6>
                    </div>
                );
            }

            var rows = this.props.commits.map(function (commit) {
                return (
                    <Commit {...commit} />
                );
            });
            return (
                <div>
                    <p><a className="back-to-repos" href="javascript:;" title="Back to Repos">Go Back</a></p>
                    {rows}
                </div>
            );
        }
    });

    var Commit = React.createClass({
        render: function() {
            return (
                <div className="row">
                    <div className="twelve columns">
                        <a href={this.props.html_url} target="_blank" title="View on Github">
                            <strong>{this.props.sha}</strong>
                        </a>
                        <em> ({this.props.author.name})</em>
                        <p>{this.props.message}&nbsp;</p>
                    </div>
                </div>
            );
        }
    });

    exports.CommitList = CommitList;
})(window.views || (window.views = {}));