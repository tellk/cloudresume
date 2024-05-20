windows.addEventListener('DOMContentLoaded', (event) =>{
	getVisitCount();
})

  const FunctionApi = '';

  const getVisitCount = () => {
      let count = 30;
      fetch(FunctionApi).then(response => {
          return response.json()
      }).then(response => {
          console.log("Webpage called function API.");
          count = response.count;
          document.getElementById("counter").innerText = count;
      }).catch(function(error){
          console.log(error);
      });

      return count;
  }
