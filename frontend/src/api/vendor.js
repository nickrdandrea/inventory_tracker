import { BASE_URL } from '../config';

const BASE_API_URL = process.env.REACT_APP_BASE_API_URL;

export function getVendorItems(vendor_name, successCallback, failureCallback) {
    return fetch(BASE_API_URL)
    .then(response => response.json())
    .then(vendorItems => successCallback(vendorItems))
    .catch(error => failureCallback(error.response.statusText))
}

export function searchVendorItems(vendor_name, terms, successCallback, failureCallback) {
    const searchTerms = terms.trim().replace(' ', '&');
    const searchURL = BASE_URL + 'search?' + 'terms=' + searchTerms;
    return fetch(searchURL, {
        method: 'GET',
        mode: 'cors',
        credentials: 'same-origin',
    })
    .then(response => response.json())
    .then(vendorItems => successCallback(vendorItems))
    .catch(error => failureCallback(error.response.statusText))
}