window.addEventListener('DOMContentLoaded', (event) => {
    getVisitCount();
});

const FunctionApi = 'https://cloudresume-funcapp.azurewebsites.net/api/read-items/webpage01?code=QlikjJ297T63ZPxhm9zWaD0dkOgXfsy0oTarejbND_YXAzFutFHANA%3D%3D';

const getVisitCount = () => {
    fetch(FunctionApi).then(response => {
        return response.text(); // Changed from response.json() to response.text()
    }).then(text => {
        console.log("Webpage called function API.");
        console.log('Data received:', text);
        document.getElementById("counter").innerText = text;
    }).catch(function(error){
        console.log(error);
    });
};
