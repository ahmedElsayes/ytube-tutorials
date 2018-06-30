/**
 * Created by Andrei Lobov.
 *
 * Works in CONJUCTION with HTML.
 *
 */
$(document).ready(function() {

    $('#myButton').click(function(event){

        var urlVal = $('#txtUrl').val(); //Retrieving output information from HTML
        var dataVal = $('#txtPayload').val(); //Getting value information from HTML
        var dataType = $('#selType').val();

        var gatewayURL = "http://127.0.0.1:4590"

        var messageForGateway = "{\"url\":\"" + urlVal + "\",\n\"payload\":" + dataVal + ",\"type\":\"" + dataType + "\"}";

        // Commented out, but alert command can be used for debugging on the web browser side.
       // alert(messageForGateway);


        $.ajax({
            type: "POST",
            url:gatewayURL,
            data: messageForGateway,
            dataType: "json",
            contentType:"application/json"
        })

    });
});