import React from "react";

interface CurrentLeaderState {
  name: string,
}

export default class CurrentLeader extends React.Component <CurrentLeaderState> {
  render() {
    const { name } = this.props;
  return <div style={{ padding: ".75rem .75rem", margin: 0 }} className="alert alert-warning"><strong>Current Leader of the Game:</strong><br /><mark>{ name }</mark></div>;
  }
};
