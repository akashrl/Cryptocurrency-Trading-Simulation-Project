import React from 'react'
import {
    Button,
    Tab,
    Tabs,
} from 'react-bootstrap'
import { connect } from 'react-redux'
import { RootState } from '../redux/reducers';
import Actions from '../redux/actions'
import { Notification } from '../redux/reducers/NotificationsReducer'
import NotificationsPagingList from './NotificationsPagingList';
import PriceAlertOptions from './PriceAlertOptions';

interface NotificationsState {
    page: number;
}

interface NotificationsProps {
    notifications: Array<Notification>;
    authToken: string;
    fetchAuthToken: () => void;
    getNotifications: (page: number) => void;
}



class Notifications extends React.Component<NotificationsProps, NotificationsState> {
    private tabs: Array<{title: string, component: JSX.Element}> = [];

    constructor(props: NotificationsProps) {
        super(props);
        this.state = {
            page: 0,
        }
        this.tabs = [
            {
                title: 'My Notifications',
                component: (<>
                    <Button style={{margin: '30px 0 30px 0'}} onClick={() => this.props.getNotifications(this.state.page)}>Refresh</Button>
                    <NotificationsPagingList/>
                </>)
            },
            {
                title: 'Price Alert Options',
                component: <PriceAlertOptions/>
            }
        ];
    }

    render() {
        return (
            <div className="container">
                <div className="col-md-12">
                    <h1>Notifications</h1>
                    <Tabs id='notification-tabbing' defaultActiveKey={this.tabs[0].title}>
                        {this.tabs.map((tab) => 
                            <Tab eventKey={tab.title} title={tab.title}>
                                {tab.component}
                            </Tab>
                        )}
                    </Tabs>
                </div>
            </div>
        )
    }
}

const mapStateToProps = (state: RootState) => ({
    notifications: state.notifications.notifications,
    authToken: state.auth.authToken,
});
const mapDispatchToProps = {
    fetchAuthToken: Actions.auth.fetchAuthToken,
    getNotifications: Actions.notifications.getNotifications,
};
export default connect(mapStateToProps, mapDispatchToProps)(Notifications);
