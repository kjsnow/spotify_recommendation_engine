import {
  REQUEST_SUCCESSFUL,
  REQUEST_STARTED,
  REQUEST_FAILED }
  from "./constants";

export const requestSuccessful = ({ data }) => ({
  type: REQUEST_SUCCESSFUL,
  data,
});
export const requestStarted = () => ({
  type: REQUEST_STARTED,
});
export const requestFailed = ({ data }) => ({
  type: REQUEST_FAILED,
  data,
});