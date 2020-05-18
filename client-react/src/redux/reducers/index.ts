import { combineReducers } from "redux";
import { connectRouter } from "connected-react-router";
import * as H from "history";

import AuthReducer, { Auth } from "./AuthReducer";
import CoinReducer, { CoinState } from "./CoinReducer";
import FriendsReducer, { FriendsState } from "./FriendsReducer";
import GameReducer, { GameState } from "./GameReducer";
import NotificationsReducer, {
  NotificationState,
} from "./NotificationsReducer";
import LeaderReducer, { LeaderState } from "./LeaderReducer";
import PlayReducer, { PlayState } from "./PlayReducer";
import AdminReducer, { AdminState } from "./AdminReducer";
import AchievementReducer, { AchievementState } from "./AchievementReducer";

export type RootState = {
  router: any;
  auth: Auth;
  coins: CoinState;
  friends: FriendsState;
  game: GameState;
  notifications: NotificationState;
  leaders: LeaderState;
  play: PlayState;
  admin: AdminState;
  achievement: AchievementState;
};

const rootReducer = (history: H.History) =>
  combineReducers({
    router: connectRouter(history),
    auth: AuthReducer,
    coins: CoinReducer,
    friends: FriendsReducer,
    game: GameReducer,
    notifications: NotificationsReducer,
    leaders: LeaderReducer,
    play: PlayReducer,
    admin: AdminReducer,
    achievement: AchievementReducer,
  });

export default rootReducer;
