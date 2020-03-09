import * as React from 'react';
import { Row, Modal, Col, Button, Container } from 'react-bootstrap';
import { GameType } from '../../redux/actions/Game'
import CSS from 'csstype';
import moment from 'moment';

interface HeaderBarState {
	days: string;
	hours: string;
	minutes: string;
	seconds: string;
	showShare: boolean;
}

interface HeaderBarProps {
	game: GameType,
	global: boolean,
}

const styles: { [name: string]: CSS.Properties } = {
	heading: {
		width: '100%',
		borderBottom: 'medium solid',
		alignItems: 'center'
	},

	toolbar: {
		justifyContent: 'flex-end',
		alignItems: 'center',
	}
};

class HeaderBar extends React.Component<HeaderBarProps, HeaderBarState> {
	private interval!: NodeJS.Timeout; // setInterval ref

	constructor(props: HeaderBarProps) {
		super(props);

		this.state = {
			days: '',
			hours: '',
			minutes: '',
			seconds: '',
			showShare: false,
		}
	}

	componentDidMount() {
		// moment countdown interval
		this.interval = setInterval(this.countdown, 1000);
	}

	componentWillUnmount() {
		clearInterval(this.interval);
	}

	// calculates how much time is left in the game
	private countdown = () => {
		const endsAt = moment(this.props.game.endsAt);
		const now = moment();
		const diff = moment(endsAt.diff(now));
		const days = diff.format('D');
		const hours = diff.format('HH');
		const minutes = diff.format('mm');
		const seconds = diff.format('ss');
		this.setState({ days, hours, minutes, seconds });
	}

	private toggleShow = () => {
		this.setState({ showShare: !this.state.showShare });
	}

	render() {
		const { days, hours, minutes, seconds, showShare } = this.state;
		const { global, game } = this.props;
		return (
			<div className="HeaderBar">
				<Row style={styles.heading}>
					<Col md="auto">
						<div>
							<h1>{global ? `Global Game` : `Private Game: ${game.name}`}</h1>
						</div>
					</Col>
					<Col>
						<Row style={styles.toolbar}>
							<div style={{ paddingRight: '1em' }}>Ends in: {days} {hours} {minutes} {seconds} </div>
							<Button style={{ marginRight: '1em' }} variant="primary" onClick={this.toggleShow}>Share</Button>
							<Button variant="primary">Leaderboard</Button>
						</Row>
					</Col>
				</Row>

				{/* Share modal */}
				<div className="myModal">
					<Modal show={showShare} onHide={this.toggleShow}>
						<Modal.Header closeButton>
							<Modal.Title>Share this game!</Modal.Title>
						</Modal.Header>
						<Modal.Body>
							<Row>Link: {game.shareableLink}</Row>
							<Row>Code: {game.shareableCode}</Row>
						</Modal.Body>
						<Modal.Footer style={{ justifyContent: 'center' }}>
							<Button variant="secondary" onClick={this.toggleShow}>
								Close
								</Button>
						</Modal.Footer>
					</Modal>
				</div>
			</div>
		)
	}
}

export default HeaderBar