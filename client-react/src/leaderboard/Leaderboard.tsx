import * as React from "react";
import sort from "fast-sort";
import { MDBDataTable } from "mdbreact";
import {
  Button
} from 'react-bootstrap'

import Actions from '../redux/actions';
import { RootState } from '../redux/reducers';
import { connect } from 'react-redux';

import CurrentLeader from './CurrentLeader';
import CreateLeaderAlertModal from './CreateLeaderAlertModal';

import { leaders } from "./data";

interface LeaderBoardState {
  modalOpen: boolean;
  currentLeader: string;
}

interface LeaderBoardProps {
  name?: string;
  gameId?: string;
  allLeaders: Array<{ id: number, name: string, score: number }>;
  getAllLeaders: () => {};
}

class Leaderboard extends React.Component<LeaderBoardProps, LeaderBoardState> {

  constructor(props: LeaderBoardProps) {
    super(props);
    this.state = {
        modalOpen: false,
        currentLeader: '',
    }
  }

  componentDidMount() {
    // this.props.getAllLeaders();
    const maxScore = Math.max(...leaders.map(item => item.score));
    const getLeader = leaders.filter(item => item.score === maxScore)[0].name;
    this.setState({
      currentLeader: 'Joe'
    });
  }

  render() {
    // const {
    //   allLeaders,
    // } = this.props;

    // TODO: IMPORTANT `u.id` need to change to `u.score`
    sort(leaders).desc((u: any) => u.score);
    for (let i = 0; i < leaders.length; i++) {
      leaders[i].id = i + 1;
    }

    const data = {
      columns: [
        {
          label: "Rank",
          field: "id",
          width: 150
        },
        {
          label: "Username",
          field: "name",
          width: 270
        },
        {
          label: "Score",
          field: "score",
          sort: "asc",
          width: 200
        }
      ],
      rows: leaders
    };

    const { currentLeader } = this.state;

    return (
      <>
        <CreateLeaderAlertModal open={this.state.modalOpen} listOfLeaders={ leaders } close={() => this.setState({modalOpen: false})}/>
        <div style={{
                      display: 'flex',
                      alignItems: 'flex-end',
                      margin: '0 0 1rem',
                    }}>
            <CurrentLeader name={currentLeader} />
            <Button style={{margin: '0 0 0 10px'}} onClick={
              () => {
                this.setState({modalOpen: true})
              }
            }>Create leader alert</Button>
        </div>
        <MDBDataTable bordered striped small data={ data } />
      </>
    );
  }
}

const mapStateToProps = (state: RootState) => ({
  allLeaders: state.leaders.leaders,
});
const mapDispatchToProps = {
  getAllLeaders: Actions.leaders.getAllLeaders,
};
export default connect(mapStateToProps, mapDispatchToProps)(Leaderboard);
