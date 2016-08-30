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


class RegistryStatistics(Model):
    """The properties related to the registry statistics.

    :param total_device_count: The total device count.
    :type total_device_count: long
    :param enabled_device_count: The enabled device count.
    :type enabled_device_count: long
    :param disabled_device_count: The disabled device count.
    :type disabled_device_count: long
    """ 

    _attribute_map = {
        'total_device_count': {'key': 'totalDeviceCount', 'type': 'long'},
        'enabled_device_count': {'key': 'enabledDeviceCount', 'type': 'long'},
        'disabled_device_count': {'key': 'disabledDeviceCount', 'type': 'long'},
    }

    def __init__(self, total_device_count=None, enabled_device_count=None, disabled_device_count=None):
        self.total_device_count = total_device_count
        self.enabled_device_count = enabled_device_count
        self.disabled_device_count = disabled_device_count
