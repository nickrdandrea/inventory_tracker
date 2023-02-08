import { Buffer } from 'buffer';
import { BASE_URL } from '../config';

export default function loginUser(credentials, successCallback, failureCallback) {
    return fetch(BASE_URL + "login", {
        method: 'POST',
        mode: 'cors',
        credentials: 'same-origin',
        headers: {
            Authorization: 'Basic ' + 
            Buffer.from(credentials.username + ":" + credentials.password).toString('base64')
        }
    })
    .then(response => response.json())
    .then(userData => {
      successCallback({
        username: userData.username,
        id: userData.id,
        token: userData.access_token
      })
    })
    .catch(failureCallback("Error logging in."))
  }