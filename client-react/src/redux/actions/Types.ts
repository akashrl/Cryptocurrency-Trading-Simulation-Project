export enum Type {
    // auth types
    LOGIN,
    LOGIN_FAILED,
    LOGIN_SUCCEEDED,
    REGISTER,
    REGISTER_FAILED,
    REGISTER_SUCCEEDED,
    LOGOUT,
    VERIFY_AUTH_TOKEN,
    VERIFY_AUTH_TOKEN_SUCCEEDED,
    CHANGE_USERNAME_SUCCEEDED,
    SET_CHANGE_USERNAME_FAILED,
    CHANGE_PASSWORD_SUCCEEDED,
    SET_CHANGE_PASSWORD_FAILED,
    SET_VERIFY_FAILED,

    // coin types
    SET_SIMPLE_COINS,
    SET_COINS,
    SET_GAME_COINS,
    SET_CURRENT_PRICES,
    SET_COIN_AMOUNT,

    // game types
    CREATE_GAME,
    CREATE_GAME_FAILED,
    GET_ACTIVE_GAMES,
    GET_ACTIVE_GAMES_FAILED,
    JOIN_GAME,
    JOIN_GAME_FAILED,
    SET_GAME,
    SET_GAME_FAILED,
    SET_GAME_PROFILE,
    SET_CASH,
    LIQUIFY_FAILED,
    TRANSACTION,
    TRANSACTION_FAILED,

    SET_REGISTRATION_ERROR,
    SET_LOGIN_ERROR,

    CLEAR_ERRORS,

    // notification types
    GET_NOTIFICATIONS,
    GET_NOTIFICATIONS_SUCCEEDED,
    GET_NOTIFICATIONS_FAILED,
    GET_PRICE_ALERTS,
    GET_PRICE_ALERTS_SUCCEEDED,
    GET_PRICE_ALERTS_FAILED,
    CREATE_PRICE_ALERT,
    CREATE_PRICE_ALERT_SUCCEEDED,
    CREATE_PRICE_ALERT_FAILED,

    SET_SOCKET,

    // friends Types
    SET_FRIEND_REQUEST,
    ACCEPT_FRIEND_REQUEST,
    FRIEND_FAILED,
    GET_PENDING,
    GET_FRIENDS,
    GET_PENDING_FAILED,
    GET_LIST_FAILED,
}
