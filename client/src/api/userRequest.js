import axios from 'axios';

const baseURL = "http://localhost:5000";

export const postUserData = async (userData) => {
  try {
    const response = await axios.post(`${baseURL}/users`, userData);
    return response.data;
  } catch (error) {
    console.log("POST request failed:", error);
    return null;
  }
};

export const getUserData = async (userId) => {
  try {
    const response = await axios.get(`${baseURL}/users/${userId}`);
    return response.data;
  } catch (error) {
    console.log("GET request failed:", error);
    return null;
  }
};
