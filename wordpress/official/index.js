import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { getDatabase, ref, update } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-database.js";


const firebaseApp = initializeApp({
    apiKey: "AIzaSyACZAxX8UyYt7zChLk-p8LGh5g9k4yiu1Y",
    authDomain: "ticketsa-26792.firebaseapp.com",
    databaseURL: "https://ticketsa-26792-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "ticketsa-26792",
    storageBucket: "ticketsa-26792.appspot.com",
    messagingSenderId: "936017910371",
    appId: "1:936017910371:web:c91db6306c698e3615f656",
    measurementId: "G-1V0WP4RMR3"
});




function writeUserData() {
  const db = getDatabase(firebaseApp);
  update(ref(db, 'users/8D8AEB2D/ticket_data/'), {
    SAZLEJ:1
  });
} 

document.getElementById ("saz").addEventListener ("click", writeUserData, false);