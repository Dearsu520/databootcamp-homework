
d3.json(ALL_EARTHQUAKES_7_DAYS).then((data) => {
    var features = data.features;

    var streetmap = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: API_KEY
    });

    var darkmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "dark-v10",
        accessToken: API_KEY
    });

    var baseMaps = {
        "Street Maps": streetmap,
        "Dark Maps": darkmap
    };

    var mymap = L.map('mapid', {
        center: [0, 0], 
        zoom: 2,
        layers: [darkmap]
    });

    L.control.layers(baseMaps).addTo(mymap);

    var color = d3.scaleOrdinal()
        .domain([0, 8])
        .range([150, 200]);

    features.forEach(d => {
        var longitude = d.geometry.coordinates[0];
        var latitude = d.geometry.coordinates[1];
        var depth = d.geometry.coordinates[2];
        var magnitude = d.properties.mag; 
        L.circle([latitude, longitude], {
            color: "#" + (255).toString(16) + (color(depth)).toString(16) + (255).toString(16),
            fillOpacity: 0.8,
            radius: 20000 * magnitude
        }).addTo(mymap).bindPopup("<h3>" + d.properties.place +
            "</h3><hr><p>" + new Date(d.properties.time) + "</p>");
    });

    var legend = L.control({position: 'topright'});
    legend.onAdd = function (map) {
        function getColor(d) {
            return d === '0-1'  ? "#ff96ff" :
                d === '1-2'  ? "#ff9dff" :
                d === '2-3' ? "#ffa5ff" :
                d === '3-4' ? "#ffadff" :
                d === '4-5' ? "#ffb4ff" :
                d === '5-6' ? "#ffbbff":
                d === '6-7' ? "#ffc2ff":
                "#ffc8ff";
        }

        var div = L.DomUtil.create('div', 'info legend');
        labels = ['<strong>Categories</strong>'],
        categories = ['0-1','1-2','2-3','3-4','4-5', '5-6', '6-7', '7-8'];

        for (var i = 0; i < categories.length; i++) {

                div.innerHTML += 
                labels.push(
                    '<span class="dot" style="display:inline-block;width:20px;height:20px;margin-right:20px;background:' + getColor(categories[i]) + '"></span> ' +
                (categories[i] ? categories[i] : '+'));

            }
            div.innerHTML = labels.join('<br>');
        return div;
    };
    legend.addTo(mymap);
});