# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements


def load_arguments(self, _):

    with self.argument_context('term show') as c:
        c.argument('publisher', type=str, help='Publisher identifier string of image being deployed.')
        c.argument('product', type=str, help='Offeridentifier string of image being deployed.')
        c.argument('plan', type=str, help='Plan identifier string of image being deployed.')

    with self.argument_context('term accept') as c:
        c.argument('publisher', type=str, help='Publisher identifier string of image being deployed.')
        c.argument('product', type=str, help='Offer identifier string of image being deployed.')
        c.argument('plan', type=str, help='Plan identifier string of image being deployed.')
