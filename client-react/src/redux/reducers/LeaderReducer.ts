import {} from '../actions/Types';
import {Type} from "../actions/Types";

export type LeaderState = typeof initialState;
const initialState = {
    leaders: [] as Array<{ id: number, name: string, score: string }>,
};

export type Action = {
    type: Type;
    payload?: any;
};

export default (state = initialState, action: Action) => {
    switch (action.type) {
        case Type.SET_LEADERS:
            return {
                ...state,
                leaders: action.payload,
            };
        default:
            return state
    }
}
