import React, { Component } from 'react';
import { Button } from 'react-bootstrap';
import PriceAlertsList from './PriceAlertsList';
import actions from '../redux/actions';
import { connect } from 'react-redux';
import CreatePriceAlertModal from './CreatePriceAlertModal';

interface PriceAlertOptionsState {
    modalOpen: boolean;
}

interface PriceAlertOptionsProps {
    getPriceAlerts: () => void;
}

class PriceAlertOptions extends Component<PriceAlertOptionsProps, PriceAlertOptionsState> {
    constructor(props: PriceAlertOptionsProps) {
        super(props);
        this.state = {
            modalOpen: false,
        }
    }
    
    render() {
        return (
            <>
                <CreatePriceAlertModal open={this.state.modalOpen} close={() => this.setState({modalOpen: false})}/>
                <div className="row" style={{padding: 10}}>
                    <div className="col-lg-6" style={{textAlign: 'left'}}>
                        <Button onClick={() => this.setState({modalOpen: true})}>Create price alert</Button>
                    </div>
                    <div className="col-lg-6" style={{textAlign: 'right'}}>
                        <Button onClick={() => this.props.getPriceAlerts()}>Refresh</Button>
                    </div>
                </div>
                <h4>Active Price Alert Subscriptions</h4>
                <PriceAlertsList/>
            </>
        )
    }
}

const mapDispatchToProps = {
    getPriceAlerts: actions.notifications.getPriceAlerts,
};
export default connect(() => {}, mapDispatchToProps)(PriceAlertOptions);