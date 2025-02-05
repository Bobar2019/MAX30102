import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    UNIT_BEATS_PER_MINUTE,
    UNIT_PERCENT
)

DEPENDENCIES = ["i2c"]

max30102_ns = cg.esphome_ns.namespace("max30102")
MAX30102Sensor = max30102_ns.class_("MAX30102Sensor", cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = sensor.sensor_schema(
    MAX30102Sensor,
    accuracy_decimals=0,
    unit_of_measurement=UNIT_BEATS_PER_MINUTE,
).extend(cv.polling_component_schema("1s"))


async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
