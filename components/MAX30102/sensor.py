import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    UNIT_BEATS_PER_MINUTE,
    UNIT_PERCENT,
    DEVICE_CLASS_HEART_RATE,
    DEVICE_CLASS_OXYGEN_SATURATION,
)

DEPENDENCIES = ["i2c"]

max30102_ns = cg.esphome_ns.namespace("max30102")
MAX30102Sensor = max30102_ns.class_("MAX30102Sensor", cg.PollingComponent, sensor.Sensor)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(MAX30102Sensor),
    }
).extend(cv.polling_component_schema("1s"))

async def to_code(config):
    var = cg.new_Pvariable(config[cv.GenerateID()])
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
