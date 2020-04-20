import axios from 'axios'
import { Dispatch } from 'redux'
import { Action } from '../reducers/AuthReducer'
import {Type} from './Types'
import {handleAxiosError} from './Utils'
import {fetchAuthToken} from "./Auth";

export const getAchievements = () => {
    return async (dispatch: Dispatch<Action>) => {
        try {
            const res = await axios.get('http://localhost:5000/achievement');
            dispatch({type: Type.SET_ACHIEVEMENTS, payload: res.data});
        } catch (e) {
            handleAxiosError(e, dispatch, Type.SET_ACHIEVEMENTS_FAILED);
        }
    }
}

export const getAchievementProfile = () => {
    return async (dispatch: Dispatch<Action>) => {
        try {
            await fetchAuthToken();
            const res = await axios.get('http://localhost:5000/achievement/profile');
            dispatch({type: Type.SET_ACHIEVEMENT_PROFILE, payload: res.data});
        } catch (e) {
            handleAxiosError(e, dispatch, Type.SET_ACHIEVEMENTS_FAILED);
        }
    }
};
