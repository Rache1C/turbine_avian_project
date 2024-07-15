import pytest
from camera_bird_detection import get_camera_coordinates

def test_lat_long():
    coordinates = get_camera_coordinates()
    assert isinstance(coordinates, tuple)