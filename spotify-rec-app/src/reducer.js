// reducer.js
import {
  REQUEST_SUCCESSFUL,
  REQUEST_STARTED,
  REQUEST_FAILED }
  from "./constants";

// a reducer receives the current state, and an action
export const reducer = (state, action) => {
  // we check the type of each action and return an updated state object accordingly
  switch (action.type) {
    case REQUEST_STARTED:
      return {
        ...state,
        isLoading: true,
      };
    case REQUEST_SUCCESSFUL:
      return {
        ...state,
        isLoading: false,
        error: null,
        data: action.data,
      };
    case REQUEST_FAILED:
      return {
        ...state,
        isLoading: false,
        error: action.error,
      };

    // usually I ignore the action if its `type` is not matched here, some people prefer throwing errors here - it's really up to you.
    default:
      return state;
  }
};