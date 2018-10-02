# import pandas
import json


def main():
    polygons = [
        [
            [-122.27783203125, 37.79296875],
            [-122.27783203125, 37.7874755859375],
            [-122.288818359375, 37.7874755859375],
            [-122.288818359375, 37.79296875], 4
        ]
    ]

    for polygon in polygons:
        polygon_context = get_polygon_context(polygon)
        print(json.dumps(get_geojson(polygon_context)))


def get_polygon_context(polygon):
    """ store polygon as {"value": val, "coordinates": []}
    """
    return {
        "value": polygon[-1],
        "coordinates": polygon[:-1]
    }


def get_geojson(polygon_context):
    """ get geojson format from polygon_context
    """
    return {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [polygon_context["coordinates"]]
        },
        "properties": {
            "name": polygon_context["value"]
        }
    }


main()
