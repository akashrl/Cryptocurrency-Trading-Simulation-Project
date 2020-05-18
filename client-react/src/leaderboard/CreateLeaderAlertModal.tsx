import React from 'react'
import { Modal } from 'react-bootstrap'
import CreateLeaderAlertForm from './CreateLeaderAlertForm';

interface CreatePriceAlertModalProps {
  open: boolean;
  close: () => void;
  listOfLeaders: Array<{
    id: number;
    name: string;
    score: number;
  }>;
}

class CreatePriceAlertModal extends React.Component<CreatePriceAlertModalProps> {

  submit = () => {
    this.props.close();
  };

  render() {
    return (
      <Modal centered size='lg' show={this.props.open} onHide={this.props.close}>
        <Modal.Header closeButton>
          <Modal.Title>Create a notification for a score value:</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <CreateLeaderAlertForm listOfLeaders={ this.props.listOfLeaders } submit={this.submit}/>
        </Modal.Body>
      </Modal>
    )
  }
}

export default CreatePriceAlertModal;
