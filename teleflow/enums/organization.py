"""This module is used to gather enumerations related to the Provider resource in Teleflow"""

from teleflow.enums.polyfill import StrEnum


class OrganizationBrandingDirection(StrEnum):
    """This enumeration define possible direction in a Teleflow organization branding"""

    LEFT_TO_RIGHT = "ltr"
    """Left to right"""

    RIGHT_TO_LEFT = "trl"
    """Right to left"""


class PartnerTypeEnum(StrEnum):
    """This enumeration define possible partner type"""

    VERCEL = "vercel"
    """Vercel partner type"""
