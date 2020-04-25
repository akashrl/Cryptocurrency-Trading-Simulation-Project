import React from 'react';
import {
    Form,
    Button,
} from 'react-bootstrap';
import { toast } from 'react-toastify';

interface CreateLeaderAlertFormState {
    strikePrice: number;
}

interface CreateLeaderAlertProps {
    submit: (strikePrice: number) => void;
    listOfLeaders: Array<{
        id: number;
        name: string;
        score: number;
      }>;
}

class CreateLeaderAlertForm extends React.Component<CreateLeaderAlertProps, CreateLeaderAlertFormState> {
    constructor(props: CreateLeaderAlertProps) {
        super(props);
        this.state = {
            strikePrice: 0,
        }
    }

    submit() {
        if (isNaN(this.state.strikePrice)) {
            alert('Please enter a valid number for the Leader');
            return;
        }
        this.props.submit(
            this.state.strikePrice,
        )
        let fragment = 'Leaders: ';
        const list = this.props
                    .listOfLeaders
                    .filter(item => item.score >= this.state.strikePrice)
                    .forEach(element => {
                        fragment += `${element.name}: ${element.score}; `;
                    });
        toast(fragment)
    }

    render() {
        return (
            <Form onSubmit={() => this.submit()}>
                <Form.Group>
                    <Form.Control
                        value={this.state.strikePrice}
                        onChange={(event: React.FormEvent<HTMLInputElement>) => this.setState({strikePrice: event.currentTarget.value})}
                    />
                </Form.Group>
                <Form.Group>
                    <Button onClick={() => this.submit()}>Submit</Button>
                </Form.Group>
            </Form>
        )
    }
}

export default CreateLeaderAlertForm;