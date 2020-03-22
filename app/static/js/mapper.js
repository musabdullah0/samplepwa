// gets position of user
function getLocation() {
    if (navigator.geolocation) {
        const options = { enableHighAccuracy: true }
        return new Promise((res, rej) => {
            navigator.geolocation.getCurrentPosition(res, rej, options);
        });
    } else {
        console.log("Geo Location not supported by browser");
    }
}

// get location then move map to center at it
async function centerMap() {
    const pos = await getLocation();
    const lat = pos.coords.latitude;
    const long = pos.coords.longitude;
    const latlang = new google.maps.LatLng(lat, long);
    map.setCenter(latlang);
    console.log('new center at', latlang);
}

// add user to map
const addSessionToMap = data => {
    var latlang = new google.maps.LatLng(data.latitude, data.longitude);
    var icon = {
        url: 'static/img/bluedot.png', // url
        scaledSize: new google.maps.Size(50, 50), // scaled size
    };
    var marker = new google.maps.Marker({
        position: latlang,
        label: data.name,
        map: map,
    });
    if (user.email.valueOf() == data.email.valueOf()) {
        marker.setDraggable(true);
        marker.setIcon(icon);
    }
    console.log('added marker at', latlang, data.email)
}

// start doing stuff
centerMap();

db.ref('sessions').on('value', snapshot => {
    snapshot.val().forEach(change => {
        addSessionToMap(change);
    });
});