from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security.purge_areas import PurgeAreas
    from ........models.security.purge_type import PurgeType

@dataclass
class PurgeDataPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The purgeAreas property
    purge_areas: Optional[PurgeAreas] = None
    # The purgeType property
    purge_type: Optional[PurgeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PurgeDataPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PurgeDataPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PurgeDataPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security.purge_areas import PurgeAreas
        from ........models.security.purge_type import PurgeType

        from ........models.security.purge_areas import PurgeAreas
        from ........models.security.purge_type import PurgeType

        fields: Dict[str, Callable[[Any], None]] = {
            "purgeAreas": lambda n : setattr(self, 'purge_areas', n.get_collection_of_enum_values(PurgeAreas)),
            "purgeType": lambda n : setattr(self, 'purge_type', n.get_enum_value(PurgeType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from ........models.security.purge_areas import PurgeAreas
        from ........models.security.purge_type import PurgeType

        writer.write_enum_value("purgeAreas", self.purge_areas)
        writer.write_enum_value("purgeType", self.purge_type)
        writer.write_additional_data_value(self.additional_data)
    

