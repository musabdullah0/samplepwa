// gets latlang of user
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        console.log("Geo Location not supported by browser");
    }
}

// helper for getLocation
function showPosition(position) {
    var location = {
        longitude: position.coords.longitude,
        latitude: position.coords.latitude
    }
    console.log(location)
}

//request for location
function getLocationWrapper() {
    return new Promise(() => {
        navigator.geolocation.getCurrentPosition(showPosition);
    });
}


// initialize google maps object
let initializeMap = () => {
    let mapProp = {
        center: new google.maps.LatLng(30.565990399999993, -97.64536319999999),
        zoom: 5
    }
    let map = new google.maps.Map(document.getElementById('myMap'), mapProp)
}


// add user to map
// update to put blue marker if same as auth user
const addUserToMap = (id, data) => {
    var latlang = new google.maps.LatLng(data.latitude, data.longitude);
    var marker = new google.maps.Marker({
        position: latlang,
        label: data.name,
        map: map
    });
    console.log('added marker at', latlang)
}

// real-time listener
db.collection('users').onSnapshot(snapshot => {
    // console.log(snapshot.docChanges());
    snapshot.docChanges().forEach(change => {
        // console.log(change.type, change.doc.id, change.doc.data());
        if (change.type === 'added') {
            // add the document data to the web page
            addUserToMap(change.doc.id, change.doc.data());
        }
        if (change.type === 'removed') {
            // remove the document data from the web page
        }
    });
});

// get location then move map to center at it
// getLocationWrapper().then(pos => {
//     console.log('got new center');
//     const latlang = new google.maps.LatLng(pos.latitude, pos.longitude);
//     map.setCenter(latlang);
//     console.log('new center at', latlang);
// });
