import folium

m = folium.Map(location=[44.9794, -93.2761], zoom_start=9)

# python foliumtests.py in terminal to obtain html file
m.save("map1.html")

