#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------
#pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class IotHubCapacity(Model):
    """The properties related to the capacity information.

    :param minimum: The minimum number of units.
    :type minimum: long
    :param maximum: The maximum number of units.
    :type maximum: long
    :param default: The default number of units.
    :type default: long
    :param scale_type: The type of the scale. Possible values include:
     'Automatic', 'Manual', 'None'
    :type scale_type: str or :class:`IotHubScaleType
     <iothubclient.models.IotHubScaleType>`
    """ 

    _validation = {
        'minimum': {'maximum': 1, 'minimum': 1},
    }

    _attribute_map = {
        'minimum': {'key': 'minimum', 'type': 'long'},
        'maximum': {'key': 'maximum', 'type': 'long'},
        'default': {'key': 'default', 'type': 'long'},
        'scale_type': {'key': 'scaleType', 'type': 'IotHubScaleType'},
    }

    def __init__(self, minimum=None, maximum=None, default=None, scale_type=None):
        self.minimum = minimum
        self.maximum = maximum
        self.default = default
        self.scale_type = scale_type
