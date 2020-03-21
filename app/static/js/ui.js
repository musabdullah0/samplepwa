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
async function centerMap() {
    const pos = await getLocation();
    const lat = pos.coords.latitude;
    const long = pos.coords.longitude;
    const latlang = new google.maps.LatLng(lat, long);
    map.setCenter(latlang);
    console.log('new center at', latlang);
}
centerMap();
