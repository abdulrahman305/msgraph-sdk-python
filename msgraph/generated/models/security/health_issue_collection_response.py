from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
    from .health_issue import HealthIssue

from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse

@dataclass
class HealthIssueCollectionResponse(BaseCollectionPaginationCountResponse):
    # The value property
    value: Optional[List[HealthIssue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HealthIssueCollectionResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HealthIssueCollectionResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HealthIssueCollectionResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .health_issue import HealthIssue

        from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .health_issue import HealthIssue

        fields: Dict[str, Callable[[Any], None]] = {
            "value": lambda n : setattr(self, 'value', n.get_collection_of_object_values(HealthIssue)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from ..base_collection_pagination_count_response import BaseCollectionPaginationCountResponse
        from .health_issue import HealthIssue

        writer.write_collection_of_object_values("value", self.value)
    

