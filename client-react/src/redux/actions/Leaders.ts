import { Type } from './Types';
import axios from 'axios'; 
import { Dispatch } from 'redux';
import { Action } from '../reducers/AuthReducer';

export const getAllLeaders = () => {
  return async (dispatch: Dispatch<Action>) => {
      const res = await axios.get('http://localhost:5000/game/coins');
      dispatch({type: Type.SET_LEADERS, payload: res.data});
  }
};
