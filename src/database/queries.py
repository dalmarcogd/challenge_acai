from typing import Dict
from uuid import UUID

import ujson
from sqlalchemy.orm import Query

from weather_forecast.database.models.weather_forecast import WeatherForecast, WeatherForecastStatus
from weather_forecast.database.utils import db_session


def create_weather_forecast(weather_forecast_params: Dict) -> Dict:
    with db_session() as session:
        weather_forecast = WeatherForecast()
        weather_forecast.params = ujson.dumps(weather_forecast_params)
        session.add(weather_forecast)
        session.commit()
        return weather_forecast.to_dict()


def update_weather_forecast(
    weather_forecast_result: Dict, status: WeatherForecastStatus
) -> Dict:
    with db_session() as session:
        weather_forecast: WeatherForecast = Query(
            WeatherForecast, session=session
        ).filter_by(id=weather_forecast_result["id"]).one()
        weather_forecast.result = ujson.dumps(weather_forecast_result)
        weather_forecast.status = status
        return weather_forecast.to_dict()


def get_weather_forecast(weather_forecast_id: UUID) -> Dict:
    with db_session() as session:
        weather_forecast: WeatherForecast = Query(
            WeatherForecast, session=session
        ).filter_by(id=weather_forecast_id).one()
        return weather_forecast.to_dict()
