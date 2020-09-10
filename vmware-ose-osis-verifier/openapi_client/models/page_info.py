# coding: utf-8

"""
    Object Storage Interoperability Services API

    This is VMware Cloud Director Object Storage Interoperability Services API. Once storage platform vendor implements REST APIs complying with this specification, Object Storage Extension can integrate with the platform without coding effort.  # noqa: E501

    The version of the OpenAPI document: 1.0.0-oas3
    Contact: wachen@vmware.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class PageInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'total': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'total': 'total'
    }

    def __init__(self, limit=None, offset=None, total=None, local_vars_configuration=None):  # noqa: E501
        """PageInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._limit = None
        self._offset = None
        self._total = None
        self.discriminator = None

        self.limit = limit
        self.offset = offset
        self.total = total

    @property
    def limit(self):
        """Gets the limit of this PageInfo.  # noqa: E501

        maxium number of the items in each page  # noqa: E501

        :return: The limit of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageInfo.

        maxium number of the items in each page  # noqa: E501

        :param limit: The limit of this PageInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this PageInfo.  # noqa: E501

        offset of the current page in the whole set of items  # noqa: E501

        :return: The offset of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageInfo.

        offset of the current page in the whole set of items  # noqa: E501

        :param offset: The offset of this PageInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def total(self):
        """Gets the total of this PageInfo.  # noqa: E501

        total number of the items  # noqa: E501

        :return: The total of this PageInfo.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PageInfo.

        total number of the items  # noqa: E501

        :param total: The total of this PageInfo.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PageInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageInfo):
            return True

        return self.to_dict() != other.to_dict()
