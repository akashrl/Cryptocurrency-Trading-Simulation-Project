import { Type } from '../actions/Types'

export type State = typeof initialState;
const initialState = {
  loggedIn: false,
  authToken: '',
  registrationErrorMessage: '',
  registrationLoading: false,
  loginErrorMessage: '',
  loginLoading: false,
  socket: null,
}

export type Action = {
  type: Type;
  payload?: any;
}

export type Auth = {
  loggedIn: boolean;
  authToken: string;
  registrationErrorMessage: string;
  registrationLoading: boolean;
  loginErrorMessage: string;
  loginLoading: boolean;
  socket: SocketIOClient.Socket;
}

export default (state = initialState, action: Action) => {
  switch (action.type) {
    case Type.LOGIN:
      return {
        ...state,
        loginErrorMessage: '',
        loginLoading: true,
      }
    case Type.LOGIN_FAILED:
      return {
        ...state,
        authToken: '',
        loginErrorMessage: action.payload,
        loginLoading: false,
      }
    case Type.LOGIN_SUCCEEDED:
      return {
        ...state,
        authToken: action.payload,
        loginErrorMessage: '',
        loginLoading: false,
        loggedIn: true,
      }
    case Type.SET_SOCKET:
      return {
        ...state,
        socket: action.payload,
      }
    case Type.LOGOUT:
      return initialState
    case Type.REGISTER:
      return {
        ...state,
        registrationErrorMessage: '',
        registrationLoading: true,
      }
    case Type.REGISTER_FAILED:
      return {
        ...state,
        authToken: '',
        registrationErrorMessage: action.payload,
        registrationLoading: false,
      }
    case Type.REGISTER_SUCCEEDED:
      return {
        ...state,
        authToken: action.payload,
        registrationErrorMessage: '',
        registrationLoading: false,
        loggedIn: true,
      }
    default:
      return state
  }
}
