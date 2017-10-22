$(document).ready(function() {
var map;

  function initMap() {
    // var myLatLng ={{ result|safe }}
    var myLatLng = {lat: 37.775, lng: -122.434};

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: myLatLng
    });

    
    var marker = new google.maps.Marker({
      position: myLatLng,
      map: map,
      title: 'Hello World!'
    });
  }

  google.maps.event.addDomListener(window, 'load', initMap);

})