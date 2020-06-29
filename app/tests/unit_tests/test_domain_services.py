from pytest import mark
from pytest import raises

from fastapi import HTTPException

from domain.service.classic_service import ClassicService
from domain.service.rock_service import RockService
from domain.service.pop_service import PopService
from domain.model.city import City
from domain.model.track import Track


@mark.smoke
@mark.parametrize('temp', [(8.5)])
def test_classic_service(temp):
    classic_service = ClassicService()
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    track_list = classic_service.get_genre_playlist(city)

    for track in track_list:
        assert isinstance(track, Track)


@mark.smoke
@mark.parametrize('temp', [(26)])
def test_pop_service(temp):
    pop_service = PopService()
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    track_list = pop_service.get_genre_playlist(city)

    for track in track_list:
        assert isinstance(track, Track)


@mark.smoke
@mark.parametrize('temp', [(15)])
def test_rock_service(temp):
    rock_service = RockService()
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    track_list = rock_service.get_genre_playlist(city)

    for track in track_list:
        assert isinstance(track, Track)


@mark.sanity
@mark.parametrize('temp, expected_result', [(9, 'classical'),
                                            (15, 'rock'),
                                            (27, 'pop')])
def test_chain_of_responsibility(temp, expected_result):
    genre_service = ClassicService(RockService(PopService()))
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    track_list = genre_service.get_genre_playlist(city)

    for track in track_list:
        assert track.genre == expected_result


@mark.sanity
@mark.parametrize('temp, expected_result', [(135, HTTPException)])
def test_rock_service_error(temp, expected_result):
    rock_service = RockService()
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    with raises(Exception) as e:
        rock_service.get_genre_playlist(city)

    assert e.errisinstance(HTTPException)


@mark.sanity
@mark.parametrize('temp, expected_result', [(11, HTTPException)])
def test_classic_service_error(temp, expected_result):
    rock_service = ClassicService()
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    with raises(Exception) as e:
        rock_service.get_genre_playlist(city)

    assert e.errisinstance(HTTPException)


@mark.sanity
@mark.parametrize('temp, expected_result', [(24, HTTPException)])
def test_pop_service_error(temp, expected_result):
    rock_service = ClassicService()
    city = City(name="Test City", temperature=temp, searched_date="29/06/2020")

    with raises(Exception) as e:
        rock_service.get_genre_playlist(city)

    assert e.errisinstance(HTTPException)
