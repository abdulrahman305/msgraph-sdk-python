from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .vulnerability_severity import VulnerabilitySeverity

@dataclass
class CvssSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The CVSS score about this vulnerability.
    score: Optional[float] = None
    # The CVSS severity rating for this vulnerability. The possible values are: none, low, medium, high, critical, unknownFutureValue.
    severity: Optional[VulnerabilitySeverity] = None
    # The CVSS vector string for this vulnerability.
    vector_string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CvssSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CvssSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CvssSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .vulnerability_severity import VulnerabilitySeverity

        from .vulnerability_severity import VulnerabilitySeverity

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "score": lambda n : setattr(self, 'score', n.get_float_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(VulnerabilitySeverity)),
            "vectorString": lambda n : setattr(self, 'vector_string', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_float_value("score", self.score)
        writer.write_enum_value("severity", self.severity)
        writer.write_str_value("vectorString", self.vector_string)
        writer.write_additional_data_value(self.additional_data)
    

