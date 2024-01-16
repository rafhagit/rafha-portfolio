// function genpass(e){
//     e.preventDefault();
//     var input_data = document.getElementById("generate").value;

//     console.log(input_data);
// }

document.addEventListener("DOMContentLoaded", function () {
    // Your code here
    function genpass(e) {
        e.preventDefault();

        var input_data = document.getElementById("generate").value;

        // Make a POST request to the API
        fetch("http://127.0.0.1:5000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ data: input_data })
        })
        .then(response => response.json())
        .then(result => {
            // Display the result in the console or update your UI as needed
            console.log(result);
            var newRes = result.body;
            // If you want to display the result in the HTML, you can do something like:
            document.getElementById("result").innerHTML = newRes;
        })
        .catch(error => {
            console.error("Error:", error);
            // Handle errors as needed
        });
    }

    // function gen_res(response) {
    //     var container = document.getElementById("gen_res"); 
    //     console.log(response.body)
    // }

    // Assuming you have an input button with id "generate"
    document.getElementById("generate").addEventListener("click", genpass);
});
